#### Michael Jarnling

# imports
import tkinter as tk 
import math

# present sum
def show_sum(x):
    ent_input.delete(0, tk.END)
    ent_input.insert(0, x)

# arithmetic functions
def calc_this(x,y,o):
    if o == "+":
        summa = float(x) + float(y)
    elif o == "-":
        summa = float(x) - float(y)
    elif o == "/":
        summa = float(x) / float(y)
    elif o == "*":
        summa = float(x) * float(y)
    elif o == "pow":
        summa = float(x) ** float(y)
    show_sum(summa)

def square_this(x):
    summa = math.sqrt(float(x))
    show_sum(summa)

def cos_this(x):
    summa = math.cos(float(x))
    show_sum(summa)

def sin_this(x):
    summa = math.sin(float(x))
    show_sum(summa)

def fact_this(x):
    summa = math.factorial(int(x)) # float is not supported
    show_sum(summa)

### window and frame
## window
window = tk.Tk()
## frames
frm_head = tk.Frame(master=window, width=30)
frm_input = tk.Frame(master=window, width=30)
frm_body = tk.Frame(master=window, width=30)
frm_calc = tk.Frame(master=window, width=30)
frm_bot = tk.Frame(master=window, width=30)
# pack em
frm_head.pack()
frm_input.pack()
frm_body.pack()
frm_calc.pack()
frm_bot.pack()

## labels
lbl_title = tk.Label(master=frm_head, text="Michaels Calculator", bg="black", fg="white", width=30)
lbl_error = tk.Label(master=frm_bot, text="", fg="red", width=30)
# pack em
lbl_title.pack()
lbl_error.pack()

## entry box
ent_input = tk.Entry(master=frm_input, width="30")
# pack em
ent_input.pack()

## buttons
btn_add = tk.Button(master=frm_body, text='+')
btn_sub = tk.Button(master=frm_body, text="-")
btn_multi = tk.Button(master=frm_body, text="*")
btn_div = tk.Button(master=frm_body, text="/")
btn_sqrt = tk.Button(master=frm_body, text="sqrt")
btn_pow = tk.Button(master=frm_body, text="pow")
btn_cos = tk.Button(master=frm_body, text="cos")
btn_sin = tk.Button(master=frm_body, text="sin")
btn_fact = tk.Button(master=frm_body, text="!")
btn_calc = tk.Button(master=frm_calc, text="CALCULATE", width="27") # fix border
# pack em
btn_add.pack(side=tk.LEFT)
btn_sub.pack(side=tk.LEFT)
btn_multi.pack(side=tk.LEFT)
btn_div.pack(side=tk.LEFT)
btn_sqrt.pack(side=tk.LEFT)
btn_pow.pack(side=tk.LEFT)
btn_cos.pack(side=tk.LEFT)
btn_sin.pack(side=tk.LEFT)
btn_fact.pack(side=tk.LEFT)
btn_calc.pack()

### interactive
## functions
def fnc_click(event):
    check=False # check default value
    lbl_error["text"] = "" # reset error label
    userinput = ent_input.get()
    if userinput == "quit":
        exit("Bye bye!")
    operators = ["+","-","/","*","pow","sqrt","cos","sin","!"]
    for op in operators:
        if op not in userinput:
            continue
        elif op in userinput:
            check=True # set true if we found the operator
            foo = userinput.split(op)
            if op in operators[0:5]:
                try: # check if there are any values
                    # send them to the function
                    calc_this(foo[0], foo[1], op)
                except: # if not, print error
                    lbl_error["text"] = "Error - Missing values"
            elif op == "sqrt":
                try: # check if there are any values
                    square_this(foo[0])
                except: # if not, print error
                    lbl_error["text"] = "Error - Missing a value"
            elif op == "cos":
                try: # check if there are any values
                    cos_this(foo[0])
                except: # if not, print error
                    lbl_error["text"] = "Error - Missing a value"
            elif op == "sin":
                try: # check if there are any values
                    sin_this(foo[0])
                except: # if not, print error
                    lbl_error["text"] = "Error - Missing a value"
            elif op == "!":
                try: # check if there are any values
                    fact_this(foo[0])
                except: # if not, print error
                    lbl_error["text"] = "Error - Missing a value"
    if not check: # if we didn't find the operator, print an error
        lbl_error["text"] = "Error - Missing operator"

# add operators to the entry box based on the button pressed
def add_click(event):
    ent_input.insert(tk.END, "+")

def sub_click(event):
    ent_input.insert(tk.END, "-")

def div_click(event):
    ent_input.insert(tk.END, "/")

def multi_click(event):
    ent_input.insert(tk.END, "*")

def sqrt_click(event):
    ent_input.insert(tk.END, "sqrt")

def pow_click(event):
    ent_input.insert(tk.END, "pow")

def cos_click(event):
    ent_input.insert(tk.END, "cos")

def sin_click(event):
    ent_input.insert(tk.END, "sin")

def fact_click(event):
    ent_input.insert(tk.END, "!")

## bind buttons
# Button-1 = left mouse click
# 2nd value is the function to pass this to
btn_calc.bind("<Button-1>", fnc_click)
btn_add.bind("<Button-1>", add_click)
btn_sub.bind("<Button-1>", sub_click)
btn_div.bind("<Button-1>", div_click)
btn_multi.bind("<Button-1>", multi_click)
btn_sqrt.bind("<Button-1>", sqrt_click)
btn_pow.bind("<Button-1>", pow_click)
btn_cos.bind("<Button-1>", cos_click)
btn_sin.bind("<Button-1>", sin_click)
btn_fact.bind("<Button-1>", fact_click)

# run it
window.mainloop()

## Things to fix:
# Negative numbers