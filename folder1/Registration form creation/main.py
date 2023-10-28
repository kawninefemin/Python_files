# Import tkinter module
from tkinter import *

# Create a root window
root = Tk()

# Set the title of the window
root.title("Registration Form")

# Create a label for the title of the form
title_label = Label(root, text="Registration Form", font=("Arial", 22))
title_label.pack()

# Create a frame to hold the input fields and buttons
frame = Frame(root)
frame.pack()

# Create labels and entries for each field
name_label = Label(frame, text="Name")
name_label.grid(row=0, column=0, padx=10, pady=10)
name_entry = Entry(frame)
name_entry.grid(row=0, column=1, padx=10, pady=10)

country_label = Label(frame, text="Country")
country_label.grid(row=1, column=0, padx=10, pady=10)
country_entry = Entry(frame)
country_entry.grid(row=1, column=1, padx=10, pady=10)

gender_label = Label(frame, text="Gender")
gender_label.grid(row=2, column=0, padx=10, pady=10)
gender_var = StringVar()
gender_var.set("Male")
gender_radio1 = Radiobutton(frame, text="Male", variable=gender_var, value="Male")
gender_radio1.grid(row=2, column=1, padx=10, pady=10)
gender_radio2 = Radiobutton(frame, text="Female", variable=gender_var, value="Female")
gender_radio2.grid(row=2, column=2, padx=10, pady=10)
gender_radio3 = Radiobutton(frame, text="Other", variable=gender_var, value="Other")
gender_radio3.grid(row=2, column=3, padx=10, pady=10)

email_label = Label(frame, text="Email")
email_label.grid(row=3, column=0, padx=10, pady=10)
email_entry = Entry(frame)
email_entry.grid(row=3, column=1, padx=10, pady=10)

# Create a function to submit the form data
def submit():
    # Get the values from the entries
    name = name_entry.get()
    country = country_entry.get()
    gender = gender_var.get()
    email = email_entry.get()

    # Print the values to the console
    print(f"Name: {name}")
    print(f"Country: {country}")
    print(f"Gender: {gender}")
    print(f"Email: {email}")

    # Clear the entries
    name_entry.delete(0, END)
    country_entry.delete(0, END)
    email_entry.delete(0, END)

# Create a function to reset the form data
def reset():
    # Clear the entries
    name_entry.delete(0, END)
    country_entry.delete(0, END)
    email_entry.delete(0, END)

    # Set the default value for the gender radio buttons
    gender_var.set("Male")

# Create buttons for submit and reset
submit_button = Button(frame, text="Submit", command=submit)
submit_button.grid(row=4, column=1, padx=10, pady=10)
reset_button = Button(frame, text="Reset", command=reset)
reset_button.grid(row=4, column=2, padx=10, pady=10)

# Start the main loop of the window
root.mainloop()

