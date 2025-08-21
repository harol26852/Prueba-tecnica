class automovil:
    def __init__(self, color, modelo, nllantas, npuertas,kmFh):
        self.color=color
        self.modelo=modelo
        self.nllantas=nllantas
        self.npuertas=npuertas
        self.kmFh=kmFh
        
        def get_color(self):
            return self.color
        def set_color(self):
            self.color=color
            
        def get_modelo(self):
            return self.modelo
        def set_modelo(self):
            self.modelo=modelo
            
        def get_nllantas(self):
            return self.nllantas
        def set_nllantas(self):
            self.nllantas=nllantas
        
        def get_npuertas(self):
            return self.npuertas
        def set_npuertas(self):
            self.npuertas=npuertas
        
        def get_kmFh(self):
            return self.kmFh
        def set_kmFh(self):
            self.kmFh=kmFh
            
        
    def encender(self):
        l=input('encender el auto? (Y/N): ')
        l=l.upper()
        if l == 'Y':
            return 'Y'
        else: return 'N'
        
    def acelerar(self):
        self.kmFh=self.kmFh+1
        return self.kmFh

    def frenar(self):
        if self.kmFh == 0:
            print ('El auto no se puede frenar porque no se esta moviendo. ')
        else: 
            self.kmFh=0
            return self.kmFh
        
    def entradas(self):
        self.color=input('Digite el color del auto: ')
        self.modelo=input('Digite el modelo del veiculo del auto: ')
        self.nllantas=int(input('Digite el numero de llantas del auto: '))
        self.npuertas=int(input('Digite el numero de puertas del auto: '))
        self.kmFh=int(input('Digite la velocidad a la que va el auto: '))
        
    def imp(self):
        print(f"el vehiculo \ncolor: {self.color}\nmodelo: {self.modelo}\nnumero de llantas: {self.nllantas}\nnumero de puertas: {self.npuertas}\nva a una velocidad de: {self.kmFh}")

color,modelo,nllantas,npuertas,kmFh=str,int,int,int,int

v1= automovil(color,modelo,nllantas,npuertas,kmFh)
v1.entradas()
v1.imp()
