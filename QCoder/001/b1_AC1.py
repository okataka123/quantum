from qiskit import QuantumCircuit, QuantumRegister
 
 
def solve() -> QuantumCircuit:
    x, y = QuantumRegister(1), QuantumRegister(1)
    qc = QuantumCircuit(x, y)
    # Write your code here:
    qc.cx(x, y)
 
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
    coeff = 1/math.sqrt(2)
    qc.initialize([coeff, coeff, 0, 0])
    #qc.initialize([0, 0, 0, 1]) # |11>
    return qc

def make_oracle():
    qc = solve()
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

# memo
# 0, 0 -> 0, 0   : 0, 0+0 = 0, 0 OK 
# 0, 1 -> 0, 1   : 0, 1+0 = 0, 1 OK 
# 1, 0 -> 1, 1   : 1, 0+1 = 1, 1 OK
# 1, 1 -> 1, 0   : 1, 1+1 = 1, 0 OK 