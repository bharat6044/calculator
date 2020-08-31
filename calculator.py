from tkinter import *

root = Tk()
root.title("CALCULATOR")

e = Entry(root)
e.grid(row=0, column=0, padx=5, pady=10, columnspan=5)


def button_click(number):
    no = e.get()
    e.delete(0, END)
    e.insert(0, no + str(number))
    print(no)


def button_OnClear():
    e.delete(len(e.get()) - 1)


def button_OnPlus():
    global Add_first_number
    Add_first_number = e.get()
    global sign
    sign = "+"
    e.delete(0, END)


def button_OnEqual():
    second_number = e.get()
    e.delete(0, END)
    if sign == "+":
        e.insert(0, int(first_number) +  int(second_number))
    if sign == "*":
        e.insert(0, int(Mul_first_number) * int(second_number))
    if sign == "-":
        e.insert(0, int(Min_first_number) - int(second_number))
    if sign == "/":
        e.insert(0, int(Div_first_number) / int(second_number))



def button_OnMultiplication():
    global Mul_first_number
    Mul_first_number = e.get()
    global sign
    sign = "*"
    e.delete(0, END)


def button_OnMinus():
    global Min_first_number
    Min_first_number = e.get()
    global sign
    sign = "-"
    e.delete(0, END)



def button_OnDivide():
    global Div_first_number
    Div_first_number = e.get()
    global sign
    sign = "/"
    e.delete(0, END)


def button_OnPeriod():
    global first_number
    first_number = e.get()
    global sign
    sign = "."
    e.delete(0, END)


button_1 = Button(root, text="1", padx=20, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=20, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=20, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=20, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=20, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=20, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=20, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=20, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=20, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=50, pady=20, command=lambda: button_click(0))
button_clear = Button(root, text="clear", padx=40, pady=20, command=lambda: button_OnClear())
button_plus = Button(root, text="+", padx=20, pady=20, command=button_OnPlus)
button_equals = Button(root, text="=", padx=50, pady=20, command=button_OnEqual)
button_minus = Button(root, text="-", padx=20, pady=20, command=button_OnMinus)
button_multiplaction = Button(root, text="*", padx=20, pady=20, command=button_OnMultiplication)
button_divide = Button(root, text="/", padx=20, pady=20, command=button_OnDivide)
button_period = Button(root, text=".", padx=20, pady=20, command=lambda: button_OnPeriod())

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=1, columnspan=2)

button_clear.grid(row=5, column=0, columnspan=2)
button_plus.grid(row=1, column=4)
button_equals.grid(row=5, column=2, columnspan=3)

button_minus.grid(row="2", column="4")
button_multiplaction.grid(row="3", column="4")
button_divide.grid(row="4", column="4")
button_period.grid(row="4", column="0")

root.mainloop()
