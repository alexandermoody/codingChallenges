# Given a set of lines, find sets of lines contained in the original
# set that are collinear.

# Create a visualization that shows the result of your work in a way you
# see fit to make the viewer understand which lines are collinear and which are
# not

# Each line is given as a set of x/y coordinates that mark the two endpoints of
# this line. Assume this format:
# [[x1,y1][x2,y2]]

# Fill in the 'collinear' and 'visualize' methods below - and feel free to
# create more if neccessary. Return your work in a single .py file that should
# execute using python 3.6 or greater. If you need to use any libraries, please
# document which packages need to installed to run your code.

# Note: we use Tkinter for visualization, but feel free to use anthing else if
# it works well for you.

# Please do not spend more than 2 hours on this exercise.
import random
import numpy as np
import tkinter as tk
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure

def collinear(lines):
    """
    Given a set of lines, find sets of lines where all lines are collinear

    example:

    lines = [[ (1,1), (2,2)],
     [ (-1,-1), (0,0)],
     [ (2,6), (3,7)],
     [ (0,0), (1,1)],
     [ (4,4), (5,5)],
     [ (-7,3), (7,-3)]]

    should return 3 sets (in any order):

    set 1
     [[(1, 1), (2, 2)], [(-1, -1), (0, 0)], [(0, 0), (1, 1)], [(4, 4), (5, 5)]],
    set 2
     [[(2, 6), (3, 7)]],
    set 3
     [[(-7, 3), (7, -3)]]

    note that sets 2 and 3 only contain a single line
    """
    lines_array = np.array(lines)
    (n,m,w) = lines_array.shape
    sets = []
    length_lines_array = n
    for l in range(n):
        if lines_array.size == 0:
            break
        slope = (lines_array[0,1,1]-lines_array[0,0,1])/(lines_array[0,1,0]-lines_array[0,0,0])
        temp_sets = np.array([lines_array[0]])
        temp_lines = lines_array.copy()
        temp_lines = np.delete(temp_lines, 0, axis=0)
        d = 1
        for x in range(1,length_lines_array):
            try:
                point1_slope = (lines_array[x,0,1]-lines_array[0,0,1])/(lines_array[x,0,0]-lines_array[0,0,0])
            except ZeroDivisionError:
                point1_slope = slope
            try:
                point2_slope = (lines_array[x,1,1]-lines_array[0,0,1])/(lines_array[x,1,0]-lines_array[0,0,0])
            except ZeroDivisionError:
                point2_slope = slope
            print('slopes', slope, point1_slope, point2_slope)
            if slope == point1_slope and slope == point2_slope:
                temp_lines = np.delete(temp_lines, x-d, axis = 0)
                d += 1
                temp_sets = np.concatenate((temp_sets,[lines_array[x]]), axis=0)
                print('delete line')
        sets.append(temp_sets)
        print('tempsetsshape', temp_sets.shape)
        lines_array = temp_lines
        (n,m,w) = lines_array.shape
        length_lines_array = n
        # print(temp_lines)
    print('shapesets', len(sets))
    return sets

        


def visualize(sets):
    """
    Create a visualization that shows the sets of collinear lines
    """
    window = tk.Tk()
    window.title('Colinear Challenge Visualization')
    window.geometry("500x500")
    window.counter = 0
    f = Figure(figsize=(5,5), dpi=100)
    a = f.add_subplot(111)
    button = tk.Button(window, text = "Visualize Next Set", width=20, height = 2, command = lambda: plotLines(sets, window, f, a))
    button.pack()
    button2 = tk.Button(window, text = "Done", width=10, height = 2, command = exit)
    button2.pack()
    # f = Figure(figsize=(5,5), dpi=100)
    # canvas = FigureCanvasTkAgg(f, master=window)
    # canvas.draw()
    # canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
    # toolbar = NavigationToolbar2Tk(canvas, window)
    # toolbar.update()
    # canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    window.mainloop()

    # fig = Figure(figsize=(5,4),dpi=100)

def plotLines(sets, root,f,a):
    if root.counter < len(sets):
        print(root.counter)
        f.clear()
        a.clear()
        f = Figure(figsize=(5,5), dpi=100)
        a = f.add_subplot(111)
        for l in range(len(sets[root.counter])):
            a.plot(sets[root.counter][l,:,0],sets[root.counter][l,:,1], label = 'set number'+str(root.counter))
        a.legend()
        canvas = FigureCanvasTkAgg(f, master=root)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, root)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        root.counter+=1





def fill(lines, num=100):
     """
     Simple test function
     fill a lines array with 100 random lines.
     All lines have coordinates between 0 and 10 using round numbered coordinates
     to maximize the chances of producing colinear lines. Feel free to improve or
     change this
     """
     for i in range(num):
         x1, y1 = [random.randint(0, 10), random.randint(0, 10)]
         x2, y2 = [random.randint(0, 10), random.randint(0, 10)]

         line = [[x1, y1],
                 [x2, y2]]
         lines.append(line)

# ----------------------------------------------------------------------
def main():
    lines = []
    fill(lines, 100)
    lines = np.array(lines)
    sets = collinear(lines)
    # print(sets)
    visualize(sets)

if __name__ == "__main__":
    main()
