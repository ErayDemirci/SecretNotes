from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import onetimepad


# window
root = Tk()
root.title("Top Secret")
root.config(bg="lightgrey")
root.geometry("500x500")

# icon
pic = Image.open("topsecret.png")
pic = pic.resize((100, 100), Image.LANCZOS)

icon = ImageTk.PhotoImage(pic)
icon_label = Label(root, image=icon, bg="lightgrey")
icon_label.pack(pady=20)

def encrypting():
    if title_entry.get() == "" or key_entry.get() == "" or secret_text.get("1.0", END).strip() == "":
        messagebox.showwarning("Warning", "Please fill in all fields before encrypting or decrypting.")
    else:
        t1 = secret_text.get("1.0", END).strip()
        k1 = key_entry.get()

        enc_text = onetimepad.encrypt(t1, k1)

        with open("mysecret.txt", "a") as f:
            f.write("Title: " + title_entry.get() + "\n")
            f.write("Encrypted Text: " + enc_text + "\n")
            f.write("-" * 20 + "\n")

        title_entry.delete(0, END)
        key_entry.delete(0, END)
        secret_text.delete("1.0", END)

def decrypting():
    if key_entry.get() == "" or secret_text.get("1.0", END).strip() == "":
        messagebox.showwarning("Warning", "Please fill in all fields before encrypting or decrypting.")
    else:
        try:
            t2 = secret_text.get("1.0", END).strip()
            k2 = key_entry.get()

            dec = onetimepad.decrypt(t2, k2)

            secret_text.delete("1.0", END)
            secret_text.insert("1.0", dec)
        except Exception as e:
            print("ERROR: ", e)
            messagebox.showwarning(title="Warning", message="Please enter encrypted text!")

# title label
title_label = Label(root, text="Enter Your Title", bg="lightgrey", fg="black")
title_label.pack()

# title entry
title_entry = Entry(root, bg="white", fg="black", highlightthickness=0, insertbackground="black")
title_entry.focus()
title_entry.pack()

# secret label
secret_label = Label(root, text="Enter Your Secret", bg="lightgrey", fg="black")
secret_label.pack()

# secret text
secret_text = Text(root, bg="white", fg="black", insertbackground="black", height=10, width=30, highlightthickness=0, bd=2, relief="sunken")
secret_text.pack()

# key label
key_label = Label(root, text="Enter Master Key", bg="lightgrey", fg="black")
key_label.pack()

# key entry
key_entry = Entry(root, bg="white", fg="black",insertbackground="black", highlightthickness=0)
key_entry.pack()

# encrypt button
encrypt_button = Button(root, text="Save & Encrypt", highlightbackground="lightgrey", relief="flat",
                        command=encrypting)
encrypt_button.pack(pady=10)

# decrypt button
decrypt_button = Button(root, text="Decrypt", highlightbackground="lightgrey", relief="flat", command=decrypting)
decrypt_button.pack()

root.mainloop()
