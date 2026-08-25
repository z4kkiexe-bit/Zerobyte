import google.genai as genai
import tkinter as tk

root = tk.Tk()
root.title("ZYFER.AI")
root.geometry("800x600")


input_user = tk.Entry(root, font=("Segoe UI Emoji", 18), width=15)
input_user.grid(row=1, column=0, columnspan=2)


def kirim_pesan():
    pesan = input_user.get()
    respon = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=pesan,
    )
    hapus_pesan = (input_user.delete(0, tk.END),)
    layar.insert(tk.END, f"\nAnda: {pesan} \n        ")
    layar.insert(tk.END, f"\nAI: {respon.text}\n     ")


AQ.client = genai.Client(api_key="")


layar = tk.Text(
    root,
    font=("Segoe UI Emoji", 15),
    width=30,
    height=17,
)
layar.grid(
    row=0,
    column=0,
    columnspan=3,
)

tombol_send = tk.Button(
    root,
    text="Kirim",
    font=("Segoe UI Emoji", 20),
    width=8,
    height=1,
    command=kirim_pesan,
)
tombol_send.grid(row=1, column=3, columnspan=1)

root.columnconfigure(0, weight=1)
layar.grid(row=0, column=0, columnspan=3, sticky="nsew", padx=10, pady=10)

root.mainloop()
