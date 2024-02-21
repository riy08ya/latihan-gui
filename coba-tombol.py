import tkinter as tk

window = tk.Tk()
window.title("Riya Agustin - latihan GUI")

def out(): 
    print("Tombol diklik")
WButton = tk.Button( 
    text = "Klik Saya!", 
    width = 20, 
    height = 10, 
    bg = "red", 
    fg = "blue" 
) 
WButton.pack()
window.mainloop()