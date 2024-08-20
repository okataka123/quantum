from qiskit import QuantumCircuit
import math

def solve(n: int, L: int) -> QuantumCircuit:
    qc = QuantumCircuit(n)
    # Write your code here:
    
    left_coeff = math.sqrt(0.6/L)
    right_coeff = math.sqrt(0.4/(2**n-L))

    coeffs = [left_coeff]*L + [right_coeff]*(2**n-L)
    qc.initialize(coeffs, list(range(n)))
 
    return qc.decompose(reps=10)


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
