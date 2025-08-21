class FDSIM():
    def _init_(self,NMaprendices,Nsalon,ficha):
        self.NMaprendices=NMaprendices
        self.Nsalon=Nsalon
        self.ficha=ficha

        def get_NMaprendices(self):
            return self.NMaprendices
        def set_NMaprendices(self):
            self.NMaprendices=NMaprendices

        def get_Nsalon(self):
            return self.Nsalon
        def set_Nsalon(self):
            self.Nsalon=Nsalon
        
        def get_ficha(self):
            return self.ficha
        def set_ficha(self):
            self.ficha=ficha

    def inputs(self):
        
        ADSOD={4111:17,
        4103       :28,
        4109       :23,
        4108       :32
        }

        ADSID={4104:24,
        4102       :10,
        4110       :22
        }

        noned={4107:0
        }

        if self.ficha==1:
            self.NMaprendices= sum(ADSOD.values())
            self.Nsalon=len(ADSOD)
            return ADSOD
        elif self.ficha==2:
            self.NMaprendices= sum(ADSID.values())
            self.Nsalon=len(ADSID)
            return ADSID
        else:
            self.NMaprendices= sum(noned.values())
            self.Nsalon=len(noned) 
            return noned
    
    def imp(self):
        if self.ficha==1:
            print("los salones de ADSO y estudiantes son: ")
        elif self.ficha==2:
            print("los salones de ADSI y estudiantes son: ")
        else: print("el numero de salones vacios y sin estudiantes es: ")
        for i,j in (self.inputs()).items():
            print(f"salon:{i}-->{j} estudiantes")
        print(f"numero total de salones: {self.Nsalon}\nnumero total de estudiantes: {self.NMaprendices}")




        

class ADSO(FDSIM):
    def _init_(self, NMaprendices, Nsalon, ficha):
        super()._init_(NMaprendices, Nsalon, ficha)
    
    def indi(self):
        self.ficha=1

class ADSI(FDSIM):
    def _init_(self, NMaprendices, Nsalon, ficha):
        super()._init_(NMaprendices, Nsalon, ficha)
    
    def indi(self):
        self.ficha=2

class nonen(FDSIM):
    def _init_(self, NMaprendices, Nsalon, ficha):
        super()._init_(NMaprendices, Nsalon, ficha)
    
    def indi(self):
        self.ficha=3

adso=ADSO()
adso.indi()
adso.imp()

adsi=ADSI()
adsi.indi()
adsi.imp()

non=nonen()
non.indi()
non.imp()