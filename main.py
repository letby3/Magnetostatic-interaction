"""
        self.c = IntVar()
        self.d = IntVar()
        self.D = IntVar()
        self.R = IntVar()
        self.niu = IntVar()
        self.H0 = IntVar()
        self.He = IntVar()
        self.Pm = IntVar()
        self.Is1 = IntVar()
        self.hCylinder = IntVar()
        self.dCylinder = IntVar()
        self.Ms = StringVar()
"""


"""
#Input data
dataFile = DataInput()
dataFile.file_parsing(dataFile.file_input("File.txt"))

data = dataFile.data_return()
Ms = dataFile.Ms_return()


#Write data in array
person = CalculationValues(*data[0], *data[1], *data[2],
                           *data[3], *data[7], *data[8],
                           Ms, *data[9], *data[10],
                           *data[12], *data[13])

#Calculating values
person.calcus_Hm()
person.calcus_Sigma()
person.calcus_Miu3()
person.calcus_Miu4()
person.calcus_x0()
person.calcus_Gamma1()
person.calcus_Gamma2()
equa = MainEquation(Ms, person.x0,
                        person.Gamma1, 
                        person.Gamma2)

#Calculating Zeta-function
Zeta = equa.calcus_Function_Zeta()

#Create Mslist array to plotting a graph 
MsList = [it for it in range(int(*Ms[0]), int(*Ms[2]), int(*Ms[1]))]

print(len(Zeta))
print(len(MsList))

#Plotting a graph
PlotConstructor.draw_Plot(MsList, Zeta)
"""

