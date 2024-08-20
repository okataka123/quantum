from qiskit import QuantumCircuit
 
 
def solve() -> QuantumCircuit:
    qc = QuantumCircuit(1)
    # Write your code here:
    qc.x(0)
    qc.z(0)
    qc.x(0)
 
    return qc


############################################################
from qiskit_aer import Aer
import matplotlib.pyplot as plt

def main():
    sim = Aer.get_backend('statevector_simulator')
    qc = solve()
    res = sim.run(qc).result()
    state = res.data()['statevector']
    print('state =', state)
    
def vis(qc):
    fig = qc.draw('mpl')
    plt.show()

if __name__ == '__main__':
    main()