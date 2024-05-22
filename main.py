from tkinter import *
from random import randint
 
 
class PasswordGenerator:
   def __init__(self, master):
       self.master = master
       self.master.title('Password Generator - The PyCodes')
       self.master.geometry("400x250")
       self.master.configure(bg="black")
 
 
       # Create password length LabelFrame
       length_frame = LabelFrame(self.master, text="How many characters do you want?",bg="black",fg="white")
       length_frame.pack(pady=20)
 
 
       # Create password length entry box
       self.password_length = Entry(length_frame, font=("arial", 20),bg="grey",fg="black")
       self.password_length.pack(pady=10)
 
 
       # Create returned password entry box
       self.returned_password = Entry(self.master, text='', font=("arial", 20),bg="grey",fg="black")
       self.returned_password.pack(pady=10)
 
 
       # Create button frame
       button_frame = Frame(self.master)
       button_frame.pack(pady=10)
 
 
       # Create generating password button
       pass_button = Button(button_frame, text="Generate Password", command=self.generate_password,bg="green",fg="white")
       pass_button.grid(row=0, column=0)
 
 
   def generate_password(self):
       # Clear returned_password entry box
       self.returned_password.delete(0, END)
 
 
       try:
           # Get password length in integer
           pass_number = int(self.password_length.get())
       except ValueError:
           # Handle non-integer input for password length
           self.returned_password.insert(0, "Invalid input. Please enter a valid number.")
           return
 
 
       # Create password variable
       password = ''
 
 
       # Loop through password length
       for _ in range(pass_number):
           password += chr(randint(33, 126))  # Adjusted the range to include more printable characters
 
 
       # Show the password on the returned_password entry box
       self.returned_password.insert(0, password)
 
 
 
 
def main():
   window = Tk()
   app = PasswordGenerator(window)
   window.mainloop()
 
 
if __name__ == "__main__":
   main()
