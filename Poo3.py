class cuadrado:
    def __init__(self,lado1):
        self.lado1 = lado1
        
        def get_lado1(self):
            return self.lado1
        def set_lado1(self):
            self.lado1 = lado1
    def ld (self):
        return f'el perimetro del cuadrado es : {self.lado1*4} y su area es  :{self.lado1*self.lado1}'
lado1=float(input('Digite el valor de un lado  '))

cuadra=cuadrado(lado1)
print(cuadra.ld())