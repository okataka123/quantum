from qiskit import QuantumCircuit
from qiskit.circuit.library import QFT
 
 
def solve(n: int) -> QuantumCircuit:
    #qc = QuantumCircuit(n)
    # Write your code here:
    qc = QFT(n)
    return qc

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
    qc.initialize([0, 1, 0, 0])
    return qc

def make_oracle():
    n = int(input())
    qc = solve(n)
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
