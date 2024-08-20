from qiskit import QuantumCircuit
import math


def solve() -> QuantumCircuit:
    qc = QuantumCircuit(2)
    # Write your code here:

    theta = math.atan(math.sqrt(2))
    qc.ry(2*theta, 0)
    qc.ch(0, 1)
    qc.cx(1, 0)

    return qc

############################################################
from qiskit_aer import Aer
import matplotlib.pyplot as plt

def main():
    # n = int(input())
    # qc = solve(n)
    qc = solve()
    # vis(qc)
    sim = Aer.get_backend('statevector_simulator')
    res = sim.run(qc).result()
    state = res.data()['statevector']
    print('state =', state)
    
def vis(qc):
    fig = qc.draw('mpl')
    plt.show()

if __name__ == '__main__':
    main()