"""
import math

class DataInput:      

    def file_input(self, fileName):
        file = open(fileName, 'r')
        return file

    def file_parsing(self, file):   
        self.data = []
        self.Ms = []
        for line in file:
            self.data.append([float(x) for x in line.split()])    

        self.Ms = [self.data[4], self.data[5], self.data[6]]
 
        
        c = data[0]; d = 1
        D = 2; R = 3
        Ms[0] = 4; Ms[1] = 5; Ms[2] = 6
        niu = 7; H0 = 8
        He = 9; Pm = 10
        Is1 = 11;
        hCylinder = 12; dCylinder = 13
        

        file.close()

    def data_return(self):
        return self.data
    
    def Ms_return(self):
        return self.Ms

###################################################################################################################

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
        #print (self.Vs)
        
        
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
        for it_Ms in range(int(*self.Ms[0]), int(*self.Ms[2]), int(*self.Ms[1])):             
             self.Hm.append(partOneHm * parTwoHm * it_Ms * self.ksi(it_Ms)) 
             it = it + 1
        return self.Hm
        
    
    def calcus_Sigma(self):              #Sigma calculation function
       partOneSg = (((4.0 * math.pi / 3.0)**2) * self.niu / 10.0)
       partTwoSg = (1.0 - 45.0 * ((self.d/self.D)**3) / 32.0)
       it = 0
       for it_Ms in range(int(*self.Ms[0]), int(*self.Ms[2]), int(*self.Ms[1])):
           self.Sg.append(math.sqrt(partOneSg * partTwoSg) * float(it_Ms))           
           it = it + 1
       return self.Sg

    def calcus_Miu3(self):              #Miu3 calculation function
        partOneMiu3 = ((4 * math.pi / 3)**3) * self.niu / 280
        partTwoMiu3 = 1 + 10*((self.d/self.D)**6)
        it = 0
        for it_Ms in range(int(*self.Ms[0]), int(*self.Ms[2]), int(*self.Ms[1])):
            self.Miu3.append(partOneMiu3 * partTwoMiu3 * (it_Ms**3) * self.ksi(it_Ms))
            it = it + 1
        return self.Miu3
    
    def calcus_Miu4(self):              #Miu4 calculation function
        partOneMiu4 = ((4 * math.pi / 3)**4) * self.niu / 1120.0
        partTwoMiu4 = (1.0 - 20.0 * ((self.d/self.D)**9))
        it = 0
        for it_Ms in range(int(*self.Ms[0]), int(*self.Ms[2]), int(*self.Ms[1])):
            self.Miu4.append(partOneMiu4 * partTwoMiu4 * (it_Ms**4))
            it = it + 1 
        return self.Miu4

    def calcus_x0(self):                #x0 calculation function
        it = 0
        for it_Ms in range(int(*self.Ms[0]), int(*self.Ms[2]), int(*self.Ms[1])):
            self.x0.append((self.H0 + self.He + self.Hm[it]) / self.Sg[it])            
            it = it + 1
        return self.x0
    
    def calcus_Gamma1(self):            #Gamma1 calculation function
        it = 0
        for it_Ms in range(int(*self.Ms[0]), int(*self.Ms[2]), int(*self.Ms[1])):
            self.Gamma1.append(self.Miu3[it] / (self.Sg[it]**3))
            it = it + 1
        return self.Gamma1
    
    def calcus_Gamma2(self):            #Gamma2 calculation function
        it = 0
        for it_Ms in range(int(*self.Ms[0]), int(*self.Ms[2]), int(*self.Ms[1])):
            self.Gamma2.append(self.Miu4[it] / (self.Sg[it]**4) - 3)
            it = it + 1
        return self.Gamma2


#############################################################################################################

class MathBase:
    @staticmethod
    def Hermit(argN, argX):             #Hermite polynomials
        factN = math.factorial(argN)
        answerHermit = 0
        powUnum = 1
        for it in range(int(argN/2) + 1):
            if(it % 2 == 0):
                powUnum = 1
            else:
                powUnum = -1
            answerHermit = answerHermit + powUnum * factN * ((2 * argX)**(argN - 2 * it)) / (math.factorial(it) * math.factorial(argN - 2 * it))

        return answerHermit

    @staticmethod
    def dnorm(argX, argMiu, argSg):     #Normal distribution
        partOneDnorm = 1 /(argSg * math.sqrt(2 * math.pi))
        partTwoDnorm = (-1 * ((argX - argMiu)**2) / (2 * argSg))
        return partOneDnorm * math.exp(partTwoDnorm)

#############################################################################################################

class MainEquation:
    
    def __init__(self, Ms, x0, Gamma1, Gamma2):
        self.Ms = Ms
        self.x0 = x0
        self.Gamma1 = Gamma1
        self.Gamma2 = Gamma2
        self.Zeta = []

    def calcus_Function_Zeta(self):     #Zeta function
        it = 0
        for it_Ms in range(int(*self.Ms[0]), int(*self.Ms[2]), int(*self.Ms[1])):
            partOneZeta = math.erf(float(self.x0[it])/math.sqrt(2))
            partTwoZeta = (MathBase.Hermit(2, float(self.x0[it])) * float(self.Gamma1[it]) / 3 - 
                           MathBase.Hermit(3, float(self.x0[it])) * float(self.Gamma2[it]) / 12  - 
                           MathBase.Hermit(5, float(self.x0[it])) * (float(self.Gamma1[it])**2) / 36)
            self.Zeta.append((partOneZeta - (MathBase.dnorm(float(self.x0[it]), 0, 1) * partTwoZeta)) / 4)            
            it = it + 1
        return self.Zeta

#############################################################################################################

dataFile = DataInput()
dataFile.file_parsing(dataFile.file_input("File.txt"))

data = dataFile.data_return()
Ms = dataFile.Ms_return()



person = CalculationValues(*data[0], *data[1], *data[2],
                           *data[3], *data[7], *data[8],
                           Ms, *data[9], *data[10],
                           *data[12], *data[13])

person.calcus_Hm()
person.calcus_Sigma()
person.calcus_Miu3()
person.calcus_Miu4()
person.calcus_x0()
person.calcus_Gamma1()
person.calcus_Gamma2()
equa = MainEquation(Ms, person.x0,
                        person.Gamma1, 
                        person.Gamma2)
equa.calcus_Function_Zeta()
#print('giuowhgiuowephgw')
#print(person.x0)
#print()
#print (MathBase.Hermit(2, 204.052))
#print (MathBase.dnorm(1, 0, 1))
"""