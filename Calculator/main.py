from tkinter import *
from tkinter import messagebox
import tkinter.font as font


# Insert inputs in entry field
def insert(btn_text):
    input_area.insert(END, btn_text)


# Insert Parentheses
def parentheses():
    last_char = ""
    if input_area.get():
        last_char = input_area.get()[-1]
    if last_char.isdigit() or last_char == ")":
        input_area.insert(END, ")")
    else:
        input_area.insert(END, "(")


# Clear the entry field
def clear():
    input_area.delete(0, END)


# Backspace the last entered value
def backspace():
    current_text = input_area.get()
    if current_text:
        new_text = current_text[:-1]
        input_area.delete(0, END)
        input_area.insert(0, new_text)


# Find result ("=")
def result():
    current_text = input_area.get()
    if current_text:
        try:
            ans = eval(input_area.get())
            input_area.delete(0, END)
            input_area.insert(0, ans)
        except SyntaxError:
            messagebox.showerror(title="ERROR", message="Please enter correct values.")


window = Tk()
window.geometry("300x470")
window.title("Calculator")
window.resizable(0, 0)

input_area = Entry(window, width=25, font=12, justify="right")
input_area.grid(row=0, column=0, columnspan=4, padx=10, pady=5)

backspace_img = PhotoImage(file="delete.png")
img_label = Label(image=backspace_img)

myFont = font.Font(weight="bold")

# Row 1
Button(text="c", padx=20, pady=20, font=myFont, command=clear).grid(row=1, column=0, padx=5, pady=5)
Button(text="()", padx=18, pady=20, font=myFont, command=parentheses).grid(row=1, column=1)
Button(text="^", padx=20, pady=20, font=myFont, command=lambda btn_text="**": insert(btn_text)).grid(row=1, column=2)
Button(text="/", padx=22, pady=20, font=myFont, command=lambda btn_text="/": insert(btn_text)).grid(row=1, column=3)

# Row 2
Button(text="7", padx=20, pady=20, font=myFont, command=lambda btn_text="7": insert(btn_text)).grid(row=2, column=0)
Button(text="8", padx=20, pady=20, font=myFont, command=lambda btn_text="8": insert(btn_text)).grid(row=2, column=1)
Button(text="9", padx=20, pady=20, font=myFont, command=lambda btn_text="9": insert(btn_text)).grid(row=2, column=2)
Button(text="x", padx=20, pady=20, font=myFont, command=lambda btn_text="*": insert(btn_text)).grid(row=2, column=3)

# Row 3
Button(text="4", padx=20, pady=20, font=myFont, command=lambda btn_text="4": insert(btn_text)).grid(row=3, column=0,
                                                                                                    pady=5)
Button(text="5", padx=20, pady=20, font=myFont, command=lambda btn_text="5": insert(btn_text)).grid(row=3, column=1)
Button(text="6", padx=20, pady=20, font=myFont, command=lambda btn_text="6": insert(btn_text)).grid(row=3, column=2)
Button(text="-", padx=22, pady=20, font=myFont, command=lambda btn_text="-": insert(btn_text)).grid(row=3, column=3)

# Row 4
Button(text="1", padx=20, pady=20, font=myFont, command=lambda btn_text="1": insert(btn_text)).grid(row=4, column=0)
Button(text="2", padx=20, pady=20, font=myFont, command=lambda btn_text="2": insert(btn_text)).grid(row=4, column=1)
Button(text="3", padx=20, pady=20, font=myFont, command=lambda btn_text="3": insert(btn_text)).grid(row=4, column=2)
Button(text="+", padx=20, pady=20, font=myFont, command=lambda btn_text="+": insert(btn_text)).grid(row=4, column=3)

# Row 5
Button(text="0", padx=20, pady=20, font=myFont, command=lambda btn_text="0": insert(btn_text)).grid(row=5, column=0,
                                                                                                    pady=5)
Button(text=".", padx=22, pady=20, font=myFont, command=lambda btn_text=".": insert(btn_text)).grid(row=5, column=1)
Button(image=backspace_img, height=75, width=60, command=backspace).grid(row=5, column=2)
Button(text="=", padx=20, pady=20, font=myFont, command=result).grid(row=5, column=3)

window.mainloop()