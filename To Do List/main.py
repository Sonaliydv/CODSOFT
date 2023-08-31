from tkinter import *
from tkinter import messagebox
import random
import string


def generate_password():
    password_list = []
    password_entry.delete(0, END)
    length = int(pass_len_entry.get())
    for i in range(length):
        password_list.append(random.choice(alpha_num))
    password = "".join(password_list)
    password_entry.insert(0, password)


def accept():
    username = user_entry.get()
    password = password_entry.get()
    print(f"Username = {username}\nPassword = {password}")
    window.clipboard_clear()
    window.clipboard_append(password)
    messagebox.showinfo(title="Success!", message="Password successfully copied to clipboard.")
    reset()


def reset():
    user_entry.delete(0, END)
    pass_len_entry.delete(0, END)
    password_entry.delete(0, END)


alpha_num = list(string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation)

window = Tk()
window.title("Password Generator")
window.geometry("300x300")
window.resizable(0, 0)

Label(text="Password Generator").grid(row=0, column=0, columnspan=3, padx=10, pady=10)
Label(text="Enter Username:").grid(row=1, column=0, padx=10, pady=10)
Label(text="Enter password length:").grid(row=2, column=0, padx=10, pady=10)
Label(text="Generated Password:").grid(row=3, column=0, padx=10, pady=10)

user_entry = Entry()
pass_len_entry = Entry()
password_entry = Entry()

generate_btn = Button(text="GENERATE PASSWORD", command=generate_password)
accept_btn = Button(text="ACCEPT", command=accept, width=7)
reset_btn = Button(text="RESET", command=reset, width=7)

user_entry.grid(row=1, column=1, columnspan=2)
pass_len_entry.grid(row=2, column=1, columnspan=2)
password_entry.grid(row=3, column=1, columnspan=2)
generate_btn.grid(row=5, column=1, pady=10, columnspan=2)
accept_btn.grid(row=7, column=1, padx=5)
reset_btn.grid(row=7, column=2, padx=5)

window.mainloop()