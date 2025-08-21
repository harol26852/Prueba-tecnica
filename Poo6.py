class venta:
    def __init__(self, codi,cant,precio):
        self.codi=codi
        self.cant=cant
        self.precio=precio

        def get_cod(self):
            return self.codi
        
        def set_cod(self):
            self.codi=codi

        def get_cant(self):
            return self.cant
        
        def set_cant(self):
            self.cant=cant

        def get_precio(self):
            return self.precio
        
        def set_precio(self):
            self.precio=precio

    def imp(self):
        return f"codigo:{self.codi}\ncantidad:{self.cant}\nprecio:{self.precio}"

codi=int(input("digite el codigo del producto: "))
cant=int(input("digite la cantidad del producto: "))
precio=float(input("digite el precio del producto: "))

ven=venta(codi,cant,precio)
print(ven.imp())