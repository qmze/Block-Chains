import tkinter as tk
from tkinter import messagebox

class LoginPage(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Login and Signup Page")
        self.geometry("400x300")

        self.create_widgets()

    def create_widgets(self):
        self.tab_control = tk.Notebook(self)

        self.login_tab = tk.Frame(self.tab_control)
        self.signup_tab = tk.Frame(self.tab_control)

        self.tab_control.add(self.login_tab, text="Login")
        self.tab_control.add(self.signup_tab, text="Signup")

        self.tab_control.pack(expand=1, fill="both")

        self.create_login_tab()
        self.create_signup_tab()

    def create_login_tab(self):
        login_label = tk.Label(self.login_tab, text="Login Page", font=("Helvetica", 16))
        login_label.grid(row=0, column=1, pady=10)

        username_label = tk.Label(self.login_tab, text="Username:")
        username_label.grid(row=1, column=0, pady=5)

        password_label = tk.Label(self.login_tab, text="Password:")
        password_label.grid(row=2, column=0, pady=5)

        self.login_username_entry = tk.Entry(self.login_tab)
        self.login_username_entry.grid(row=1, column=1, pady=5)

        self.login_password_entry = tk.Entry(self.login_tab, show="*")
        self.login_password_entry.grid(row=2, column=1, pady=5)

        login_button = tk.Button(self.login_tab, text="Login", command=self.login)
        login_button.grid(row=3, column=1, pady=10)

    def create_signup_tab(self):
        signup_label = tk.Label(self.signup_tab, text="Signup Page", font=("Helvetica", 16))
        signup_label.grid(row=0, column=1, pady=10)

        new_username_label = tk.Label(self.signup_tab, text="New Username:")
        new_username_label.grid(row=1, column=0, pady=5)

        new_password_label = tk.Label(self.signup_tab, text="New Password:")
        new_password_label.grid(row=2, column=0, pady=5)

        self.signup_username_entry = tk.Entry(self.signup_tab)
        self.signup_username_entry.grid(row=1, column=1, pady=5)

        self.signup_password_entry = tk.Entry(self.signup_tab, show="*")
        self.signup_password_entry.grid(row=2, column=1, pady=5)

        signup_button = tk.Button(self.signup_tab, text="Signup", command=self.signup)
        signup_button.grid(row=3, column=1, pady=10)

    def login(self):
        username = self.login_username_entry.get()
        password = self.login_password_entry.get()

        # Add authentication logic here
        # For demonstration purposes, let's assume a hardcoded username and password
        if username == "demo" and password == "demo":
            messagebox.showinfo("Login Successful", "Welcome, {}".format(username))
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

    def signup(self):
        new_username = self.signup_username_entry.get()
        new_password = self.signup_password_entry.get()

        # Add user registration logic here
        # For demonstration purposes, let's assume a simple registration success
        messagebox.showinfo("Signup Successful", "Account created for {}".format(new_username))


if __name__ == "__main__":
    app = LoginPage()
    app.mainloop()
