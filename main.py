from passgen import generate_password
import tkinter as tk 

top = tk.Tk()

B = tk.Button(top, text ="Generate Password", command = generate_password)

B.pack()
top.mainloop()