import tkinter as tk

persegi = tk.Tk()
persegi.title("Riya Agustin - L.persegi")
def show():
    tk.Label(text=sisi1.get()).grid(row=3,column=0)

tk.Label(persegi, text="Masukkan Nilai sisi").grid(row=0)
tk.Label(persegi, text="Hasil").grid(row=1)
hasil = tk.Label(persegi, text="0", anchor="w",width="15")

sisi1 = tk.Entry(persegi)
sisi1.grid(row=0, column=1)
hasil.grid(row=1, column=1)

def penyelesaian():
    hasil.configure(text=(int(sisi1.get())*int(sisi1.get())))

btn = tk.Button(persegi, text="L.persegi", command=penyelesaian)
btn.grid(column=0, row=4)

persegi.mainloop()