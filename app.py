from tkinter import *
from tkinter import ttk

root = Tk()

root.title('Калькулятор')
root.geometry('375x500')

frame = Frame(root, bg='white')
frame.place(relwidth=1, relheight=1)

def btn(Text, posx, posy, Command):
    btn = Button(frame, text=Text, font=50, activebackground = 'lightgray', bd=0, command=Command)
    btn.place(height=50, width=80, x = posx, y = posy)

def OnePressed():
    entry.insert(END, '1')

def TwoPressed():
    entry.insert(END, '2')

def ThreePressed():
    entry.insert(END, '3')

def FourPressed():
    entry.insert(END, '4')

def FivePressed():
    entry.insert(END, '5')

def SixPressed():
    entry.insert(END, '6')

def SevenPressed():
    entry.insert(END, '7')

def EightPressed():
    entry.insert(END, '8')

def NinePressed():
    entry.insert(END, '9')

def ZeroPressed():
    entry.insert(END, '0')

def AddPressed():
    entry.insert(END, '+')

def SubstractPressed():
    entry.insert(END, '-')

def MultiplyPressed():
    entry.insert(END, '*')

def DividePressed():
    entry.insert(END, '÷')

def DelPressed():
    Str = entry.get()
    entry.delete(0, END)
    entry.insert(0, Str[:-1])

def ClearPressed():
    entry.delete(0,END)


def EqualPressed():
    Str = entry.get()
    parts = []
    nums = ""
    for i in Str:
        if i.isdigit():
            nums += i
        else:
            parts.append(int(nums))
            parts.append(i)
            nums = ""
    parts.append(int(nums))
    if parts[1] == '+':
        result = parts[0] + parts[2]
    elif parts[1] == '-':
        result = parts[0] - parts[2]
    elif parts[1] == '*':
        result = parts[0] * parts[2]
    elif parts[1] == '÷':
        result = parts[0] / parts[2]
    elif parts[1] == '%':
        result = parts[0] % parts[2]
    entry.delete(0,END)
    entry.insert(0,result)

def SquarePressed():
    Str = entry.get()
    nums = ""
    for i in Str:
        if i.isdigit():
            nums += i
        
    result = int(nums) * int(nums)
    entry.delete(0,END)
    entry.insert(0,result)

def PercentPressed():
    entry.insert(END, "%")

def SwitchSingPressed():
    Str = entry.get()
    parts = []
    for i in Str:
        parts.append(i)
    if parts[0] == '-':
        entry.delete(0)
    else:
        entry.insert(0, "-")

entry = ttk.Entry(justify=RIGHT, font=100)
entry.place(height=150, width=335, x = 20, y = 20)

btn('%',20,185,PercentPressed)

btn('x^2',105,185,SquarePressed)

btn('+/-',190,185,SwitchSingPressed)

btn('<==',275,185,DelPressed)

btn('1',20,240,OnePressed)

btn('2',105,240,TwoPressed)

btn('3',190,240,ThreePressed)

btn('+',275,240,AddPressed)

btn('4',20,295,FourPressed)

btn('5',105,295,FivePressed)

btn('6',190,295,SixPressed)

btn('-',275,295,SubstractPressed)

btn('7',20,350,SevenPressed)

btn('8',105,350,EightPressed)

btn('9',190,350,NinePressed)

btn('*',275,350,MultiplyPressed)

btn('C',20,405,ClearPressed)

btn('0',105,405,ZeroPressed)

btn('=',190,405,EqualPressed)

btn('÷',275,405,DividePressed)

root.mainloop()