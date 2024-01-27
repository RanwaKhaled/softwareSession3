"""Complex number tasks"""
import math


class Complex:
    """Class for complex numbers and their operations"""
    def __init__(self, real=0.00, imag=0.00):
        self.real = float(real)
        self.imag = float(imag)

    def __str__(self):
        if self.imag>=0:
            return f'{self.real}+{self.imag}i'
        if self.imag<0:
            return f'{self.real}{self.imag}i'

    def __add__(self, other):
        new_real = self.real + other.real
        new_imag = self.imag + other.imag
        return Complex(new_real, new_imag)
    def __sub__(self, other):
        new_real = self.real - other.real
        new_imag = self.imag - other.imag
        return Complex(new_real, new_imag)

    def __mul__(self, other):
        new_real= (self.real * other.real) - (self.imag * other.imag)
        new_imag= (self.real * other.imag) + (self.imag * other.real)
        return Complex(new_real, new_imag)

    def __truediv__(self, other):
        conjugate= Complex(other.real, other.imag * -1)
        complex1 = self*conjugate
        complex2 = other * conjugate
        new_real = round(complex1.real / complex2.real, 2)
        new_imag = round(complex1.imag / complex2.real, 2)
        return Complex(new_real, new_imag)

    def mod(self):
        """returns the modulus of the complex nbr"""
        return round(math.sqrt(self.real ** 2 + self.imag ** 2), 2)

#driver program
#taking the first number from the user
complex_nbr1 = input('input your first number: ')
complex_nbr1 = complex(complex_nbr1.replace('i', 'j'))
complex_nbr1 = Complex(complex_nbr1.real, complex_nbr1.imag)
#taking the second number from the user
complex_nbr2 = input('input your second number: ')
complex_nbr2 = complex(complex_nbr2.replace('i', 'j'))
complex_nbr2 = Complex(complex_nbr2.real, complex_nbr2.imag)
#performing the operation
print(complex_nbr1 + complex_nbr2)
print(complex_nbr1 - complex_nbr2)
print(complex_nbr1 * complex_nbr2)
print(complex_nbr1 / complex_nbr2)
print(complex_nbr1.mod())
print(complex_nbr2.mod())
