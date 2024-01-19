from tkinter import *


app = Tk()
app.title("the geneus calculator")
screen = Entry(app, width=45, borderwidth=3)
screen.grid(row=0, column=0, ipadx=10, ipady=10,
            padx=10, pady=10, columnspan=4)


var_1 = 0
var_2 = 0
opration = 0


def backspace():
    screen.delete(first=screen.index(INSERT) - 1, last=screen.index(INSERT))


def clear():
    global var_1, var_2
    screen.delete(first=0, last=screen.index(INSERT))
    var_2 = 0
    var_1 = 0


def plus():
    global opration, var_1
    opration = 1
    var_1 = float(screen.get())
    screen.delete(0, END)


def div():
    global opration
    opration = 2
    global var_1
    var_1 = float(screen.get())
    screen.delete(0, END)


def mul():
    global opration
    opration = 3
    global var_1
    var_1 = float(screen.get())
    screen.delete(0, END)


def minus():
    global opration
    opration = 4
    global var_1
    var_1 = float(screen.get())
    screen.delete(0, END)


def equal():
    global var_2, var_1, opration
    var_2 = float(screen.get())
    screen.delete(0, END)
    match opration:
        case 1:
            screen.insert(0, var_1 + var_2)
            opration = 0
        case 2:
            try:
                screen.insert(0, var_1 / var_2)
                opration = 0
            except ZeroDivisionError:
                screen.insert(0, "INVALID OPERATION")
        case 3:
            screen.insert(0, var_1 * var_2)
            opration = 0
        case 4:
            screen.insert(0, var_1 - var_2)
            opration = 0
    var_2 = 0
    var_1 = 0


def click(nbr):
    screen.insert(screen.index(END), nbr)


bt7 = Button(app, text=7, padx=30, pady=7, command=lambda: click("7"))
bt8 = Button(app, text=8, padx=30, pady=7, command=lambda: click("8"))
bt9 = Button(app, text=9, padx=30, pady=7, command=lambda: click("9"))
bt_del = Button(app, text="\u2190", padx=30, pady=7,
                command=backspace, bg="#bbbbbb")
bt4 = Button(app, text=4, padx=30, pady=7, command=lambda: click("4"))
bt5 = Button(app, text=5, padx=30, pady=7, command=lambda: click("5"))
bt6 = Button(app, text=6, padx=30, pady=7, command=lambda: click("6"))
bt_mul = Button(app, text="x", padx=30, pady=7,
                command=mul, bg="#bbbbbb")
bt1 = Button(app, text=1, padx=30, pady=7, command=lambda: click("1"))
bt2 = Button(app, text=2, padx=30, pady=7, command=lambda: click("2"))
bt3 = Button(app, text=3, padx=30, pady=7, command=lambda: click("3"))
bt_plus = Button(app, text="+", padx=30, pady=7,
                 command=plus, bg="#bbbbbb")
bt7_clear = Button(app, text="C", padx=30, pady=7, bg="#bde1e8", command=clear)
bt0 = Button(app, text=0, padx=30, pady=7, command=lambda: click("0"))
bt_point = Button(app, text=".", padx=30, pady=7, command=lambda: click("."))
bt7_mimus = Button(app, text="-", padx=30, pady=7,
                   command=minus, bg="#bbbbbb")
bt7_equ = Button(app, text="=", padx=30, pady=7,
                 command=equal, bg="#bbbbbb")
bt7_div = Button(app, text="/", padx=30, pady=7,
                 command=div, bg="#bbbbbb")


bt7.grid(row=1, column=0, pady=3)
bt8.grid(row=1, column=1, pady=3)
bt9.grid(row=1, column=2, pady=3)
bt_del.grid(row=1, column=3, pady=3)
bt4.grid(row=2, column=0, pady=3)
bt5.grid(row=2, column=1, pady=3)
bt6.grid(row=2, column=2, pady=3)
bt_mul.grid(row=2, column=3, pady=3)
bt1.grid(row=3, column=0, pady=3)
bt2.grid(row=3, column=1, pady=3)
bt3.grid(row=3, column=2, pady=3)
bt_plus.grid(row=4, column=3)
bt7_clear.grid(
    row=4, rowspan=2, pady=3, sticky="ns")
bt0.grid(row=4, column=1, pady=3,)
bt_point.grid(row=4, column=2, pady=3)
bt7_mimus.grid(row=5, column=3, pady=3)
bt7_equ.grid(row=5, column=1, pady=3, columnspan=2, sticky="we")
bt7_div.grid(row=3, column=3, pady=3)
app.mainloop()
