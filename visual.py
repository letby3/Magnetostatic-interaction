from tkinter import *
from MainEquation import MainEquation
from DataInput import DataInput
from CalculationValues import CalculationValues
from PlotConstructor import PlotConstructor

class Window:
    def __init__(self, weight,height,title="Программа по расчёту",resizable=(False,False), icon= ("icon.ico") ):
        dataFile = DataInput()
        dataFile.file_parsing(dataFile.file_input("File.txt"))
        data = dataFile.data_return()
        Ms = dataFile.Ms_return()

        self.root=Tk()
        self.root.title(title)
        self.root.geometry(f"{weight}x{height}+400+100")
        self.root.resizable(resizable[0],resizable[1])
        if icon:
            self.root.iconbitmap("icon.ico")
        self.lbl = Label(self.root,text="c                 ", font=("Verdana", 14))
        self.lbl1 = Label(self.root, text="d                 ",font=("Verdana", 14))
        self.lbl2 = Label(self.root, text="D                 ",font=("Verdana", 14))
        self.lbl3 = Label(self.root, text="R                 ", font=("Verdana", 14))
        self.lbl4 = Label(self.root, text=chr(951)+"                 " ,font=("Verdana", 14)) #Здесь chr(951) это код для греческой ню
        self.lbl5 = Label(self.root, text="H0                 ",font=("Verdana", 14))
        self.lbl6 = Label(self.root, text="He                 ",font=("Verdana", 14))
        self.lbl7 = Label(self.root, text="Pm                 ",font=("Verdana", 14))
        self.lbl8 = Label(self.root, text="Is1                 ",font=("Verdana", 14))
        self.lbl9 = Label(self.root, text="Высота                 ",font=("Verdana", 14))
        self.lbl10 = Label(self.root, text="Диаметр                 ",font=("Verdana", 14))
        
        self.Ms = Ms
        self.c = DoubleVar()
        self.c.set(data[0])
        self.d = DoubleVar()
        self.d.set(data[1])
        self.D = DoubleVar()
        self.D.set(data[2])
        self.R = DoubleVar()
        self.R.set(data[3])
        self.niu = DoubleVar()
        self.niu.set(data[7])
        self.H0 = DoubleVar()
        self.H0.set(data[8])
        self.He = DoubleVar()
        self.He.set(data[9])
        self.Pm = DoubleVar()
        self.Pm.set(data[10])
        self.Is1 = DoubleVar()
        self.Is1.set(data[11])
        self.hCylinder = DoubleVar()
        self.hCylinder.set(data[12])
        self.dCylinder = DoubleVar()
        self.dCylinder.set(data[13])
        self.Ms = StringVar()
        self.Ms.set("1 9 501")
        self.ent = Entry(self.root,width=10, textvariable=self.c)
        self.ent1 = Entry(self.root, width=10, textvariable=self.d)
        self.ent2 = Entry(self.root, width=10, textvariable=self.D)
        self.ent3 = Entry(self.root, width=10, textvariable=self.R)
        self.ent4 = Entry(self.root, width=10, textvariable=self.niu)
        self.ent5 = Entry(self.root, width=10, textvariable=self.H0)
        self.ent6 = Entry(self.root, width=10, textvariable=self.He)
        self.ent7 = Entry(self.root, width=10, textvariable=self.Pm)
        self.ent8 = Entry(self.root, width=10, textvariable=self.Is1)
        self.ent9 = Entry(self.root, width=10, textvariable=self.hCylinder)
        self.ent10 = Entry(self.root, width=10, textvariable=self.dCylinder)
        self.ent11 = Entry(self.root, width=10, textvariable=self.Ms)

    numbers = []

    def running_solve(self, data, Ms):             
        print(data)
        print(type(Ms[0]))
        #Write data in array
        person = CalculationValues(float(data[0]), float(data[1]), float(data[2]),
                                   float(data[3]), float(data[4]), float(data[5]),
                                   Ms, float(data[6]), float(data[7]),
                                   float(data[9]), float(data[10]))         
       
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
                                person.Gamma2, 
                                person.Mr,
                                person.niu)        
        #Calculating Zeta-function
        Zeta = equa.calcus_Function_Zeta()
        Zeta_Exp = equa.calcus_Function_Zeta_Exp()
        
        #Create Mslist array to plotting a graph 
        MsList = [it for it in range(int(Ms[0]), int(Ms[2]), int(Ms[1]))]

        #print(len(Zeta))
        #print(len(MsList))

        #Plotting a graph
        PlotConstructor.draw_Plot(MsList, Zeta, MsList, Zeta_Exp)

    def run(self):
        self.draw_widgets()        
        self.root.mainloop()

    def fromStr_to_array(self, str):
        arr = str.split()        
        return arr

    def get_number(self,n):        
        n.insert(0,self.ent.get())
        n.insert(1, self.ent1.get())
        n.insert(2, self.ent2.get())
        n.insert(3, self.ent3.get())
        n.insert(4, self.ent4.get())
        n.insert(5, self.ent5.get())
        n.insert(6, self.ent6.get())
        n.insert(7, self.ent7.get())
        n.insert(8, self.ent8.get())
        n.insert(9, self.ent9.get())
        n.insert(10, self.ent10.get())
        n.insert(11, self.ent11.get())  
        arr = self.fromStr_to_array(n[11])
        self.running_solve(n, [int(arr[0]), int(arr[1]), int(arr[2])])
        #Running_Solve
        Ms = str.split(n[-1])
        print(str(Ms))

    def draw_widgets(self):
        self.lbl.grid(row=2, column=2, sticky=W)
        self.ent.grid(row=2, column=2)
        self.lbl1.grid(row=4, column=2, sticky=W)
        self.ent1.grid(row=4, column=2)
        self.lbl2.grid(row=6, column=2, sticky=W)
        self.ent2.grid(row=6, column=2)
        self.lbl3.grid(row=8, column=2, sticky=W)
        self.ent3.grid(row=8, column=2)
        self.lbl4.grid(row=10, column=2, sticky=W)
        self.ent4.grid(row=10, column=2)
        self.lbl5.grid(row=12, column=2, sticky=W)
        self.ent5.grid(row=12, column=2)
        self.lbl6.grid(row=14, column=2, sticky=W)
        self.ent6.grid(row=14, column=2)
        self.lbl7.grid(row=16, column=2, sticky=W)
        self.ent7.grid(row=16, column=2)
        self.lbl8.grid(row=18, column=2, sticky=W)
        self.ent8.grid(row=18, column=2)
        self.lbl9.grid(row=20, column=2, sticky=W)
        self.ent9.grid(row=20, column=2, padx=90)
        self.lbl10.grid(row=22, column=2, sticky=W)
        self.ent10.grid(row=22, column=2, padx=90)
        self.ent11.grid(row=18, column=2, sticky='E')
        solvebut = Button(self.root, 
                          text="Solve", 
                          command=lambda: self.get_number([]), 
                          width=7)
        solvebut.grid(row=20, column=2, sticky='E')




