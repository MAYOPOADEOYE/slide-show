from tkinter import *
alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def callback(x):
    label.configure(text=f"Button clicked:{float(alphabet[x])}")


root=Tk()
label=Label()
label.grid(row=1,column=0,columnspan=26)

buttons=[0]*26 #it creates a list that holds 26 buttons
for i in range(26):
    buttons[i]=Button(text=alphabet[i],command=lambda x=i:callback(x))
    buttons[i].grid(row=0,column=1)

mainloop()