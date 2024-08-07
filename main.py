from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password():
    password_entry.delete(0, END)
    password = [choice(letters) for _ in range(randint(8, 10))]
    password += [choice(symbols) for _ in range(randint(2, 4))]
    password += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password)
    shuffled_password = "".join(password)
    password_entry.insert(0, shuffled_password)
    pyperclip.copy(shuffled_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showwarning(title=None, message="Please don't leave any of the fields empty!")
    else:
        is_ok = messagebox.askokcancel(message=f"Is it ok to save?", detail=f"\nWebsite: {website} "
                                               f"\nEmail : {email} \nPassword : {password}")

        if is_ok:
            with open('data.txt', 'a') as file:
                file.write(f"{website} | {email} | {password}\n")

            website_entry.delete(0, END)
            password_entry.delete(0, END)
            website_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.minsize(width=520, height=380)
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(125, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0, sticky="E")
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0, sticky="E")
password_label = Label(text="Password:")
password_label.grid(row=3, column=0, sticky="E")

# Entries
website_entry = Entry()
website_entry.grid(row=1, column=1, columnspan=2, sticky="EW")
website_entry.focus()
email_entry = Entry()
email_entry.grid(row=2, column=1, columnspan=2, sticky="EW")
email_entry.insert(0, "@gmail.com")
password_entry = Entry()
password_entry.grid(row=3, column=1, sticky="EW")

# Buttons
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2, sticky="EW")
add_button = Button(text="Add", command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")

window.mainloop()
