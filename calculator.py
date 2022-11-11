import operator
import tkinter
from tkinter import *

calculator_window = tkinter.Tk()
calculator_window.geometry('250x190+500+250')
calculator_window.title('Calculator')
calculator_window.resizable(False, False)

entry_label = tkinter.Entry(calculator_window, width=25)
entry_label.grid(row=0, column=0, columnspan=4)


# calculator_window['pady'] = 5

def c_butt():
    entry_label.delete(0, 'end')


def symbols(x):
    return lambda: entry_label.insert('end', x)


def add_entry(p):
    return lambda: entry_label.insert('end', p)


def equals():
    eq = eval(entry_label.get())
    eq = str(eq)
    entry_label.delete(0, 'end')
    entry_label.insert(0, eq)


c_button = tkinter.Button(calculator_window, text='C', command=c_butt)
c_button.grid(row=1, column=0, sticky='nwes')
ce_button = tkinter.Button(calculator_window, text='CE')
ce_button.grid(row=1, column=1, sticky='nwes')
tkinter.Button(calculator_window, text='0', command=lambda: entry_label.insert('end', '0')) \
    .grid(row=5, column=0, sticky='nwes')
tkinter.Button(calculator_window, text='=', command=equals).grid(row=5, column=1, columnspan=2, sticky='news')

x = 0
y = 4
for i in range(1, 10):
    tkinter.Button(calculator_window, text=i, command=add_entry(i)).grid(row=y, column=x, sticky='nwse')
    x += 1
    if x == 3:
        y -= 1
        x = 0

symbol_list = ['*', '-', '/', '+']
c = 2

for s in symbol_list:
    tkinter.Button(calculator_window, text=s, command=symbols(s)).grid(row=c, column=3, sticky='nwse')
    c += 1

calculator_window.mainloop()
