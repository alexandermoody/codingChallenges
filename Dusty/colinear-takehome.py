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

def visualize(sets):
    """
    Create a visualization that shows the sets of collinear lines
    """
    window = tk.Tk()
    window.title('Colinear Challenge Visualization')
    window.geometry("500x500")
    button = tk.Button(window, text = "Visualize", width=10, height = 2, command = lambda: plotLines(sets))
    button.pack()
    button2 = tk.Button(window, text = "Done", width=10, height = 2, command = exit)
    button2.pack()
    window.mainloop()

    # fig = Figure(figsize=(5,4),dpi=100)
def plotLines(sets):
    f = Figure(figsize=(5,5), dpi=100)
    a = f.add_subplot(111)
    for s in range(len(sets)):
        a.plot(sets[s][l])
    print('duck')
    print(sets)

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
    print(lines[0])
    print(np.shape(lines))
    sets = collinear(lines)
    visualize(sets)

if __name__ == "__main__":
    main()
