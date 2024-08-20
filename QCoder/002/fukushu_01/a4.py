from qiskit import QuantumCircuit
 
 
def solve(n: int) -> QuantumCircuit:
    qc = QuantumCircuit(n)
    # Write your code here:

    if n == 1:
        qc.x(0)
        qc.h(0)
        return qc

    qc.h(0)
    for i in range(n-1):
        if i % 2 == 0:
            qc.cx(0, i+1)
        else:
            qc.cx(1, i+1)
    qc.cz(0,1)
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
