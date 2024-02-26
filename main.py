# Creating calculator by using tkinter

import tkinter as tk
from tkinter import messagebox

#-----------------------------------command_functions-----------------------------------------
# function that adds digit to the entery
def add_digit(digit):   
    value = calc.get()
    if value[0] == '0' and len(value) == 1:
        value = value[1:]
    calc['state'] = tk.NORMAL   # swiching state from readonly to normal
    calc.delete(0, tk.END)
    calc.insert(0, value+digit)
    calc['state'] = 'readonly'   # and here swiching it again
    
# function that adds operation to entery
def add_operation(operation):
    value = calc.get()
    if value[-1] in '-+/*':   # 21-25 - algo that allowing to do a cool thing 
        value = value[:-1]
    elif '+' in value or '-' in value or '/' in value or '*' in value:
        calculate()
        value = calc.get()
    calc['state'] = tk.NORMAL
    calc.delete(0, tk.END)
    calc.insert(0, value+operation)
    calc['state'] = 'readonly'

# it is an = 
def calculate():
    calc['state'] = tk.NORMAL
    value = calc.get()
    calc.delete(0, tk.END)
    if value[-1] == '+':
        calc.insert(0, int(value[:-1]) + int(value[:-1]))
    elif value[-1] == '*':
        calc.insert(0, int(value[:-1]) * int(value[:-1]))
    calc.delete(0, tk.END   )
    try:
        calc.insert(0, eval(value))
    except (ZeroDivisionError):
        messagebox.showinfo('Attention!', "You can't divide by zero!!!")
        calc.insert(0, 0)
    calc['state'] = 'readonly'
    
# it is a command for 'C' button 
def clean():
    calc['state'] = tk.NORMAL
    calc.delete(0, tk.END)
    calc.insert(0, '0')
    calc['state'] = 'readonly'  

# this function allows adding...
def press_key(event):
    if event.char.isdigit():   # ...digit...
        add_digit(event.char)
    elif event.char in '+-/*':   # ...operation to the entery by using keyboard.
        add_operation(event.char)
    elif event.char == '\r':   # And allows to use '=' and 'C' buttons
        calculate()
    elif event.char == 'c':
        clean()
#-------------------------------------------------------------------------------------------
#------------------------------make_some_button_functions-----------------------------------
# :
def make_digit_button(digit):
    return tk.Button(text=digit, bd=4, font=('Arial', 13), command=lambda: add_digit(digit))

def make_operation_button(operation):
    return tk.Button(text=operation, bd=4, font=('Arial', 15), fg='red', 
                    command=lambda: add_operation(operation))

def make_calc_button(operation):
    return tk.Button(text=operation, bd=4, font=('Arial', 13), command=calculate)
#--------------------------------------------------------------------------------------------


win = tk.Tk()
win.geometry(f'240x270+100+200')
win['bg'] = '#27ffe7'
win.title('Calculator')

win.bind('<Key>', press_key)   # using the calculator from the keyboard

calc = tk.Entry(win, justify='right', font=('Arial', 15), width=15)
calc.insert(0, '0')
calc['state'] = 'readonly'
calc.grid(row=0, column=0, columnspan=4, sticky='we', padx=5)

# making digit buttons
make_digit_button('1').grid(row=1, column=0, sticky='wens', padx=5, pady=5)
make_digit_button('2').grid(row=1, column=1, sticky='wens', padx=5, pady=5)
make_digit_button('3').grid(row=1, column=2, sticky='wens', padx=5, pady=5)
make_digit_button('4').grid(row=2, column=0, sticky='wens', padx=5, pady=5)
make_digit_button('5').grid(row=2, column=1, sticky='wens', padx=5, pady=5)
make_digit_button('6').grid(row=2, column=2, sticky='wens', padx=5, pady=5)
make_digit_button('7').grid(row=3, column=0, sticky='wens', padx=5, pady=5)
make_digit_button('8').grid(row=3, column=1, sticky='wens', padx=5, pady=5)
make_digit_button('9').grid(row=3, column=2, sticky='wens', padx=5, pady=5)
make_digit_button('0').grid(row=4, column=0, sticky='wens', padx=5, pady=5)

# making operation buttons
make_operation_button('/').grid(row=1, column=3, sticky='wens', padx=5, pady=5)
make_operation_button('*').grid(row=2, column=3, sticky='wens', padx=5, pady=5)
make_operation_button('-').grid(row=3, column=3, sticky='wens', padx=5, pady=5)
make_operation_button('+').grid(row=4, column=3, sticky='wens', padx=5, pady=5)

# making 'C' and '=' buttons
tk.Button(text='C', bd=4, font=('Arial', 13), fg='red', command=clean).grid(row=4, column=1, sticky='wens', padx=5, pady=5)
make_calc_button('=').grid(row=4, column=2, sticky='wesn', padx=5, pady=5)

win.grid_columnconfigure(0, minsize=60)
win.grid_columnconfigure(1, minsize=60)
win.grid_columnconfigure(2, minsize=60)
win.grid_columnconfigure(3, minsize=60)


win.grid_rowconfigure(1, minsize=60)
win.grid_rowconfigure(2, minsize=60)
win.grid_rowconfigure(3, minsize=60)
win.grid_rowconfigure(4, minsize=60)


win.mainloop()