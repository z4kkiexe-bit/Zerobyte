import tkinter as tk

root = tk.Tk()
root.title("Kalkulator")


layar = tk.Entry(root, font=("Segoe UI Emoji", 18), width=30)
layar.grid(row=0, column=0, columnspan=3)


def hitung():
    hasil = eval(layar.get())
    if hasil == 13:
        layar.delete(0, tk.END)
        layar.insert(tk.END, "gak tau")
    else:
        layar.delete(0, tk.END)
        layar.insert(tk.END, hasil)


def tekan_1():
    layar.insert(tk.END, "1")


tombol_1 = tk.Button(
    root, text="1", font=("Segoe UI Emoji", 20), width=8, height=1, command=tekan_1
)
tombol_1.grid(row=1, column=0)

tombol_2 = tk.Button(
    root,
    text="2",
    font=("Segoe UI Emoji", 20),
    width=8,
    height=1,
    command=lambda: layar.insert(tk.END, "2"),
)
tombol_2.grid(row=1, column=1)

tombol_3 = tk.Button(
    root,
    text="3",
    font=("Segoe UI Emoji", 20),
    width=8,
    height=1,
    command=lambda: layar.insert(tk.END, "3"),
)
tombol_3.grid(row=1, column=2)

tombol_4 = tk.Button(
    root,
    text="4",
    font=("Segoe UI Emoji", 20),
    width=8,
    height=1,
    command=lambda: layar.insert(tk.END, "4"),
)
tombol_4.grid(row=2, column=0)

tombol_5 = tk.Button(
    root,
    text="5",
    font=("Segoe UI Emoji", 20),
    width=8,
    height=1,
    command=lambda: layar.insert(tk.END, "5"),
)
tombol_5.grid(row=2, column=1)

tombol_6 = tk.Button(
    root,
    text="6",
    font=("Segoe UI Emoji", 20),
    width=8,
    height=1,
    command=lambda: layar.insert(tk.END, "6"),
)
tombol_6.grid(row=2, column=2)

tombol_7 = tk.Button(
    root,
    text="7",
    font=("Segoe UI Emoji", 20),
    width=8,
    height=1,
    command=lambda: layar.insert(tk.END, "7"),
)
tombol_7.grid(row=3, column=0)

tombol_8 = tk.Button(
    root,
    text="8",
    font=("Segoe UI Emoji", 20),
    width=8,
    height=1,
    command=lambda: layar.insert(tk.END, "8"),
)
tombol_8.grid(row=3, column=1)

tombol_9 = tk.Button(
    root,
    text="9",
    font=("Segoe UI Emoji", 20),
    width=8,
    height=1,
    command=lambda: layar.insert(tk.END, "9"),
)
tombol_9.grid(row=3, column=2)

tombol_0 = tk.Button(
    root,
    text="0",
    font=("Segoe UI Emoji", 20),
    width=8,
    height=1,
    command=lambda: layar.insert(tk.END, "0"),
)
tombol_0.grid(row=4, column=1)

tombol_minus = tk.Button(
    root,
    text="-",
    font=("Segoe UI Emoji", 20),
    width=8,
    height=1,
    command=lambda: layar.insert(tk.END, "-"),
)
tombol_minus.grid(row=4, column=0)

tombol_tambah = tk.Button(
    root,
    text="+",
    font=("Segoe UI Emoji", 20),
    width=8,
    height=1,
    command=lambda: layar.insert(tk.END, "+"),
)
tombol_tambah.grid(row=4, column=2)

tombol_kali = tk.Button(
    root,
    text="x",
    font=("Segoe UI Emoji", 20),
    width=8,
    height=1,
    command=lambda: layar.insert(tk.END, "*"),
)
tombol_kali.grid(row=5, column=0)

tombol_bagi = tk.Button(
    root,
    text=":",
    font=("Segoe UI Emoji", 20),
    width=8,
    height=1,
    command=lambda: layar.insert(tk.END, "/"),
)
tombol_bagi.grid(row=5, column=2)

tombol_reset = tk.Button(
    root,
    text="C",
    font=("Segoe UI Emoji", 20),
    width=8,
    height=1,
    command=lambda: layar.delete(0, tk.END),
)
tombol_reset.grid(row=5, column=1)

tombol_output = tk.Button(
    root, text="=", font=("Segoe UI Emoji", 20), width=8, height=1, command=hitung
)
tombol_output.grid(row=0, column=2)


root.mainloop()
