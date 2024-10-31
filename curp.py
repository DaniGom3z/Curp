import tkinter as tk
from tkinter import ttk
from datetime import datetime
import random

def es_bisiesto(anio):
    return anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)

def obtener_vocal_interna(nombre):
    for letra in nombre[1:]:
        if letra in "AEIOU":
            return letra
    return "X"

def obtener_consonante_interna(nombre):
    for letra in nombre[1:]:
        if letra not in "AEIOU":
            return letra
    return "X"

def generar_curp():
    nombre = nombre_entry.get().strip().upper()
    primer_apellido = apellido1_entry.get().strip().upper()
    segundo_apellido = apellido2_entry.get().strip().upper()
    dia = dia_combo.get()
    mes = mes_combo.get()
    anio = anio_entry.get()
    sexo = sexo_combo.get()[0].upper()  
    estado = estado_combo.get()

    if not (nombre and primer_apellido and mes and anio and sexo and estado):
        resultado_label.config(text="Por favor, completa todos los campos obligatorios.")
        return

    try:
        anio_int = int(anio)
        dia_int = int(dia)
        mes_int = int(mes)
        if dia_int == 29 and mes_int == 2 and not es_bisiesto(anio_int):
            resultado_label.config(text="Error: el 29 de febrero solo es válido en años bisiestos.")
            return  
        fecha_nacimiento = datetime.strptime(f"{anio}-{mes}-{dia}", "%Y-%m-%d")
    except ValueError:
        resultado_label.config(text="Fecha de nacimiento inválida.")
        return

    curp = primer_apellido[0] + obtener_vocal_interna(primer_apellido)
    curp += segundo_apellido[0] if segundo_apellido else "X"
    curp += nombre[0]
    curp += fecha_nacimiento.strftime("%y%m%d")
    curp += sexo
    estados = {
        "Aguascalientes": "AS", "Baja California": "BC", "Baja California Sur": "BS", "Campeche": "CC", 
        "Chiapas": "CS", "Chihuahua": "CH", "Ciudad de México": "DF", "Coahuila": "CL", "Colima": "CM", 
        "Durango": "DG", "Guanajuato": "GT", "Guerrero": "GR", "Hidalgo": "HG", "Jalisco": "JC", 
        "México": "MC", "Michoacán": "MN", "Morelos": "MS", "Nayarit": "NT", "Nuevo León": "NL", 
        "Oaxaca": "OC", "Puebla": "PL", "Querétaro": "QT", "Quintana Roo": "QR", "San Luis Potosí": "SP", 
        "Sinaloa": "SL", "Sonora": "SR", "Tabasco": "TC", "Tamaulipas": "TS", "Tlaxcala": "TL", 
        "Veracruz": "VZ", "Yucatán": "YN", "Zacatecas": "ZS"
    }
    curp += estados.get(estado, "NE")
    curp += obtener_consonante_interna(primer_apellido)
    curp += obtener_consonante_interna(segundo_apellido) if segundo_apellido else "X"
    curp += obtener_consonante_interna(nombre)
    curp += str(random.randint(0, 9)) + chr(random.randint(65, 90))

    resultado_label.config(text="CURP generada: " + curp)

ventana = tk.Tk()
ventana.title("Generador de CURP")
ventana.geometry("400x400")

tk.Label(ventana, text="Nombre(s)*:").grid(row=0, column=0, pady=5, padx=5, sticky='e')
nombre_entry = tk.Entry(ventana)
nombre_entry.grid(row=0, column=1, pady=5)

tk.Label(ventana, text="Primer apellido*:").grid(row=1, column=0, pady=5, padx=5, sticky='e')
apellido1_entry = tk.Entry(ventana)
apellido1_entry.grid(row=1, column=1, pady=5)

tk.Label(ventana, text="Segundo apellido:").grid(row=2, column=0, pady=5, padx=5, sticky='e')
apellido2_entry = tk.Entry(ventana)
apellido2_entry.grid(row=2, column=1, pady=5)

tk.Label(ventana, text="Día de nacimiento*:").grid(row=3, column=0, pady=5, padx=5, sticky='e')
dia_combo = ttk.Combobox(ventana, values=[str(i) for i in range(1, 32)], width=5)
dia_combo.grid(row=3, column=1, sticky='w')

tk.Label(ventana, text="Mes de nacimiento*:").grid(row=4, column=0, pady=5, padx=5, sticky='e')
mes_combo = ttk.Combobox(ventana, values=[f"{i:02d}" for i in range(1, 13)], width=5)
mes_combo.grid(row=4, column=1, sticky='w')

tk.Label(ventana, text="Año de nacimiento*:").grid(row=5, column=0, pady=5, padx=5, sticky='e')
anio_entry = tk.Entry(ventana, width=10)
anio_entry.grid(row=5, column=1, pady=5)

tk.Label(ventana, text="Sexo*:").grid(row=6, column=0, pady=5, padx=5, sticky='e')
sexo_combo = ttk.Combobox(ventana, values=["Hombre", "Mujer"], width=10)
sexo_combo.grid(row=6, column=1, pady=5)

tk.Label(ventana, text="Estado*:").grid(row=7, column=0, pady=5, padx=5, sticky='e')
estado_combo = ttk.Combobox(ventana, values=[
    "Aguascalientes", "Baja California", "Baja California Sur", "Campeche", 
    "Chiapas", "Chihuahua", "Ciudad de México", "Coahuila", "Colima", 
    "Durango", "Guanajuato", "Guerrero", "Hidalgo", "Jalisco", 
    "México", "Michoacán", "Morelos", "Nayarit", "Nuevo León", 
    "Oaxaca", "Puebla", "Querétaro", "Quintana Roo", "San Luis Potosí", 
    "Sinaloa", "Sonora", "Tabasco", "Tamaulipas", "Tlaxcala", 
    "Veracruz", "Yucatán", "Zacatecas"
])
estado_combo.grid(row=7, column=1, pady=5)

generar_button = tk.Button(ventana, text="Generar CURP", command=generar_curp)
generar_button.grid(row=8, column=0, columnspan=2, pady=20)

resultado_label = tk.Label(ventana, text="")
resultado_label.grid(row=9, column=0, columnspan=2)

ventana.mainloop()
