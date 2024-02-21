import tkinter as tk

window = tk.Tk()
window.title("Riya Agustin - latihan GUI")
logo = tk.PhotoImage(file="smkn9.png") 
WLableImage = tk.Label(image=logo)
WLableImage.pack()
window.mainloop()