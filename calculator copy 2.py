import tkinter as tk
import math

# Définitions de fonctions
def click(button_text):
    # égal
    if button_text == "=":
        try:
            result = str(eval(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(0, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(0, "Erreur")
    # Effacer l'entierté de l'entrée
    elif button_text == "C":
        entry.delete(0, tk.END)
    # Effacer le dernier caractère
    elif button_text == "CE":
        entry.replace(str(entry[-1], " "))
    # racine carrée
    elif button_text == "√":
        try:
            result = str("%.6f"%math.sqrt(eval(entry.get())))
            entry.delete(0, tk.END)
            entry.insert(0, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(0, "Erreur")
    # sinus, cosinus, tangente
    elif button_text in ["sin", "cos", "tan"]:
        try:
            value = eval(entry.get())
            if button_text == "sin":
                result = str("%.6f"%math.sin(math.radians(value)))
            elif button_text == "cos":
                result = str("%.6f"%math.cos(math.radians(value)))
            elif button_text == "tan":
                result = str("%.6f"%math.tan(math.radians(value)))
            entry.delete(0, tk.END)
            entry.insert(0, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(0, "Erreur")
    # Logarithme Néperien
    elif button_text == "ln":
        try:
            result = str("%.6f"%math.log(eval(entry.get())))
            entry.delete(0, tk.END)
            entry.insert(0, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(0, "Erreur")
    #logarithme
    elif button_text == "log":
        try:
            result = str("%.6f"%math.log10(eval(entry.get())))
            entry.delete(0, tk.END)
            entry.insert(0, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(0, "Erreur")
    # 
    elif button_text == "^":
        entry.insert(tk.END, "**")
    # e : exponentielle
    elif button_text == "exp":
        try:
            result = str("%.6f"%math.exp(eval(entry.get())))
            entry.delete(0, tk.END)
            entry.insert(0, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(0, "Erreur")
    # pi
    elif button_text == "π":
        try:
            result = entry.get() + str("%.6f"%math.pi) # affiche 6 chiffres après la virgule
            entry.delete(0, tk.END)
            entry.insert(0, result) # affiche le résultat
        except:
            entry.delete(0, tk.END)
            entry.insert(0, "Erreur")
    # factorielle
    elif button_text == "n!":
        try:
            result = str("%.6f"%math.factorial(int(eval(entry.get()))))
            entry.delete(0, tk.END)
            entry.insert(0, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(0, "Erreur")
    # valeur absolue
    elif button_text == "abs":
        try:
            result = str(eval(abs(entry.get())))
            entry.delete(0, tk.END)
            entry.insert(0, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(0, "Erreur")
    else:
        entry.insert(tk.END, button_text)


# Fenêtre principale
window = tk.Tk()
window.title("Calculatrice Scientifique")
window.geometry("400x500") # dimensionner la fenêtre à l'ouverture
window.configure(bg="#eedae4")

# Zone d'affichage
entry = tk.Entry(window, font=("Segoe UI", 20), width=17, borderwidth=0, relief="flat", bg="#F3F3F3", fg="#FF70A6")
entry.grid(row=0, column=0, columnspan=8, padx=10, pady=10)

# Couleurs des boutons dans un dictionnaire nommé button_colors
# Pour chaque "type" de boutons on attribut une certaine couleur
button_colors = {"number": "pink", "operator": "#f3f3f3", "function": "#ff70a6", "equals": "#c42863", "clear": "#FF6961", "ce":"#ff8e88"}

# Configuration des boutons dans une liste indiquant à quoi correspondent chaque boutons
buttons = [
    ("7", "number"), ("8", "number"), ("9", "number"), ("/", "operator"), ("-","operator"), ("sin", "function"), ("cos", "function"), ("n!", "function"),
    ("4", "number"), ("5", "number"), ("6", "number"), ("*", "operator"), ("+", "operator"), ("tan", "function"), ("√", "function"), ("exp", "function"),
    ("1", "number"), ("2", "number"), ("3", "number"), ("(", "operator"), (")", "operator"), ("ln", "function"), ("log", "function"), ("π", "function"),
    ("0", "number"), (".", "number"), ("C", "clear"), ("CE", "ce"), ("^", "operator"), ("|x|","function"), ("=", "equals")
]

# Placement des boutons
for i, (text, btn_type) in enumerate(buttons):
    color = button_colors[btn_type]
    button = tk.Button(window, text=text, command=lambda x=text: click(x), width=6, height=2, font=("Segoe UI", 12),bg=color, fg="black" if btn_type != "equals" and btn_type!= "clear" and btn_type!= "ce" else "white",activebackground="#ffdee8" if btn_type != "equals" else "#6f1937", relief="flat")
    
    # pour des raisons de responsives design (optimisation de l'espace de la calculette sur le canva), j'utilise les propriétés weight et sticky
    button.grid(row=(i//8)+1, column=i%8, padx=2, pady=2, sticky="nsew") # sticky = "nsew" permet de le faire coller sur tous les côtés
    window.grid_rowconfigure((i//7)+1, weight=1)   # Ajustement des lignes
    window.grid_columnconfigure(i%8, weight=1)     # Ajustement des colonnes
# Création bouton
boutegal = tk.Button(window, text="=", command=lambda x=text: click(x), width=6, height=2, font=("Segoe UI", 12),bg = color, fg= "white",activebackground="#ffdee8", relief = "flat")
boutegal.grid(row= 4,column= 6, columnspan=3, padx=2, pady= 2, sticky ="nsew")
# Redimensionnement automatique
for i in range(1, 6):
    window.grid_columnconfigure(i, weight=1)

# Lancer l'application
window.mainloop()
