import tkinter as tk

class InterfacePoker(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Poker")
        self.geometry("1200x700")

    def iniciar_jogo(self):
        pass

if __name__ == "__main__":
    app = InterfacePoker()
    app.mainloop() # loop principal da janela