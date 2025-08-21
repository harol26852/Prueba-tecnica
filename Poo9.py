class Nuficha:
    def __init__(self, Nficha, aprendices,edad,cedula):
        self.Nficha=Nficha
        self.aprendices=aprendices
        self.edad = edad 
        self.id = cedula
        
        def get_Nficha(self):
            return self.Nficha
        def set_Nficha(self):
            self.Nficha=Nficha
            
        def get_aprendices(self):
            return self.aprendices
        def set_aprendices(self):
            self.aprendices=aprendices
        
        def get_edad(self):
            return self.edad
        def set_edad(self):
            self.edad=edad
        
        def get_cedula(self):
            return self.cedula
        def set_cedula(self):
            self.cedula=cedula
        
    def info(self):
        self.Nficha=int(input('Escribir el numero de ficha: '))
        self.aprendices=input('Escriba su nombre: ')
        self.edad=int(input('Escribir su edad: '))
        self.cedula=int(input('Escribir su numero de cedula: '))
    def imp(self):
        return f"el nombre del aprendiz es {self.aprendices} \nPertenece a la ficha: {self.Nficha} \nSu edad es :{self.edad} \nSu numero de cecdula es :{self.cedula}"
    
Nficha,aprendices,edad,cedula=int,str,int,int


fi=Nuficha(Nficha, aprendices,edad,cedula)
fi.info()
print(fi.imp())