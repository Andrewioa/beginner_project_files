from tkinter import *
from tkinter import messagebox
import random

# password generator
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"
                                                             "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w",
           "x", "y", "z"]
# make the letters upper case and add them to the list.
letters_caps = [x.upper() for x in letters]
for add in letters_caps:
    letters.append(add)
# add the symbols
symbols = [",", ".", "!", '?', "@", "$", "£", ">", "<"]
for s in symbols:
    letters.append(s)
# add numbers 1-9
for i in range(10):
    letters.append(i)
# shuffle the list so the generated password is a mix of all the above, in random order.
random.shuffle(letters)


# generate and paste the password onto the password entry.
def generate_password():
    entry3.delete(0, END)
    random_pass = []
    for _ in range(10):
        random_pass.append(random.choice(letters))
    password = ""
    for x in random_pass:
        x = str(x)
        password += x
    entry3.insert(0, password)


# save the password data into a file
def create_pass():
    if not entry1.get() or not entry2.get() or not entry3.get():
        messagebox.showerror(message="one or more entry boxes is empty!")
    else:

        is_ok = messagebox.askokcancel(message=f"website: {entry1.get()}\nusername: {entry2.get()}\nThese details"
                                               f" will be saved with the new password")
        if is_ok:
            try:
                with open("passwords.txt", "a") as file:
                    file.write(f"{entry1.get()} | {entry2.get()} | {entry3.get()}\n")
            except FileExistsError:
                with open("passwords.txt", "w") as file:
                    file.write(f"{entry1.get()} | {entry2.get()} | {entry3.get()}\n")
            entry1.delete(0, END)
            entry3.delete(0, END)


screen = Tk()
screen.title("Password manager")
screen.config(padx=50, pady=50)

# create a canvas for the image
canvas1 = Canvas(height=200, width=200)
canvas1.grid(row=0, column=1)

photo = PhotoImage(file="logo.png")
canvas1.create_image(100, 100, image=photo)

# our labels/text
label1 = Label(text="Website:")
label1.grid(row=1, column=0)
# entry box for website
entry1 = Entry(width=35)
entry1.grid(row=1, column=1, columnspan=2)
entry1.focus()

label2 = Label(text="Email/Username:")
label2.grid(row=2, column=0)
# entry box for email/username
entry2 = Entry(width=35)
entry2.grid(row=2, columnspan=2, column=1)
entry2.insert(0, "andrew.ioannou91@gmail.com")

label3 = Label(text="Password")
label3.grid(row=3, column=0)
# entry box for password
entry3 = Entry(width=18)
entry3.grid(row=3, column=1)

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2)
# add button
add_button = Button(text="Add", width=36, command=create_pass)
add_button.grid(row=4, column=1, rowspan=2, columnspan=2)

screen.mainloop()
