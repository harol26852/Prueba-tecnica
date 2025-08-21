class Identificador:
    def __init__(self,nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
        def get_nombre(self):
            return self.nombre
    
        def set_nombre(self):
            self.nombre = nombre 
        
        def get_edad(self):
            return self.edad
    
        def set_edad(self):
            self.edad = edad
        
    def mayor(self):
        if self.edad < 18:
            print('Eres menor de edad intentelo despues')
        else:
            print('Eres mayor de edad')
persona = Identificador('alfonso', 17)
persona.mayor()