class Aprendiz:
    def __init__(self,nombre,nota):
        self.nombre = nombre
        self.nota = nota
        
        def get_nombre(self):
            return self.nombre
    
        def set_nombre(self):
            self.nombre = nombre 
        
        def get_nota(self):
            return self.nota
        
        def set_nota(self):
            self.nota = nota
            
    def estudiante(self):
        self.nombre = input('Digite su nombre   :')
        self.nota = float(input('Digite su nota '))
    
    def aprob(self):
        if self.nota <= 5 :
            return 'No aprobo'
        else:
            print('Aprobo')
nombre=str
nota=float
Sta=Aprendiz(nombre,nota)
Sta.estudiante()
Sta.aprob()