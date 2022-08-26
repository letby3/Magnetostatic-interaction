import math

class CalculationValues:

    def __init__(self, c, d, D, R, niu, H0, Ms, He, Pm, hCylinder, dCylinder):          #Constructor
        self.niu = niu
        self.R = R        
        self.D = D
        self.d = d
        self.H0 = H0
        self.He = He   
        self.Ms = Ms
        self.Pm = Pm
        self.c = c
        self.hCylinder = hCylinder
        self.dCylinder = dCylinder
        self.Hm = []
        self.Sg = []
        self.Miu3 = []
        self.Miu4 = []
        self.x0 = []
        self.Gamma1 = []
        self.Gamma2 = []       
        self.Vs = D * math.pi * (R**2)        
        self.Mr = Pm / (c * self.Vs)
        #print (type(self.Ms[0]))
        
        
    def checker(self):                  #Check function
        print(self.Ms)
    
    def it_To_Ms(self, it):             #Conversion from it to Ms
        return it * float(*self.Ms[1]) + float(*self.Ms[0])

    def Ms_To_it(self, it_Ms):          #Conversion from Ms to it
        return (it_Ms - float(*self.Ms[0])) / float(*self.Ms[1])

    def ksi(self, it_Ms):               #Ksi function
        return self.Pm / (self.c * self.Vs * it_Ms * self.niu)

    def calcus_Hm(self):                #Hm calculation function
        partOneHm = (4.0 * math.pi / 3.0) * self.niu        
        parTwoHm = (1 - (3 / 2) / math.sqrt(1 + (4 * self.R * self.R / (self.D * self.D))))
        it = 0        
        for it_Ms in range(int(self.Ms[0]), int(self.Ms[2]), int(self.Ms[1])):                          
             self.Hm.append(partOneHm * parTwoHm * it_Ms * self.ksi(it_Ms)) 
             it = it + 1        
        return self.Hm
        
    
    def calcus_Sigma(self):              #Sigma calculation function
       partOneSg = (((4.0 * math.pi / 3.0)**2) * self.niu / 10.0)
       partTwoSg = (1.0 - 45.0 * ((self.d/self.D)**3) / 32.0)
       it = 0
       for it_Ms in range(int(self.Ms[0]), int(self.Ms[2]), int(self.Ms[1])):
           self.Sg.append(math.sqrt(partOneSg * partTwoSg) * float(it_Ms))           
           it = it + 1
       return self.Sg

    def calcus_Miu3(self):              #Miu3 calculation function
        partOneMiu3 = ((4 * math.pi / 3)**3) * self.niu / 280
        partTwoMiu3 = 1 + 10*((self.d/self.D)**6)
        it = 0
        for it_Ms in range(int(self.Ms[0]), int(self.Ms[2]), int(self.Ms[1])):
            self.Miu3.append(partOneMiu3 * partTwoMiu3 * (it_Ms**3) * self.ksi(it_Ms))
            it = it + 1
        return self.Miu3
    
    def calcus_Miu4(self):              #Miu4 calculation function
        partOneMiu4 = ((4 * math.pi / 3)**4) * self.niu / 1120.0
        partTwoMiu4 = (1.0 - 20.0 * ((self.d/self.D)**9))
        it = 0
        for it_Ms in range(int(self.Ms[0]), int(self.Ms[2]), int(self.Ms[1])):
            self.Miu4.append(partOneMiu4 * partTwoMiu4 * (it_Ms**4))
            it = it + 1 
        return self.Miu4

    def calcus_x0(self):                #x0 calculation function
        it = 0
        for it_Ms in range(int(self.Ms[0]), int(self.Ms[2]), int(self.Ms[1])):
            self.x0.append((self.H0 + self.He + self.Hm[it]) / self.Sg[it])            
            it = it + 1
        return self.x0
    
    def calcus_Gamma1(self):            #Gamma1 calculation function
        it = 0
        for it_Ms in range(int(self.Ms[0]), int(self.Ms[2]), int(self.Ms[1])):
            self.Gamma1.append(self.Miu3[it] / (self.Sg[it]**3))
            it = it + 1
        return self.Gamma1
    
    def calcus_Gamma2(self):            #Gamma2 calculation function
        it = 0
        for it_Ms in range(int(self.Ms[0]), int(self.Ms[2]), int(self.Ms[1])):
            self.Gamma2.append(self.Miu4[it] / (self.Sg[it]**4) - 3)
            it = it + 1
        return self.Gamma2

