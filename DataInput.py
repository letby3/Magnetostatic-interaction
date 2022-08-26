
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
 
        """
        c = data[0]; d = 1
        D = 2; R = 3
        Ms[0] = 4; Ms[1] = 5; Ms[2] = 6
        niu = 7; H0 = 8
        He = 9; Pm = 10
        Is1 = 11;
        hCylinder = 12; dCylinder = 13
        """

        file.close()

    def data_return(self):
        return self.data
    
    def Ms_return(self):
        return self.Ms
