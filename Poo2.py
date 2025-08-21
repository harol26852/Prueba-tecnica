class Triangulo:
    def __init__(self,lado1,lado2,lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3  
        
        def get_lado1(self):
            return self.lado1
    
        def set_lado1(self):
            self.lado1 = lado1 
        
        def get_lado2(self):
            return self.lado2
        
        def set_lado2(self):
            self.lado2 = lado2
        
        def get_lado3(self):
            return self.lado3
    
        def set_lado3(self):
            self.lado3 = lado3
            
    def intp(self):
        self.lado1 = float(input('Digite el valor del lado 1 :   '))
        self.lado2 = float(input('Digite el valor del lado 2 :   '))
        self.lado3 = float(input('Digite el valor del lado 3 :   '))
        
    def Lado_m(self):
        if self.lado1 > self.lado2 and self.lado1 > self.lado3:
            return 'el lado 1 es el mayor'
        elif self.lado2 > self.lado1 and self.lado2 > self.lado3:
            return 'el lado 2 es el mayor'
        elif self.lado3 > self.lado1 and self.lado3 > self.lado2:
            return 'el lado 3 es el mayor  '
        else:
            print('todos los lados son iguales ')
    def tipo(self):
        if self.lado1 == self.lado2 == self.lado3:
            return 'El triangulo es equilatero'
        else:
            print('El triangulo no es quilater')
lado1=float
lado2=float
lado3=float

tria = Triangulo(lado1,lado2,lado3)
tria.intp()
print(tria.Lado_m())
print(tria.tipo())