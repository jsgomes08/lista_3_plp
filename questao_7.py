from pyswip import Prolog
import tkinter as tk
from tkinter import ttk, messagebox

# Inicializar Prolog
prolog = Prolog()
prolog.consult("sistema_doacao.pl")  # Certifique-se de que o arquivo Prolog está no mesmo diretório

# Função para verificar compatibilidade
def verificar_compatibilidade():
    doador = combo_doador.get()
    receptor = combo_receptor.get()
    if not doador or not receptor:
        messagebox.showerror("Erro", "Selecione um doador e um receptor!")
        return

    # Consulta Prolog
    query = list(prolog.query(f"podedoar({doador}, {receptor})"))
    if query:
        messagebox.showinfo("Resultado", f"{doador} pode doar para {receptor}.")
    else:
        messagebox.showinfo("Resultado", f"{doador} NÃO pode doar para {receptor}.")

# Função para listar pessoas por tipo sanguíneo ou fator RH
def listar_por_tipo():
    tipo = combo_tipo.get()
    if not tipo:
        messagebox.showerror("Erro", "Selecione um tipo sanguíneo ou RH!")
        return

    if tipo in ["a", "b", "ab", "o"]:
        query = list(prolog.query(f"tiposanguineo(X, {tipo})"))
    else:
        query = list(prolog.query(f"fatorrh(X, {tipo})"))

    pessoas = [r["X"] for r in query]
    messagebox.showinfo("Resultado", f"Pessoas com {tipo}: {', '.join(pessoas) if pessoas else 'Nenhuma'}")

# Configurar interface
root = tk.Tk()
root.title("Sistema de Doação de Sangue")
root.geometry("400x300")

# Widgets
ttk.Label(root, text="Selecione o Doador:").pack(pady=5)
combo_doador = ttk.Combobox(root, values=["joao", "davi", "maria", "ana", "julia", "alice", "pedro", "laura", "manuela", "vitoria", "manuel", "jose", "carlos", "telma"])
combo_doador.pack(pady=5)

ttk.Label(root, text="Selecione o Receptor:").pack(pady=5)
combo_receptor = ttk.Combobox(root, values=["joao", "davi", "maria", "ana", "julia", "alice", "pedro", "laura", "manuela", "vitoria", "manuel", "jose", "carlos", "telma"])
combo_receptor.pack(pady=5)

ttk.Button(root, text="Verificar Compatibilidade", command=verificar_compatibilidade).pack(pady=10)

ttk.Label(root, text="Listar por Tipo Sanguíneo ou RH:").pack(pady=5)
combo_tipo = ttk.Combobox(root, values=["a", "b", "ab", "o", "+", "-"])
combo_tipo.pack(pady=5)

ttk.Button(root, text="Listar Pessoas", command=listar_por_tipo).pack(pady=10)

# Rodar a aplicação
root.mainloop()
