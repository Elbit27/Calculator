import tkinter as tk
from tkinter import messagebox

def add_digit(digit):
    value = calc.get()
    if value[0] == '0' and len(value) == 1:
        value = value[1:]
    calc['state'] = tk.NORMAL
    calc.delete(0, tk.END)
    calc.insert(0, value+digit)
    calc['state'] = 'readonly'
    

def add_operation(operation):
    value = calc.get()
    if value[-1] in '-+/*':
        value = value[:-1]
    elif '+' in value or '-' in value or '/' in value or '*' in value:
        calculate()
        value = calc.get()
    calc['state'] = tk.NORMAL
    calc.delete(0, tk.END)
    calc.insert(0, value+operation)
    calc['state'] = 'readonly'



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
    # except (NameError, SyntaxError):
    #     messagebox.showinfo('Attention!', 'You can only enter numbers!!!\nYou entered another symbols')
    #     calc.insert(0, 0)
    except (ZeroDivisionError):
        messagebox.showinfo('Attention!', "You can't divide by zero!!!")
        calc.insert(0, 0)
    calc['state'] = 'readonly'
    

def make_digit_button(digit):
    return tk.Button(text=digit, bd=4, font=('Arial', 13), command=lambda: add_digit(digit))

def make_operation_button(operation):
    return tk.Button(text=operation, bd=4, font=('Arial', 15), fg='red', 
                    command=lambda: add_operation(operation))

def clean():
    calc['state'] = tk.NORMAL
    calc.delete(0, tk.END)
    calc.insert(0, '0')
    calc['state'] = 'readonly'
    


def make_calc_button(operation):
    return tk.Button(text=operation, bd=4, font=('Arial', 13), command=calculate)


def press_key(event):
    if event.char.isdigit():
        add_digit(event.char)
    elif event.char in '+-/*':
        add_operation(event.char)
    elif event.char == '\r':
        calculate()
    elif event.char == 'c':
        clean()

win = tk.Tk()
win.geometry(f'240x270+100+200')
win['bg'] = '#27ffe7'
win.title('Calculator')

win.bind('<Key>', press_key)

calc = tk.Entry(win, justify='right', font=('Arial', 15), width=15)
calc.insert(0, '0')
calc['state'] = 'readonly'
calc.grid(row=0, column=0, columnspan=4, sticky='we', padx=5)

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

make_operation_button('/').grid(row=1, column=3, sticky='wens', padx=5, pady=5)
make_operation_button('*').grid(row=2, column=3, sticky='wens', padx=5, pady=5)
make_operation_button('-').grid(row=3, column=3, sticky='wens', padx=5, pady=5)
make_operation_button('+').grid(row=4, column=3, sticky='wens', padx=5, pady=5)

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