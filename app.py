import customtkinter as ctk
import random
r = random.randint(1,10)
j = str(r)

root = ctk.CTk()
root.geometry("500x400")
root._set_appearance_mode("dark")

# way to change resize
root.minsize(width=500,height=400)
root.maxsize(width=500,height=400)

#modifications
root.configure(fg="#B33B3B")

#adding logic
label = ctk.CTkLabel(master=root,
                     text="I am thinking of a number ......",
                     font=("Arial",25,"bold",),
                     text_color="#3A30CE",
                     fg_color="#252525")

label.pack(pady=20)

label1 = ctk.CTkLabel(master=root,
                     font=("Arial",50,"bold"),
                     text="",
                     text_color="#2E9455",
                     bg_color="#252525"
                     )

label1.pack(pady=40)

entry1 = ctk.CTkEntry(master=root,
                      bg_color="#252525")

entry1.pack(pady=50)

def add():
    entry1.get()
    if entry1.get() == j:
        label1.configure(text=r)
        label1.pack(pady=40)

button = ctk.CTkButton(root,
                       text="Click",
                       command=add,
                       bg_color="#252525")

button.pack()

root.mainloop()
