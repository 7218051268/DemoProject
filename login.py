import tkinter as tk
from tkinter import messagebox

# Dummy user credentials for demonstration purposes
USER_CREDENTIALS = {
    "admin": "Pass123",
    "user": "7218051268"
}

def login():
    username = username_entry.get()
    password = password_entry.get()

    if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
        messagebox.showinfo("Login Success", f"Welcome, {username}! You have successfully logged in.")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password. Please try again.")

def exit_app():
    root.quit()  # This will close the application

# Create the main application window
root = tk.Tk()
root.title("Login Page of Library Management System")

# Set fixed window size (width x height)
root.geometry("500x400")

# Disable resizing of the window
root.resizable(False, False)

# Set a font for the labels and button
font_style = ("Helvetica", 14)  # Adjust font family and size as needed

# Username label and entry
username_label = tk.Label(root, text="Username:", font=font_style)
username_label.pack(pady=10)
username_entry = tk.Entry(root, font=font_style)
username_entry.pack(pady=10)

# Password label and entry
password_label = tk.Label(root, text="Password:", font=font_style)
password_label.pack(pady=10)
password_entry = tk.Entry(root, show="*", font=font_style)
password_entry.pack(pady=10)

# Login button
login_button = tk.Button(root, text="Login", command=login, font=font_style, width=15, height=2)
login_button.pack(pady=20)

# Exit button
exit_button = tk.Button(root, text="Exit", command=exit_app, font=font_style, width=15, height=2)
exit_button.pack(pady=10)

# Run the application
root.mainloop()
