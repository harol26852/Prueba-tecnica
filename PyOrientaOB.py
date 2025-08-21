class Ex_op:
    def __init__(self, num1,num2):
        self.num1 = num1
        self.num2 = num2
    
        def get_num1(self):
            return self.num1
    
        def set_num1(self):
            self.num1 = num1 
        
        def get_num2(self):
            return self.num2
        
        def set_num2(self):
            self.num2 = num2
            
    def dat(self):
        while True:
            try:
                self.num1=float(input("digite el numero 1: "))
                self.num2=float(input("digite el numero 2: "))
                print(self.num1/self.num2)
                resp=input("desea hacer la operacion nuevamente? (Y/N): ")
                resp=resp.upper()
                if resp == "N":
                    break
            except Exception as e:
                print(f"hay un error en la operacion, {e}- digite un numero mayor a 0 \n debe digitar numero")
                resp=input("desea hacer la operacion nuevamente? (Y/N): ")
                resp=resp.upper()
                if resp == "N":
                    break

"""while True:
    try:
        num1=float(input("digite el numero 1: "))
        num2=float(input("digite el numero 2: "))
        ope= Ex_op(num1,num2)
        print(ope.dat())
        resp=input("desea hacer la operacion nuevamente? (Y/N): ")
        resp=resp.upper()
        if resp == "N":
            break
    except Exception as e:
        print(f"hay un error en la operacion, {e}- digite un numero mayor a 0 \n debe digitar numero")
        resp=input("desea hacer la operacion nuevamente? (Y/N): ")
        resp=resp.upper()
        if resp == "N":
            break"""

num1=float
num2=float
ope= Ex_op(num1,num2)
ope.dat()