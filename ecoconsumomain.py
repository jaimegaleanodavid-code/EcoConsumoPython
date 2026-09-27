import tkinter as tk
from logica import PilaAparatos
from ui import EcoConsumoUI


def main():
    
    pila_principal = PilaAparatos()

   
    root = tk.Tk()
    
    
    app = EcoConsumoUI(root, pila_principal)
    root.mainloop()


if __name__ == "__main__":
    main()