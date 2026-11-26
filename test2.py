
import customtkinter as ctk

root = ctk.CTk()
root.geometry("500x500")
root.configure(fg_color="#0D1117")
root.resizable(False, False)
root.title("InstantLogin")

frame = ctk.CTkFrame(
    root,
    width=400,
    height=500,
    fg_color="#242C36",
    border_width=7,
    border_color="#6132B9"
)
frame.pack(fill="both", expand=True, padx=15, pady=15)

label = ctk.CTkLabel(frame,
                     text="InstantLogin",
                     font=("Arial",50,"bold"),
                     text_color="#ECD134",
                     border_color="#2788D8",
                     border_width=2)

label.pack(pady=(80,35))


# Username Entry
entry_username = ctk.CTkEntry(
    frame,
    placeholder_text="Username",
    width=190,
    height=40,
    corner_radius=10,
    border_color="#3B82F6",
    border_width=2,
    fg_color="#111827",
    text_color="#F9FAFB"
)
entry_username.pack(pady=(10,20))

# Password Entry
entry_password = ctk.CTkEntry(
    frame,
    placeholder_text="Password",
    width=190,
    height=40,
    corner_radius=10,
    border_color="#3B82F6",
    border_width=2,
    fg_color="#111827",
    text_color="#F9FAFB",
    show="*"
)
entry_password.pack(pady=(10, 20))


def func():
    username = "Aayush7620"
    password = "Aayush@123"
    entry1 = entry_username.get()
    entry2 = entry_password.get()
    if entry1 == username:
        if entry2 == password:  
           label.configure(text="Logging In ....")
           root.destroy()
           app = ctk.CTkToplevel()
           app.title("GUI")
           label3 = ctk.CTkLabel(app,text="Hello")
           label3.pack()
           
           app.geometry("500x500")
           app.resizable(False,False)
        elif entry2 != password:
            label.configure(text="Wrong Password !")
    elif entry1 != username:
        label.configure(text="Wrong Username !")
      
button = ctk.CTkButton(frame,
                       text="Login",
                       width=180,
                       height=35,
                       corner_radius=15,
                       hover_color="#2B8D86",
                       border_color="#245E85",
                       border_width=2,
                       text_color="#FFFFFF",
                       command=func
                       )

button.pack(pady=10)

root.mainloop()
