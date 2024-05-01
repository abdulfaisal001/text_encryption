import tkinter as tk
from tkinter import messagebox, scrolledtext
import string

# ye Function message encryption k liye hai !!
def encrypt(message, shift):
    encrypted_message = ""
    for char in message:
        if char in string.ascii_letters:
            if char.islower():
                encrypted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            encrypted_char = char
        encrypted_message += encrypted_char
    return encrypted_message

# ye Function  message decryption k liye hai !!
def decrypt(message, shift):
    return encrypt(message, -shift)

# to decide the encryption or decryption function !!
def perform_operation(operation):
    message = entry_message.get()
    shift = int(entry_shift.get())
    if operation == "Encrypt":
        result = encrypt(message, shift)
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, result)
    else:
        result = decrypt(message, shift)
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, result)
    refresh_button.grid(row=4, column=0, columnspan=2, padx=20, pady=5)

# Function to refresh the interface after  performing an operation/ singe task
def refresh():
    entry_message.delete(0, tk.END)
    entry_shift.delete(0, tk.END)
    result_text.delete(1.0, tk.END)
    refresh_button.grid_forget()

root = tk.Tk()
root.title("Encryption and Decryption")

label_message = tk.Label(root, text="Enter Message:")
label_message.grid(row=0, column=0, padx=15, pady=5)
entry_message = tk.Entry(root)
entry_message.grid(row=0, column=1, padx=15, pady=5)

label_shift = tk.Label(root, text="Enter key :")
label_shift.grid(row=1, column=0, padx=20, pady=15)
entry_shift = tk.Entry(root)
entry_shift.grid(row=1, column=1, padx=20, pady=5)

button_encrypt = tk.Button(root, text="Encrypt", command=lambda: perform_operation("Encrypt"))
button_encrypt.grid(row=2, column=0, padx=20, pady=5)

button_decrypt = tk.Button(root, text="Decrypt", command=lambda: perform_operation("Decrypt"))
button_decrypt.grid(row=2, column=1, padx=20, pady=5)

result_text = scrolledtext.ScrolledText(root, width=30, height=10, wrap=tk.WORD)
result_text.grid(row=3, columnspan=2, padx=20, pady=5)

refresh_button = tk.Button(root, text="Refresh", command=refresh)
root.configure(background='light grey')
root.mainloop()
