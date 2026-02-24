import customtkinter as ctk
app = ctk.CTk()
app.title("say hi")
app.geometry("175x75")

def say_hi():
    for i in range(10):
        print(f"Hallo du, willkommen! Schön, dass du da bist.")
        i+=1


button = ctk.CTkButton(app, text="push me", command=say_hi)
button.grid(row=0, column=0, padx=20, pady=20)


app.mainloop()