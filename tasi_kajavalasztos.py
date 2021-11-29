import tkinter as tk
from tkinter import ttk
#import asdasd as asd

class Box:
   # def __init__(self):
        

    lista_kenyer = []
    lista_kenet = []
    folista = []

    root = tk.Tk()
    root.geometry('220x220')
    root.resizable(False, False)
    root.title('Kenyér, kenet demó')

    def random_var():
        asd.Randomfugg(folista)

    def mutat():
        lista_kenyer.append(sel_a1)
        lista_kenyer.append(sel_b1)
        lista_kenyer.append(sel_c1)
        lista_kenyer.append(sel_d1)
        lista_kenet.append(sel_a2)
        lista_kenet.append(sel_b2)
        lista_kenet.append(sel_c2)
        lista_kenet.append(sel_d2)
        folista.append(lista_kenyer)
        folista.append(lista_kenet)
        showinfo(
            title='Eredmény',
            message=random_var())


    sel_a1 = tk.StringVar()
    sel_b1 = tk.StringVar()
    sel_c1 = tk.StringVar()
    sel_d1 = tk.StringVar()
    sel_a2 = tk.StringVar()
    sel_b2 = tk.StringVar()
    sel_c2 = tk.StringVar()
    sel_d2 = tk.StringVar()

    breads = [("Teljes kiörlésű"),
                 ("Fehér"),
                 ("Barna"),
                  ("Kalászos")]

    creams = [("Vaj"),
              ("Medvesjat"),
              ("Kőrös"),
              ("Májkrém")]

    breads_label = ttk.Label(text = "Kenyerek")
    breads_label.grid(row = 0, column = 0, padx = 5, pady = 5)

    breads_label = ttk.Label(text = "Kenet")
    breads_label.grid(row = 0, column = 1, padx = 5, pady = 5)

    a1 = ttk.Checkbutton(
    root,
    text=breads[0],
    variable=sel_a1)
    a1.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = 'W')

    a2 = ttk.Checkbutton(
    root,
    text=creams[0],
    variable=sel_a2)
    a2.grid(row = 1, column = 1, padx = 5, pady = 5, sticky = 'W')

    b1 = ttk.Checkbutton(
    root,
    text=breads[1],
    variable=sel_b1)
    b1.grid(row = 2, column = 0, padx = 5, pady = 5, sticky = 'W')

    b2 = ttk.Checkbutton(
    root,
    text=creams[1],
    variable=sel_b2)
    b2.grid(row = 2, column = 1, padx = 5, pady = 5, sticky = 'W')

    c1 = ttk.Checkbutton(
    root,
    text=breads[2],
    variable=sel_c1)
    c1.grid(row = 3, column = 0, padx = 5, pady = 5, sticky = 'W')

    c2 = ttk.Checkbutton(
    root,
    text=creams[2],
    variable=sel_c2)
    c2.grid(row = 3, column = 1, padx = 5, pady = 5, sticky = 'W')

    d1 = ttk.Checkbutton(
    root,
    text=breads[3],
    variable=sel_d1)
    d1.grid(row = 4, column = 0, padx = 5, pady = 5, sticky = 'W')

    d2 = ttk.Checkbutton(
    root,
    text=creams[3],
    variable=sel_d2)
    d2.grid(row = 4, column = 1, padx = 5, pady = 5, sticky = 'W')

    button = ttk.Button(
    root,
    text="Generálás",
    command=mutat)
    button.grid(row = 5, columnspan = 2)


Box.mainloop()
