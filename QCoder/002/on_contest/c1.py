from qiskit import QuantumCircuit


def solve(n: int, L: int) -> QuantumCircuit:
    qc = QuantumCircuit(n)
    # Write your code here:

    if L == 1:
        return qc

    th = 0
    while True:
        if 2**th >= L:
            break
        else:
            th += 1
    
    qc.h(range(th))
    return qc

############################################################
from qiskit_aer import Aer
import matplotlib.pyplot as plt

def main():
    sim = Aer.get_backend('statevector_simulator')
    qc = solve(3, 3)
    res = sim.run(qc).result()
    state = res.data()['statevector']
    print('state =', state)
    
def vis(qc):
    fig = qc.draw('mpl')
    plt.show()

if __name__ == '__main__':
    main()
