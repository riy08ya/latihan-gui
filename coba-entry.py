import tkinter as tk

window = tk.Tk()
window.title("Riya Agustin - latihan GUI")

def show():
    tk.Label(text = e1.get()).grid(row=3,column=0) 
    tk.Label(text = e2.get()).grid(row=3,column=1 )
    tk.Label(text = e3.get()).grid(row=3,column=2)
tk.Label(window, text="Nama Depan").grid(row=0) 
tk.Label(window, text="Nama Belakang").grid(row=1)
tk.Label(window, text="Nama Lengkap").grid(row=2)
e1 = tk.Entry(window) 
e2 = tk.Entry(window) 
e3 = tk.Entry(window)
b1 = tk.Button(text="show", command=show)
e1.grid(row=0, column=1) 
e2.grid(row=1, column=1) 
e3.grid(row=2, column=1)
b1.grid(row=3, column=1)

window.mainloop()