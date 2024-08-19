from random import shuffle
from re import T
from tkinter import N
import numpy as np
import matplotlib.pyplot as plt
import time
from copy import copy

import torch
from torch.autograd import Function
from torchvision import datasets, transforms
import torch.optim as optim
import torch.nn as nn
import torch.nn.functional as F

import qiskit
from qiskit.visualization import *

# training data
n_samples = 100
X_train = datasets.MNIST(
    root='./data', 
    train=True, 
    download=True, 
    transform=transforms.Compose([transforms.ToTensor()])
)

idx = np.append(np.where(X_train.targets == 0)[0][:n_samples],
                np.where(X_train.targets == 1)[0][:n_samples])

# print('idx =', idx)
# print('len(idx) =', len(idx))

X_train.data = X_train.data[idx]
X_train.targets = X_train.targets[idx]

train_loader = torch.utils.data.DataLoader(X_train, batch_size=16, shuffle=True)

n_sample_show = 6
data_iter = iter(train_loader)
fig, axes = plt.subplots(nrows=1, ncols=n_sample_show, figsize=(10, 3))

while n_sample_show > 0:
    images, targets = data_iter.__next__()
    images = (torch.nn.AvgPool2d(3)(images))
    axes[n_sample_show-1].imshow(images[0][0].numpy(), cmap='gray')
    axes[n_sample_show-1].set_xticks([])
    axes[n_sample_show-1].set_yticks([])
    axes[n_sample_show-1].set_title('Labeled: {}'.format(targets[0].item()))
    n_sample_show -= 1

#print('images.shape =', images.shape)
#plt.show()


# test data
n_samples = 50
X_test = datasets.MNIST(
    root='./data', 
    train=False, 
    download=True, 
    transform=transforms.Compose([transforms.ToTensor()])
)
idx = np.append(np.where(X_test.targets == 0)[0][:n_samples],
                np.where(X_test.targets == 1)[0][:n_samples])
X_test.data = X_test.data[idx]
X_test.targets = X_test.targets[idx]

test_loader = torch.utils.data.DataLoader(X_test, batch_size=16, shuffle=True)

#########################################################################################

class QMLCircuit:
    def __init__(self, n_qubits, backend):
        # 学習用量子回路の作成
        self.qc = qiskit.QuantumCircuit(n_qubits, 1)
        self.n_params = 3 * (2 * n_qubits + 1)
        self.n_qubits = n_qubits
        self.all_qubits = [i for i in range(n_qubits)]
        self.params = [qiskit.circuit.Parameter('p{}'.format(i)) for i in range(self.n_params)]

        for qubit in self.all_qubits:
            self.qc.u(self.params[3*qubit],
                            self.params[3*qubit + 1],
                            self.params[3*qubit + 2],
                            qubit)
        self.qc.barrier()

        for qubit in self.all_qubits:
            control = qubit
            target = (qubit + 1) % n_qubits
            self.qc.cu3(self.params[3*n_qubits + 3*qubit],
                        self.params[3*n_qubits + 3*qubit + 1],
                        self.params[3*n_qubits + 3*qubit + 2],
                        control_qubit = control,
                        target_qubit = target)
        self.qc.u(self.param[-3], self.param[-2], self.param[-1], self.n_qubits - 1)
        self.backend = backend
    
    def run(self, data, param):
        param_dict = {}
        params = tuple(param.detach().numpy())
        for i in range(self.n_params):
            param_dict[self.params[i]] = params[i]

        # データを振幅エンコーディングした量子回路を作成し、学習用量子回路と結合
        init_circ = qiskit.QuantumCircuit(self.n_qubits, 1)
        init_statevec = self.amplitude_embedding(data)
        init_circ.initialize(init_statevec, self.all_qubits)
        self.qc = init_circ + self.qc
        self.bound_circuit = self.qc.bind_parameters(param_dict)

        # 量子回路を実行
        job = qiskit.execute(self.bound_circuit, self.backend, )

        # 状態ベクトルを取得し、期待値を計算
        outputstate = job.result().get_statevector(self.bound_circuit)
        expectation = np.sum((np.abs(outputstate)**2)[2**(self.n_qubits -1):])
        return np.array([expectation])

    def amplitude_embedding(self, data):
        data = np.array(data, dtype=np.float)
        dim = 2 ** self.n_qubits
        if len(data) < dim:
            data = np.pad(data, (0, dim-len(data)), 'constant', constant_values=(0, 0))
        if np.sum(data**2) == 0:
            data += 1
        vec = data / np.sqrt(np.sum(data**2))
        return vec

class HybridFunction(Function):

    @staticmethod
    def forward(ctx, f, data, params):
        # 順伝播の計算
        def f_each(data, params):
            return torch.tensor([f(torch.flatten(d), params) for d in data], dtype=torch.float64)

        expectation_z = f_each(data, params)
        ctx.save_for_backward(data, params, expectation_z)
        ctx.f = f_each
        return expectation_z

    @staticmethod
    def backward(ctx, grad_output):
        # 逆伝播の計算
        