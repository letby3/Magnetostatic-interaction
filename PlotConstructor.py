import matplotlib.pyplot as plt
import numpy as np

class PlotConstructor:
   def __init__(self):
       pass

   @staticmethod
   def draw_Plot(x, y, x1, y1):
       fig = plt.figure()          
       plt.plot(x, y, label = 'line', color = 'blue') 
       plt.plot(x1, y1, label = 'line', color = 'red')
       plt.vlines(122.12, -10, 100, linestyle = '-.')
       plt.ylim(0, 1)
       plt.grid(True)
       plt.show()
   
       


