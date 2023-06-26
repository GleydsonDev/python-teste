from tkinter import *
from time import strftime

win = Tk()
win.geometry("400x300")
win.title("Relógio")
win.configure(background='#97e695', padx=40, pady=40)

texto_horario = Label(win, text="", padx=80, pady=80, background='#7ab879', font=('arial', 20, 'bold'))
texto_horario.grid(column=0, row=1)
   
def horario():
    hora = strftime('%H:%M:%S %p')
    texto_horario["text"] = hora
    texto_horario.after(1000, horario)

texto_cima = Label(win, text='Horario Atual', command=horario(), font=('arial', 10))
texto_cima.grid(column=0, row=0)


win.mainloop()