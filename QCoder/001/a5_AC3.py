from qiskit import QuantumCircuit
import math


def solve() -> QuantumCircuit:
    qc = QuantumCircuit(2)
    # Write your code here:

    coeff = 1 / math.sqrt(3)
    qc.initialize([coeff, coeff, coeff, 0])
    #qc.initialize([coeff, coeff, coeff, 0], [0, 1]) # コレでもOK

    #return qc # UGEとなってしまう。(qc.initialize()で作った回路は非常に深い回路になる可能性がある。)
    return qc.decompose(reps=5)

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
