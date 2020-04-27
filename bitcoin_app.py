import matplotlib
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from matplotlib import style
import tkinter as tk
from tkinter import ttk
import urllib
import json
import pandas as pd
import numpy as np

matplotlib.use('TkAgg')
LARGE_FONT = ('Verdana', 12)
style.use('ggplot')

f = Figure(figsize=(5, 5), dpi=100)
a = f.add_subplot(111)


def animate(i):
    pullData = open('sampleData.txt', 'r').read()
    dataList = pullData.split('\n')
    xList = []
    yList = []
    for readline in dataList:
        if len(readline) > 1:
            x, y = readline.split(',')
            xList.append(int(x))
            yList.append(int(y))

    a.clear()
    a.plot(xList, yList)


class BitcoinTrading(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, 'crypto-pyoneer')
        container = tk.Frame(self)
        container.pack(side='top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        for F in (StartPage, PageOne, PageTwo, PageThree):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky='nsew')
            self.show_frame(StartPage)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Start Page', font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        button1 = ttk.Button(self, text='visit page 1', command=lambda: controller.show_frame(PageOne))
        button1.pack()
        button2 = ttk.Button(self, text='visit page 2', command=lambda: controller.show_frame(PageTwo))
        button2.pack()
        button3 = ttk.Button(self, text='Graph Page', command=lambda: controller.show_frame(PageThree))
        button3.pack()


class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text='Page One', font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        button1 = ttk.Button(self, text='back to home', command=lambda: controller.show_frame(StartPage))
        button1.pack()


class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Page Two', font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        button1 = ttk.Button(self, text='back to home', command=lambda: controller.show_frame(StartPage))
        button1.pack()


class PageThree(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text='Graph Page', font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        button1 = ttk.Button(self, text='back to home', command=lambda: controller.show_frame(StartPage))
        button1.pack()

        # matplotlib coding for page three graph =======================================
        canvas = FigureCanvasTkAgg(f, self)
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        # toolbar code for matplotlib ================================================
        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas.tkcanvas.pack(fill=tk.BOTH, side=tk.TOP, expand=True)


app = BitcoinTrading()
ani = animation.FuncAnimation(f, animate, interval=1000)
app.mainloop()
