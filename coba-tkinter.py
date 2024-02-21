import tkinter as tk

window = tk.Tk()
window.title("Riya Agustin - latihan GUI")
kata = tk.Label(text="Hello", fg='white', bg='pink')
nama = tk.Label(text="Nama saya riya agustin")
logo = tk.PhotoImage(file="smkn9.png")
WLableImage = tk.Label(image=logo)
WButton = tk.Button( 
    text = "KlikSaya!",
    bg = "red", 
    fg = "blue" 
) 
kata.pack()
nama.pack()
WLableImage.pack()
WButton.pack()

window.mainloop()