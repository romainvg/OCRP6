from tkinter import *

# Creer une premier Fenêtre #

from tkinter import Tk

window: Tk = Tk()

# Personnaliser la Fenetre

window.title("Remote Administration Tool By Guihot Romain")
window.geometry("1080x720")
window.minsize(800, 600)
window.maxsize(1080, 720)
window.iconbitmap("logo.ico")
window.config(background="black")
window.attributes('-alpha', 0.8)

# Creation de la barre de Menu

menu_bar = Menu(window)

# Creer un premier Menu

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="General Settings")
menu_bar.add_cascade(label="Builder")
#menu_bar.add_cascade(label="A.I Management")
menu_bar.add_cascade(label="Workplace")
menu_bar.add_cascade(label="Tools")
menu_bar.add_cascade(label="Logs")
menu_bar.add_cascade(label="About")

# Configurer la barre de Menu

window.config(menu=menu_bar)

# Creation de la Frame Principale - All Servers Connexions

Mainframe = Frame(window, height=360, width=1080, relief=RAISED, bd=8, bg="green")
Mainframe.grid(row=0, column=0)
Mainframe.pack(fill="both")

# Creation de la Frame Secondaire - Logs In/Out Connexions

# Creation de la Frame Tertiaire - WorldMap


# Afficher le GUI

window.mainloop()