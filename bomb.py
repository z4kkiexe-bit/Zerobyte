import tkinter as tk
import random

root = tk.Tk()
root.title("BOMB DEFUSAL")

root.configure(bg="black")

label_text = tk.Label(
    root,
    text="^^BOM AKAN MELEDAK DALAM^^",
    font=("Arial", 20),
    bg="black",
    fg="white",
    wraplength=600,
)
label_text.grid(row=1, column=0, columnspan=4, pady=20)

label_timer = tk.Label(root, text="⏰ 30", font=("Arial", 40), bg="black", fg="red")
label_timer.grid(row=0, column=0, columnspan=4, pady=20)


label_soal = tk.Label(
    root, text="Soal muncul disini", font=("Arial", 20), bg="black", fg="white"
)
label_soal.grid(row=2, column=0, columnspan=4, pady=10)

label_feedback = tk.Label(root, text="", font=("Arial", 20), bg="black", fg="white")
label_feedback.grid(row=4, column=0, columnspan=3)

jawaban = tk.Entry(root, font=("Arial", 25), bg="red")
jawaban.grid(row=3, columnspan=3)
jawaban.insert(
    0,
    "<jawab di sini>",
)


def hapus_placeholder(event):
    if jawaban.get() == "<jawab di sini>":
        jawaban.delete(0, tk.END)


jawaban.bind("<FocusIn>", hapus_placeholder)


def buat_soal():
    global jawaban_benar
    angka_1 = random.randint(1, 100)
    angka_2 = random.randint(1, 100)
    jawaban_benar = angka_1 + angka_2
    label_soal.config(text=f"{angka_1} + {angka_2} = ?")


def cek_jawaban():
    if int(jawaban.get()) == jawaban_benar:
        label_feedback.config(text="BENAR!!!", fg="green")
        global bom_aktif
        bom_aktif = False
    else:
        label_feedback.config(text="SALAH!!!", fg="red")


bom_aktif = True


def kedip(nyala=True):
    if nyala:
        label_text.config(
            fg="red",
            text="^^BOM AKAN MELEDAK DALAM^^",
        )
    elif not bom_aktif:
        label_text.config(fg="green", text="^^BOM DIJINAKKAN^^")
        jawaban.config(bg="green")
        tombol_submit.config(bg="green")
        root.after(3000, root.destroy)
        return
    else:
        label_text.config(
            fg="white",
            text="^^TIMER BOM AKAN MELEDAK DALAM^^",
        )
    root.after(1000, lambda: kedip(not nyala))


kedip()

jawaban_benar = 0

tombol_submit = tk.Button(
    root,
    text="Submit",
    font=("Arial", 20),
    width=8,
    height=3,
    bg="red",
    command=cek_jawaban,
)
tombol_submit.grid(
    row=3,
    column=3,
)
buat_soal()


def countdown():
    global timer
    if not bom_aktif:
        label_timer.config(text=f"⏰ {timer}", fg="green")
        return
    timer -= 1
    label_timer.config(text=f"⏰ {timer}")
    root.after(1000, countdown)
    if timer == 0:
        root.after(1000, root.destroy)


timer = 30

countdown()


root.mainloop()
