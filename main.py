import random
from turtle import Turtle, Screen
import tkinter as tk
from tkinter import ttk, simpledialog

root = tk.Tk()
root.title("Apuesta por tu tortuga favorita")

def apuesta():
    global apuesta_realizada, tortuga_apostada
    tortuga_apostada = opcion_seleccionada.get().split()[0]  # Obtener el nombre sin el color
    apuesta_realizada = True
    mensaje.config(text=f"Apostaste por: {tortuga_apostada}")
    iniciar_carrera()

# Variables para la apuesta
apuesta_realizada = False
tortuga_apostada = ""

# Crear una ventana principal
screen = Screen()
screen.title("Carrera de Tortugas")
referee = Turtle()
referee.hideturtle()
turtles = {}

def create_turtle(name, color):
    new_turtle = Turtle()
    new_turtle.color(color)
    turtles[name] = new_turtle
    return new_turtle

def mover_tortuga(tortuga):
    turtles[tortuga].forward(random.randint(1, 10))

def set_referee(referee):
    referee.shape("turtle")
    referee.up()
    referee.pensize(10)
    referee.setpos(((screen.window_width() / 2) - (screen.window_width() / 2) * 0.10), (screen.window_height() / 2))
    referee.right(90)
    referee.down()
    referee.fd(screen.window_height())

tortuga_clasificadas = ["joaquin", "alfredo", "ohio", "chisato", "destiny", "soyluna"]
lista_colores = ["red", "blue", "yellow", "orange", "green", "purple"]

opcion_seleccionada = tk.StringVar()
opcion_seleccionada.set(f"{tortuga_clasificadas[0]} [{lista_colores[0]}]")  # Nombre y color
opciones_menu = [f"{nombre} [{color}]" for nombre, color in zip(tortuga_clasificadas, lista_colores)]
menu_desplegable = ttk.OptionMenu(root, opcion_seleccionada, *opciones_menu)
menu_desplegable.pack()

style = ttk.Style()
style.configure("TMenubutton", background="lightgray", foreground="black")

for opcion in opciones_menu:
    style.configure("TMenubutton", background="lightgray", foreground="black",
                    **{"TMenubutton.menubutton": {"foreground": opcion.split()[1][1:-1]}},  # Color sin corchetes
                    selector=f"TMenubutton.{opcion}")

boton_apostar = tk.Button(root, text="Apostar", command=apuesta)
boton_apostar.pack()

mensaje = tk.Label(root, text="")
mensaje.pack()

incremento = (screen.window_height() - screen.window_height() * 0.10) / len(tortuga_clasificadas)

def iniciar_carrera():
    global apuesta_realizada, tortuga_apostada

    for tortuga in tortuga_clasificadas:
        create_turtle(tortuga, lista_colores[tortuga_clasificadas.index(tortuga)])
        turtles[tortuga].up()
        turtles[tortuga].shape("turtle")
        turtles[tortuga].setpos(-((screen.window_width() / 2) - (screen.window_width() / 2) * 0.10),
                                 -((screen.window_height() / 2) - (screen.window_height() / 2) * 0.10) +
                                 incremento * tortuga_clasificadas.index(tortuga))

    set_referee(referee)

    flag = True
    while flag:
        for tortuga in tortuga_clasificadas:
            mover_tortuga(tortuga)
            if turtles[tortuga].xcor() >= ((screen.window_width() / 2) - (screen.window_width() / 2) * 0.10):
                resultado_carrera(tortuga)
                flag = False
                break

def resultado_carrera(ganadora):
    mensaje.config(text=f"Ganadora: {ganadora}")
    if apuesta_realizada:
        if tortuga_apostada == ganadora:
            mensaje.config(text=f"¡Ganaste la apuesta! Ganadora: {ganadora}")
        else:
            mensaje.config(text=f"Perdiste la apuesta. Ganadora: {ganadora}")

root.mainloop()
