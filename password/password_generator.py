import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("1200x1200")
        self.root.configure(bg="#ffffff")
        
        # Title Label
        self.title_label = tk.Label(root, text="Password Generator", font=("Times New Roman", 50, "bold"), bg="#ffffff", fg="black")
        self.title_label.pack(pady=10)
        
        # Length Label and Entry
        self.length_label = tk.Label(root, text="Enter Password Length:", font=("Times New Roman", 60), bg="#ffffff", fg="red")
        self.length_label.pack()
        
        self.length_entry = tk.Entry(root, width=10, font=("Times New Roman", 30),justify="center")
        self.length_entry.pack(pady=20)
        
        # Generate Button
        self.generate_button = tk.Button(root, text="Generate Password", font=("Times New Roman", 30, "bold"), bg="#fff00c", fg="black", command=self.generate_password)
        self.generate_button.pack(pady=10)
        
        # Password Display
        self.password_label = tk.Label(root, text="Generated Password:", font=("Times New Roman", 50), bg="#ffffff", fg="Green")
        self.password_label.pack(pady=6)
        
        self.password_display = tk.Entry(root, width=30, font=("Times New Roman", 40), bg="#079e00", fg="black", borderwidth=0, justify="center")
        self.password_display.pack()

    def generate_password(self):
        try:
            # Get the desired password length from the entry field
            length = int(self.length_entry.get())
            if length < 4:
                messagebox.showwarning("Warning", "Password length should be at least 4 for better security.")
                return

            # Generate a random password
            characters = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(random.choice(characters) for _ in range(length))
            
            # Display the generated password
            self.password_display.config(state='normal')
            self.password_display.delete(0, tk.END)
            self.password_display.insert(0, password)
            self.password_display.config(state='readonly')
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number for password length.")

# Main application
if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
