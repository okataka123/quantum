from qiskit import QuantumCircuit
 

def solve() -> QuantumCircuit:
    qc = QuantumCircuit(2)
    # Write your code here:
    qc.h(0) 
    qc.cx(0, 1)
    qc.h(0)

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
    qc = QuantumCircuit(1)
    #qc.initialize([1, 0]) # |0>
    #qc.initialize([0, 1]) # |1>
    qc.initialize([1/math.sqrt(2), 1/math.sqrt(2)])
    return qc

def make_oracle():
    qc = solve(1, 2)
    oracle_gate = qc.to_gate()
    oracle_gate.name = 'oracle'
    return oracle_gate
    
def main():
    #qc = solve()
    qc = create_input_qc()
    oracle_gate = make_oracle()
    qc.append(oracle_gate, [0])

    #visualization(qc)
    get_state(qc)

if __name__ == '__main__':
    main()

