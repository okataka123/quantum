from qiskit import QuantumCircuit
from qiskit.circuit.library import ZGate, CRZGate
from qiskit.circuit import ControlledGate
 
def solve(n: int, L: int, theta: float) -> QuantumCircuit:
    qc = QuantumCircuit(n)
    # Write your code here:
    
    all_one = False

    if L == 2**n-1:
        qc.mcrz(-2*theta, range(n-1), n-1)
        return qc    

    cnt = 0
    for j in range(n):
        if (L >> j) & 1 == 0:
            qc.x(j)
            cnt += 1
    print('cnt =', cnt)
    if cnt != 0:
        qc.mcrz(-2*theta, range(n-1), n-1)
    for j in range(n):
        if (L >> j) & 1 == 0:
            qc.x(j)
    return qc

"""

1.57079633

2 1 1.57079633
"""



######################################################
import matplotlib.pyplot as plt
from qiskit_aer import Aer
import math

def visualization(qc):
    qc.draw('mpl')
    plt.show()


def get_state(qc):
    qc = qc.decompose(reps=5)
    sim = Aer.get_backend('statevector_simulator')
    res = sim.run(qc).result()
    state = res.data()['statevector']
    print('state =', state)


def create_input_qc():
    '''
    oracleに入力する初期状態を作る。
    '''
    qc = QuantumCircuit(2)
    coeff = 1/2
    qc.initialize([coeff]*4)
    return qc

def make_oracle():
    n, L, theta = map(float, input().split())
    n = int(n)
    L = int(L)
    qc = solve(n, L, theta)
    oracle_gate = qc.to_gate()
    oracle_gate.name = 'oracle'
    return oracle_gate
    
def main():
    #qc = solve()
    qc = create_input_qc()
    oracle_gate = make_oracle()
    qc.append(oracle_gate, [0, 1])

    #visualization(qc)
    get_state(qc)

if __name__ == '__main__':
    main()


'''
output

state = Statevector([-6.70078871e-17+5.55111512e-17j,
              7.07106781e-01-1.38777878e-17j,
             -2.77555756e-17+1.38777878e-16j,
             -1.11022302e-16+2.22044605e-16j,
             -5.55111512e-17+2.77555756e-16j,
             -2.15704154e-32-1.84889275e-32j,
              7.07106781e-01+5.55111512e-17j,
             -1.84889275e-32+0.00000000e+00j],
            dims=(2, 2, 2))
'''

