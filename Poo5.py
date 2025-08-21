class calculadora:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
        
        def get_num2(self):
            return self.num2
        
        def set_num2(self):
            self.num2=num2
        
        def get_num1(self):
            return self.num1
        
        def set_num1(self):
            self.num1=num1
    
    def suma(self):
        return self.num1+self.num2
    
    def rest(self):
        return self.num1-self.num2
    
    def div (self):
        return self.num1/self.num2
    
    def multi (self):
        return self.num1*self.num2
    
    def imp(self):
        print(f"las operaciones entre {self.num1} y {self.num2} son: \n {self.num1}+{self.num2}={self.suma()} \n {self.num1}-{self.num2}={self.rest()} \n {self.num1}x{self.num2}={self.multi()} \n {self.num1}/{self.num2}={self.div()}")

num1=float(input("digite el primer numero: "))
num2=float(input("digite el segundo numero: "))

calcu=calculadora(num1,num2)
calcu.imp()