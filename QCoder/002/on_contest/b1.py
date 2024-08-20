from qiskit import QuantumCircuit
 
 
def solve(theta: float) -> QuantumCircuit:
    qc = QuantumCircuit(1)
    # Write your code here:
    qc.rz(-2*theta, 0)
    return qc

######################################################
from qiskit_aer import Aer
import matplotlib.pyplot as plt

def main():
    n = float(input())
    qc = solve(n)
    #qc = solve()
    sim = Aer.get_backend('statevector_simulator')
    res = sim.run(qc).result()
    state = res.data()['statevector']
    print('state =', state)
    
def vis(qc):
    fig = qc.draw('mpl')
    plt.show()

if __name__ == '__main__':
    main()


