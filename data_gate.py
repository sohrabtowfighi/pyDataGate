# Title: pyDataGate
#
# Purpose: Given a CSV of numerical data, create a subset of the dataset using
# instructions supplied by the user, then provide easy plotting ability with the
# ability to switch variables of the plot.
#
# Note: The CSV must have, as its first row, the column names
#
# Author: Sohrab Towfighi
import csv
import numpy
import tkinter as Tk
import matplotlib
matplotlib.use('TkAgg')
from numpy import arange, sin, pi, zeros
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

class Application(object):    
    def __init__(self, abs_path_to_csv, var_names):
        self.check_vars(var_names)
        self._root = Tk.Tk()
        self._root.wm_title("pyDataGate")
        self._figure = Figure(figsize=(5,4), dpi=100)
        self._dataset = DataSet(abs_path)
        root = self._root
        f = self._figure
        canvas = FigureCanvasTkAgg(f, master=root)
        canvas.show()
        canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
    #    canvas.mpl_connect('key_press_event', self.on_key_event)
        arrays = []
        for a_var in var_names:            
            arrays.append(self._dataset.get_array_from_dicts(a_var))
        if len(var_names) == 2:
            ax = f.add_subplot(111)
            ax.scatter(arrays[0], arrays[1])
        if len(var_names) == 3:
            ax = f.add_subplot(111, projection='3d')
            ax.scatter(arrays[0], arrays[1], arrays[2], c=arrays[2])
        button = Tk.Button(master=root, text='Quit', command=self.quit)
        button.pack(side=Tk.BOTTOM)
    #def on_key_event(event):
    #    click_result= [event.button, event.x, event.y, event.xdata, event.ydata]
    #    #print('button=%d, x=%d, y=%d, xdata=%f, ydata=%f'%click_result)
    #    return click_result
    @staticmethod
    def check_vars(list_of_vars):
        length = len(list_of_vars)
        if length > 3 or length < 2:
            raise TypeError("len(list_of_vars) > 3 or < 2.")
    def quit(self):
        self._root.quit()
        self._root.destroy()
    
class Gate(object):
    def __init__(self, name_attribute_0, name_attribute_1, array_attribute_0,
                 array_attribute_1):
        self._name_attribute_0 = name_attribute_0
        self._name_attribute_1 = name_attribute_1
        self._array_attribute_0 = array_attribute_0
        self._array_attribute_1 = array_attribute_1

class DataSet(object):
    def __init__(self, abs_path_to_csv):
        self._path_csv = abs_path_to_csv
        self._list_of_points = list()
        self._headers = list()
        i = 0
        with open(self._path_csv) as csv_file:
            self._csv_reader = csv.DictReader(csv_file)
            for row in self._csv_reader:
                print(row)
                if i == 0:
                    self._headers = list(row.keys())
                    print(self._headers)
                self._list_of_points.append(row)
                print(self._headers)
                i += 1
    def get_array_from_dicts(self, name_variable):
        length_data = len(self._list_of_points)
        my_array = zeros(length_data)
        for i in range(1, length_data):
            my_array[i] = float(self._list_of_points[i][name_variable])        
        return my_array
    
if __name__ == '__main__':
    abs_path = '/home/sohrab/GitRepos/pyDataGate/new_data_for_Hadi(2).csv'
    myapp = Application(abs_path, ["We", "Fr", "COR"])
    Tk.mainloop()

