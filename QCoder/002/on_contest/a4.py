from qiskit import QuantumCircuit
 
 
def solve(n: int) -> QuantumCircuit:
    qc = QuantumCircuit(n)
    # Write your code here:

    if n == 1:
        qc.x(0)
        qc.h(0)
        return qc

    qc.h(0)

    step = 1
    while step < n:
        for i in range(0, n, 2*step):
            if i + step < n:
                print(f'i = {i}, i + step = {i+step}')
                qc.cx(i, i + step)
        step *= 2

    return qc



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

