import matplotlib.pyplot as plt
from numpy import *

def main():
    real1 = int(input('please input first real number: '))
    imag1 = int(input('please input first imaginary number: '))
    real2 = int(input('please input second real number: '))
    imag2 = int(input('please input second imaginary number: '))
    a = complex(real1, imag1)
    b = complex(real2, imag2)

    print(f'first complex number: ${a}')
    print(f'second complex number: ${b}')
    print(f'add: ${a + b}')
    print(f'subtract: ${a + b}')
    print(f'multiply: ${a * b}')
    print(f'divide ${a / b}')
    
    x1, y1 = [0, real(a)], [0, imag(a)]
    # x2, y2 = [real(a), real]
    plt.plot(x1, y1, 'r')
    plt.show()

if __name__ == "__main__":
    main()