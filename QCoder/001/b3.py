from qiskit import QuantumCircuit
from qiskit.circuit.library import ZGate


def solve(n: int, L: int) -> QuantumCircuit:
    qc = QuantumCircuit(n)
    # Write your code here:

    if n == 1:
        for l in range(L):
            if l & 1 == 0:
                qc.x(0)
            qc.z(0)
            if l & 1 == 0:
                qc.x(0)
        return qc

    for l in range(L):
        for i in range(n):
            if (l >> i) & 1 == 0:
                qc.x(i)
        qc.append(ZGate().control(n-1), range(n))
        for i in range(n):
            if (l >> i) & 1 == 0:
                qc.x(i)

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

