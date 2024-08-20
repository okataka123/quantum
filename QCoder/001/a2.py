from qiskit import QuantumCircuit
 
 
def solve(n: int) -> QuantumCircuit:
    qc = QuantumCircuit(n)
    # Write your code here:
    for i in range(n):
        qc.h(i)
    return qc


############################################################
from qiskit_aer import Aer
import matplotlib.pyplot as plt

def main():
    n = int(input())
    qc = solve(n)

    sim = Aer.get_backend('statevector_simulator')
    res = sim.run(qc).result()
    state = res.data()['statevector']
    print('state =', state)
    
def vis(qc):
    fig = qc.draw('mpl')
    plt.show()

if __name__ == '__main__':
    main()
