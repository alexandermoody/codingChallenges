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
    lines_array = np.array(lines) #make list of lines into array for easier indexing
    (n,m,w) = lines_array.shape
    sets = [] #initialize sets parameter
    length_lines_array = n #initialize mutable parameter to keep track of array size as it changes
    for l in range(n):
        if lines_array.size == 0:
            break
        ref_vector = lines_array[0,1,:] - lines_array[0,0,:] #first line in array as vector
        temp_sets = np.array([lines_array[0]]) #initialize temporary arrays
        temp_lines = lines_array.copy()
        temp_lines = np.delete(temp_lines, 0, axis=0)
        d = 1 #parameter to keep track of deleted lines
        for x in range(1,length_lines_array):
            vector1 = lines_array[x,0,:]-lines_array[0,0,:] #compute vectors to each new point
            vector2 = lines_array[x,1,:]-lines_array[0,0,:]
            vector1_check = np.cross(vector1,ref_vector) 
            vector2_check = np.cross(vector2,ref_vector)
            if vector1_check==0 and vector2_check==0: #check if colinear with cross product
                temp_lines = np.delete(temp_lines, x-d, axis = 0)
                d += 1
                temp_sets = np.concatenate((temp_sets,[lines_array[x]]), axis=0)
                # print('matching slope', lines_array[0], lines_array[x])
        sets.append(temp_sets) #add new set of colinear lines to sets list
        lines_array = temp_lines #reassign lines_array
        (n,m,w) = lines_array.shape
        length_lines_array = n #new length
    return sets #return sets as list of arrays

        


def visualize(sets):
    """
    Inputs: sets - sets of colinear lines
    This function creates a visualization that allows individual sets of colinear lines to be observed. When there are many sets of colinear lines, observing them all at once does not allow for each set to be seen clearly. Therefore, everytime the "Visualize Next Set" button is pressed, the subsequent set of colinear lines will be plotted in a new window. The "Done" button simply exits out of the program. 
    """
    window = tk.Tk()
    window.title('Colinear Challenge Visualization')
    window.counter = 0
    button = tk.Button(window, text = "Visualize Next Set", width=20, height = 2, command = lambda: plotLines(sets, window))
    button.pack()
    button2 = tk.Button(window, text = "Done", width=10, height = 2, command = exit)
    button2.pack()
    window.mainloop()


def plotLines(sets, root):
    """
    Inputs: sets - sets of colinear lines
            root - root of main visualization window
    This function plots a single set of colinear lines in a new Tkinter window.
    """
    if root.counter < len(sets):
        f = Figure(figsize=(5,5), dpi=100)
        a = f.add_subplot(111)
        for l in range(len(sets[root.counter])):
            a.plot(sets[root.counter][l,:,0],sets[root.counter][l,:,1], marker="*")

        newWindow = tk.Tk()
        newWindow.geometry("500x500")
        newWindow.title('Set Number '+str(root.counter+1))

        w = tk.Label(newWindow, text=str(len(sets[root.counter]))+" Line(s) in Set")
        w.pack()

        canvas = FigureCanvasTkAgg(f, master=newWindow)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        toolbar = NavigationToolbar2Tk(canvas, newWindow)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        root.counter+=1

        newWindow.mainloop()





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
    fill(lines, 10)
    # lines = np.array(lines)
    lines = [[ [1,1], [2,2]],
     [ [-1,-1], [0,0]],
     [ [2,6], [3,7]],
     [ [0,0], [1,1]],
     [ [4,4], [5,5]],
     [ [-7,3], [7,-3]]]
    sets = collinear(lines)
    # print(sets)
    visualize(sets)

if __name__ == "__main__":
    main()
