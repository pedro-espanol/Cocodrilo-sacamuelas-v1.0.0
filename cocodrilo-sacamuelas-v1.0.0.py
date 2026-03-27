"""
Cocodrilo sacamuelas

Versión: 1.0.0
Fecha: 27/03/2026
Autor: Pedro Español
"""
import customtkinter as ctk
import random


app = ctk.CTk()

app.geometry("1000x550")
app.title("Cocodrilo Sacamuelas v1.0.0")

label = ctk.CTkLabel(app, text="Cocodrilo Sacamuelas")
label.grid(row=0, column=0, columnspan=5, pady=5)



app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=0)
app.grid_columnconfigure(2, weight=0)
app.grid_columnconfigure(3, weight=0)
app.grid_columnconfigure(4, weight=0)
app.grid_columnconfigure(5, weight=0)
app.grid_columnconfigure(6, weight=0)
app.grid_columnconfigure(7, weight=0)
app.grid_columnconfigure(8, weight=0)
app.grid_columnconfigure(9, weight=1)


diente_malo = random.randint(1, 8)
print()


def clicar_diente(diente):
    if diente_malo == diente:
        print("has perdido")
        game_over.grid()
        cocodrilo.grid_remove()



diente1 = ctk.CTkButton(app, text="🦷", command=lambda: clicar_diente(1), width=60, height=60)
diente1.grid(row=4, column=1, pady=5, padx=5)

diente2 = ctk.CTkButton(app, text="🦷", command=lambda: clicar_diente(2), width=60, height=60)
diente2.grid(row=3, column=2, pady=5, padx=5)

diente3 = ctk.CTkButton(app, text="🦷", command=lambda: clicar_diente(3), width=60, height=60)
diente3.grid(row=2, column=3, pady=5, padx=5)

diente4 = ctk.CTkButton(app, text="🦷", command=lambda: clicar_diente(4), width=60, height=60)
diente4.grid(row=1, column=4, pady=5, padx=5)

diente5 = ctk.CTkButton(app, text="🦷", command=lambda: clicar_diente(5), width=60, height=60)
diente5.grid(row=1, column=5, pady=5, padx=5)

diente6 = ctk.CTkButton(app, text="🦷", command=lambda: clicar_diente(6), width=60, height=60)
diente6.grid(row=2, column=6, pady=5, padx=5)

diente7 = ctk.CTkButton(app, text="🦷", command=lambda: clicar_diente(7), width=60, height=60)
diente7.grid(row=3, column=7, pady=5, padx=5)

diente8 = ctk.CTkButton(app, text="🦷", command=lambda: clicar_diente(8), width=60, height=60)
diente8.grid(row=4, column=8, pady=5, padx=5)


game_over = ctk.CTkFrame(app, fg_color="red", height= 500)
game_over.grid(row=1, columnspan=10, sticky="ew")
game_over.grid_remove()




cocodrilo = ctk.CTkFrame(app, fg_color="green", height=300)
cocodrilo.grid(row=5, column=0, columnspan=10, pady=20, padx=50, sticky="ew")  # "columnspan" hace que la caja abarque 10 columnas
"""
"e" = este (derecha), "w" = oeste (izquierda)
"ew" significa que el widget se estira horizontalmente para llenar todo el ancho disponible
También podría ser "n" (norte/arriba), "s" (sur/abajo), o combinaciones como "nsew" (todas direcciones)
"""

app.mainloop()