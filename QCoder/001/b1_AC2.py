from qiskit import QuantumCircuit, QuantumRegister
 
 
def solve() -> QuantumCircuit:
    qc = QuantumCircuit(2)
    # Write your code here:
    qc.cx(0, 1)
    return qc

######################################################
import matplotlib.pyplot as plt
from qiskit_aer import Aer

def visualization(qc):
    qc.draw('mpl')
    plt.show()

def state(qc):
    sim = Aer.get_backend('statevector_simulator')
    res = sim.run(qc).result()
    state = res.data()['statevector']
    print('state =', state)


def main():
    qc = solve()
    # visualization(qc)


if __name__ == '__main__':
    main()

# memo
# 0, 0 -> 0, 0   : 0, 0+0 = 0, 0 OK 
# 0, 1 -> 0, 1   : 0, 1+0 = 0, 1 OK 
# 1, 0 -> 1, 1   : 1, 0+1 = 1, 1 OK
# 1, 1 -> 1, 0   : 1, 1+1 = 1, 0 OK 




