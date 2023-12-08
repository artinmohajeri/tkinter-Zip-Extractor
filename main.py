from tkinter import *
from tkinter.filedialog import askopenfilename, askdirectory
from tkinter import messagebox
from patoolib import extract_archive
import os

# creating the window ↓↓↓
win = Tk()
win.geometry("400x270")
win.title("Artin Zip Extractor")
win.resizable(0,0)
win.iconbitmap("./logo.ico")
win.configure(bg="hotpink")
forbidden_characters = ['/', '\\', ':', '*', '?', '"', '<', '>', '|']

def browse():
    address.config(state='normal')
    address.delete(0,"end")
    global loc, file_name
    loc = askopenfilename(initialdir="select...", title="save")
    file_name = loc.split("/")[-1].split(".")[0]
    print(file_name)
    address.insert(0,loc)
    address.config(state='readonly')

def extract():
    if address.get():
        if not any(char in name_input.get() for char in forbidden_characters):
            global destination
            def extract(zip_file, destination):
                if not os.path.exists(destination):
                    os.makedirs(destination)
                try:
                    extract_archive(zip_file, outdir=destination)
                    if name_input.get():
                        os.rename(f"{destination}/{file_name}", f"{destination}/{name_input.get()}")
                        messagebox.showinfo(title="Zip File", message="Your file extracted successfuly!")
                    else:
                        messagebox.showinfo(title="Zip File", message="Your file extracted successfuly!")
                except:
                    address.config(state="normal")
                    address.delete(0,"end")
                    address.config(state="disabled")
                    name_input.delete(0,"end")
                    messagebox.showerror(title="Zip File", message="the zip file is not valid")

        else:
            name_input.delete(0,"end")
            messagebox.showerror(title="Zip File", message="output name is not suitable")
            return
    else:
        messagebox.showerror(title="Zip File", message="please choose your zipfile first")

    zip_file_path = loc
    destination = askdirectory(initialdir="where to", title="save")
    extract(zip_file_path, destination)



# widgets ↓↓↓
browse_btn = Button(win, text="select...",font=("None",14), relief="flat", command=browse)
browse_btn.pack(pady=(10,0), padx=(0,188))
address = Entry(win, font=("None", 12), width=30, state="readonly")
address.pack(pady=(5,0))

name_label = Label(win, text="Enter the name:", bg="hotpink", font=("None",14))
name_input = Entry(win, font=("None", 12), width=30)
name_label.pack(pady=(40,0))
name_input.pack()

extract_btn = Button(win, text="Extract",font=("None",14), relief="flat",command=extract)
extract_btn.pack(pady=(40,0))

win.mainloop()