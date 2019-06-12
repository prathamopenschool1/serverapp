from tkinter import Label, Tk
root = Tk()
prompt = 'hello'
label1 = Label(root, text=prompt, width=len(prompt))
label1.pack()

def close_after_2s():
    root.destroy()

root.after(10000, close_after_2s)
root.mainloop()