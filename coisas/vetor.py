from math import sqrt
class Vetor:
    def __init__(self, x, y):
        self.x = x
        self.y = y
            
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vetor(x, y)

    def __abs__(self):
        soma = self.x**2+self.y**2
        return sqrt(soma)

    def __repr__(self):
        return f'({self.x},{self.y})'
