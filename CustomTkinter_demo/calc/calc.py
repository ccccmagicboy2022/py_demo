from tkinter import *
from tkinter import messagebox
import customtkinter
def add():
 a = float(ent1.get()) 
 b = float(ent2.get())
 c = a + b
 result.configure(text=str(c))



def subtract():
    a = float(ent1.get())
    b = float(ent2.get())
    c = a - b
    result.configure(text=str(c))


def multipy():
    a = float(ent1.get())
    b = float(ent2.get())
    c = a * b
    result.configure(text=str(c))

def divide():
    a = float(ent1.get())
    b = float(ent2.get())
    c = a / b
    result.configure(text=str(c))


customtkinter.set_appearance_mode("dark")
window=customtkinter.CTk()
window.geometry("550x500")
window.title("Calculator")
window.resizable(False,False)
f1=customtkinter.CTkFrame(window,bg="#f1faee")
f1.pack(expand=True,fill=BOTH)
la1=customtkinter.CTkLabel(f1,bg="#f1faee",text_color="white",text="First Number:",text_font=("",25))
la1.place(x=20,y=20)
la2=customtkinter.CTkLabel(f1,bg="#f1faee",text_color="white",text="Second Number:",text_font=("",25))
la2.place(x=20,y=98)
ent1=customtkinter.CTkEntry(f1,bg="#f1faee",text_color="silver",placeholder_text="Enter a number",width=220)
ent1.place(x=300,y=26)
ent2=customtkinter.CTkEntry(f1,bg="#f1faee",text_color="silver",placeholder_text="Enter a number",width=220,text_font=("",12))
ent2.place(x=300,y=110)

btn1=customtkinter.CTkButton(f1,bg="#f1faee",text_color="white",text="Add",text_font=("",27),command=add,corner_radius=4,fg_color="#2a9d8f")
btn1.place(x=340,y=220)
btn2=customtkinter.CTkButton(f1,bg="#f1faee",text_color="white",text="Subtract",text_font=("",27),command=subtract,corner_radius=4,fg_color="#2a9d8f")
btn2.place(x=340,y=320)
btn3=customtkinter.CTkButton(f1,bg="#f1faee",text_color="white",text="Multipy",text_font=("",27),command=multipy,corner_radius=4,fg_color="#2a9d8f")
btn3.place(x=70,y=220)
btn4=customtkinter.CTkButton(f1,bg="#f1faee",text_color="white",text="Divide",text_font=("",27),command=divide,corner_radius=4,fg_color="#2a9d8f")
btn4.place(x=70,y=320)

Result=customtkinter.CTkLabel(f1,bg="#f1faee",text_color="orange",text="Result:",text_font=("",29))
Result.place(x=100,y=400)

result=customtkinter.CTkLabel(f1,bg="#f1faee",text_color="orange",text="",text_font=("",29))
result.place(x=300,y=400)


window.mainloop()
