from qiskit import QuantumCircuit
 
 
def solve(n: int) -> QuantumCircuit:
    qc = QuantumCircuit(n)
    # Write your code here:

    qc.h(0)

    i = 0
    while 2**i < n:
        for j in range(2**i):
            if j+2**i < n:
                qc.cx(j, j+2**i)
        i += 1
    qc.z(0)

    return qc
    
"""

"""


############################################################
from qiskit_aer import Aer
import matplotlib.pyplot as plt

def main():
    n = int(input())
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
