# Library: Tkinter
# Baris kode: 24
# Instalasi: Termasuk di Python standar (tidak perlu pip)

import tkinter as tk

root = tk.Tk()
root.title("Tkinter Hello GUI")
root.geometry("500x300")
root.configure(bg="#f3f4f6")

status = tk.StringVar(value="Press the button below")

frame = tk.Frame(root, bg="#f3f4f6", padx=24, pady=24)
frame.pack(expand=True)

label = tk.Label(frame, text="Hello World!", font=("Segoe UI", 24, "bold"), bg="#f3f4f6")
label.pack(pady=(0, 16))

button = tk.Button(frame, text="Click Me", font=("Segoe UI", 14), width=14,
                   command=lambda: status.set("Have a great day!"))
button.pack(pady=(0, 12))

status_label = tk.Label(frame, textvariable=status, font=("Segoe UI", 12), bg="#f3f4f6")
status_label.pack()

root.mainloop()

