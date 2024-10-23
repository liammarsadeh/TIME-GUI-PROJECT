from tkinter import *
import time
def update():
    time_string = time.strftime('%H:%M:%S %p')
    label.config(text=time_string)
    day_string = time.strftime('%A')
    label2.config(text=day_string)
    year_m_d = time.strftime('%d,%b,%Y')
    label3.config(text=year_m_d)
    label.after(1000,update)
window = Tk()

label=Label (window,bg="purple",font=("Arial",30))
label.pack()
label2 =Label(window,bg="red",font=("Arial",20))
label2.pack()
label3 = Label(window,fg="green",font=("Arial",20))
label3.pack()
update()

window.mainloop()