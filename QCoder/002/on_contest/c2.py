from qiskit import QuantumCircuit
import math
 
 
def solve(n: int, L: int) -> QuantumCircuit:
    qc = QuantumCircuit(n)
    # Write your code here:
    coeff = 1/math.sqrt(L)
    qc.initialize([coeff]*L + [0]*(2**n-L))
    return qc.decompose(reps=25)

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
