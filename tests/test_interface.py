import tkinter as tk
from tkinter import messagebox

class TestePoker(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Poker")
        self.geometry("1200x700") # tamanho da janela (larg x alt)
"""
    def iniciar_jogo(self):
        try:
            num_jogadores = int(self.entry_jogadores.get())
            if num_jogadores <= 0:
                raise ValueError("O número de jogadores deve ser positivo.")
            self.label_resultado.config(text=f"Jogo iniciado com {num_jogadores} jogadores.")
            messagebox.showinfo("Sucesso", "O jogo foi iniciado com sucesso!")
        except ValueError as e:
            messagebox.showerror("Erro", f"Entrada inválida: {e}")
"""
if __name__ == "__main__":
    app = TestePoker()
    app.mainloop() # loop principal da janela