from tkinter import *

own = Tk()
own.geometry("356x460")
own.title('CALCULATOR')
own_label = Label(own, text='CALCULATOR', bg='Grey', font=("Times", 30, 'bold'))
own_label.pack(side=TOP)
own.config(background='Dark gray')

textin = StringVar()
operator = ""

def clickbut(number):
    global operator
    operator = operator + str(number)
    textin.set(operator)

def equlbut():
    global operator
    add = str(eval(operator))
    textin.set(add)
    operator = ''

def equlbut():
    global operator
    sub = str(eval(operator))
    textin.set(sub)
    operator = ''

def equlbut():
    global operator
    mul = str(eval(operator))
    textin.set(mul)
    operator = ''

def equlbut():
    global operator
    div = str(eval(operator))
    textin.set(div)
    operator = ''

def clrbut():
    textin.set('')

