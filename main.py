from tkinter import *
from tkinter import messagebox
import random
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]

    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]

    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)




# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website:{
            "email": email,
            "password": password
        }
    }


    if len(website) == 0  or len(password) == 0:
        messagebox.showerror("Error", "Please enter your website and password")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file,indent=4)
        else:
            data.update(new_data)
            with open("data.json",mode="w") as data_file:
                json.dump(data, data_file,indent=4)

        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


def search_data():
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            if website in data:
                messagebox.showinfo("Information", f"password: {data[website]['password']}\n email: {data[website]['email']}\n website: {website}")
            else:
                messagebox.showinfo("Error", "There is no matching website")
    except FileNotFoundError:
        messagebox.showerror("Error", "There is no any website info")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("My password generator")
window.config(padx=20, pady=20, bg="white")


#------------ Canvas------------
canvas = Canvas(width=200, height=200, bg='white', highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img, )
canvas.grid(column=1, row=0)

# ------------Labels--------------
website_label = Label(text="Website",bg="white",fg="black" )
email_label = Label(text="Email/Username",bg="white",fg="black" )
password_label = Label(text="Password",bg="white",fg="black")
website_label.grid(column=0, row=1)
email_label.grid(column=0, row=2)
password_label.grid(column=0, row=3)

# -----------Entries---------------

website_entry = Entry(width=21, bg="white",highlightthickness=0,fg="black",insertbackground="black",)
website_entry.grid(column=1, row=1, pady=5)
website_entry.focus()
email_entry = Entry(width=36, bg="white" ,highlightthickness=0,fg="black",insertbackground="black")
email_entry.grid(column=1, row=2, columnspan=2, pady=5)
email_entry.insert(0,'laman@gmail.com')
password_entry = Entry(width=21, bg="white",highlightthickness=0,fg="black",insertbackground="black")
password_entry.grid(column=1, row=3, pady=5)


# ----------Buttons------------------
generate_password_button = Button(text="Generate password",bg="white", fg="black",highlightbackground="white",command=generate_password)
generate_password_button.grid(column=2, row=3)
add_button = Button(text="Add",bg="white",width=36, fg="black",highlightbackground="white",command=save_data)
add_button.grid(column=1, row=4, columnspan=2,padx=5, pady=5)
search_button = Button(text="Search",bg="white",width=15, fg="black",highlightbackground="white",command=search_data)
search_button.grid(column=2, row=1,padx=5, pady=5)




window.mainloop()