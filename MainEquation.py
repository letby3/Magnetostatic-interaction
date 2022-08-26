import math
from MathBase import MathBase

class MainEquation:
    
    def __init__(self, Ms, x0, Gamma1, Gamma2, Mr, niu):
        self.Ms = Ms
        self.x0 = x0
        self.Gamma1 = Gamma1
        self.Gamma2 = Gamma2
        self.Zeta = []
        self.Zeta_Exp = []
        self.Mr = Mr
        self.niu = niu

    def calcus_Function_Zeta(self):     #Zeta function
        it = 0
        for it_Ms in range(int(self.Ms[0]), int(self.Ms[2]), int(self.Ms[1])):
            partOneZeta = math.erf(float(self.x0[it])/math.sqrt(2))
            partTwoZeta = (MathBase.Hermit(2, float(self.x0[it])) * float(self.Gamma1[it]) / 3 - 
                           MathBase.Hermit(3, float(self.x0[it])) * float(self.Gamma2[it]) / 12  - 
                           MathBase.Hermit(5, float(self.x0[it])) * (float(self.Gamma1[it])**2) / 36)
            self.Zeta.append((partOneZeta - (MathBase.dnorm(float(self.x0[it]), 0, 1) * partTwoZeta)) / 4)             
            it = it + 1
        return self.Zeta

    def calcus_Function_Zeta_Exp(self):
        it = 0
        for it_Ms in range(int(self.Ms[0]), int(self.Ms[2]), int(self.Ms[1])):           
            self.Zeta_Exp.append(self.Mr / (it_Ms * self.niu))             
            it = it + 1
        return self.Zeta_Exp
    