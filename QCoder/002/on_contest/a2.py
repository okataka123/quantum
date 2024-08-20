from qiskit import QuantumCircuit
 
 
def solve() -> QuantumCircuit:
    qc = QuantumCircuit(2)
    # Write your code here:
 
    qc.h(0)
    qc.cx(0, 1)
    qc.cz(0, 1)
    return qc

############################################################
from qiskit_aer import Aer
import matplotlib.pyplot as plt

def main():
    qc = solve()

    sim = Aer.get_backend('statevector_simulator')
    res = sim.run(qc).result()
    state = res.data()['statevector']
    print('state =', state)
    
def vis(qc):
    fig = qc.draw('mpl')
    plt.show()

if __name__ == '__main__':
    main()
