from tkinter import *
from tkinter import ttk
import random
from colors import *

# Importing algorithms 
from algorithms.bubbleSort import bubble_sort
from algorithms.selectionSort import selection_sort
from algorithms.insertionSort import insertion_sort
from algorithms.mergeSort import merge_sort
from algorithms.quickSort import quick_sort
from algorithms.heapSort import heap_sort
from algorithms.countingSort import counting_sort


# Main window 
window = Tk()
window.title("Sorting Algorithms Visualization")
window.maxsize(1000, 700)
window.config(bg = WHITE)


algorithm_name = StringVar()
speed_name = StringVar()
data = []
algo_list = ['Bubble Sort', 'Insertion Sort', 'Selection Sort', 'Merge Sort', 'Quick Sort', 'Heap Sort', 'Counting Sort']
speed_list = ['Fast', 'Medium', 'Slow']


# Drawing the numerical array as bars
def drawData(data, colorArray):
    canvas.delete("all")
    canvas_width = 800
    canvas_height = 400
    x_width = canvas_width / (len(data) + 1)
    offset = 4
    spacing = 2
    normalizedData = [i / max(data) for i in data]

    for i, height in enumerate(normalizedData):
        x0 = i * x_width + offset + spacing
        y0 = canvas_height - height * 390
        x1 = (i + 1) * x_width + offset
        y1 = canvas_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])

    window.update_idletasks()


# Randomly generate array
def generate():
    global data

    minVal = int(min_entry.get())
    maxVal = int(max_entry.get())
    size = int(size_entry.get())    

    data = []

    for _ in range(size):
        data.append(random.randrange(minVal, maxVal + 1))        

    drawData(data, [BLUE for x in range(len(data))])


def set_speed():
    if speed_menu.get() == 'Slow':
        return 0.3
    elif speed_menu.get() == 'Medium':
        return 0.1
    else:
        return 0.001

def stop():
    exit()

def sort():
    global data
    timeTick = set_speed()
    
    if algo_menu.get() == 'Bubble Sort':
        bubble_sort(data, drawData, timeTick)
    elif algo_menu.get() == 'Selection Sort':
        selection_sort(data, drawData, timeTick)
    elif algo_menu.get() == 'Insertion Sort':
        insertion_sort(data, drawData, timeTick)
    elif algo_menu.get() == 'Merge Sort':
        merge_sort(data, 0, len(data)-1, drawData, timeTick)
    elif algo_menu.get() == 'Quick Sort':
        quick_sort(data, 0, len(data)-1, drawData, timeTick)
    elif algo_menu.get() == 'Heap Sort':
        heap_sort(data, drawData, timeTick)
    else:
        counting_sort(data, drawData, timeTick)


### User interface ###
UI_frame = Frame(window, width= 900, height=300, bg=WHITE)
UI_frame.grid(row=0, column=0, padx=10, pady=5)

#Row[1]
l1 = Label(UI_frame, text="Algorithm: ", bg=WHITE)
l1.grid(row=0, column=0, padx=10, pady=5, sticky=W)
algo_menu = ttk.Combobox(UI_frame, textvariable=algorithm_name, values=algo_list)
algo_menu.grid(row=0, column=1, padx=5, pady=5)
algo_menu.current(0)

#Row[2]
size_entry = Scale(UI_frame, from_=3, to=25, resolution=1, orient=HORIZONTAL, label='Data Size', bg=WHITE)
size_entry.grid(row=1, column=0, padx=5, pady=5)

min_entry = Scale(UI_frame, from_=0, to=10, resolution=1, orient=HORIZONTAL, label='Min value', bg=WHITE)
min_entry.grid(row=1, column=1, padx=5, pady=5)

max_entry = Scale(UI_frame, from_=10, to=100, resolution=1, orient=HORIZONTAL, label='Max Value', bg=WHITE)
max_entry.grid(row=1, column=2, padx=5, pady=5)

#Row[3]
l2 = Label(UI_frame, text="Sorting Speed: ", bg=WHITE)
l2.grid(row=2, column=0, padx=10, pady=5, sticky=W)
speed_menu = ttk.Combobox(UI_frame, textvariable=speed_name, values=speed_list)
speed_menu.grid(row=2, column=1, padx=5, pady=5)
speed_menu.current(0)

canvas = Canvas(window, width=800, height=400, bg=WHITE)
canvas.grid(row=2, column=0, padx=10, pady=5)

#Row[4]
b1 = Button(UI_frame, text="Sort", command=sort, bg=YELLOW)
b1.grid(row=3, column=1, padx=5, pady=5)

b3 = Button(UI_frame, text="Generate Array", command=generate, bg=YELLOW)
b3.grid(row=3, column=0, padx=5, pady=5)

b4 = Button(UI_frame, text="Exit", command=stop, bg=YELLOW)
b4.grid(row=3, column=2, padx=5, pady=5)


window.mainloop()