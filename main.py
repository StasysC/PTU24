from tkinter import *

pagrindinis = Tk()
def spausti():

    raise ValueError("dsfsadfasdf")

uzrasas = Label(pagrindinis, text="Sveikas, pasauli!")
b = Button(pagrindinis,text="Mygtukas su klaida", command=spausti)
uzrasas.pack()
b.pack()
pagrindinis.mainloop()