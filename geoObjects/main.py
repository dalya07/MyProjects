from turtle import Screen, Turtle
from kreis import Kreis
from dot import Dot
from linie import Linie
from dreieck import Dreieck
from rechteck import Rechteck
from punkt import Punkt

screen = Screen()
screen.setup(width=600, height=500)

random_color = ["cyan4", "chocolate4", "DeepPink4", "LightPink3", "LightCoral", "HotPink4", "PaleVioletRed4",
                "DarkSeaGreen4", "LightBlue4"]


def take_user_input():
    user_input = input("""Was machen? 
  (0) nix machen
  (1) Punkt zeichnen
  (2) Kreis zeichnen
  (3) Linie zeichnen
  (4) Rechteck zeichnen
  (5) Dreieck zeichnen
  """)
    # Was in der user_input ist, wird in return gespeichert,
    # sodass wir es in der while-loop aufrufen oder zurückgeben können
    # ohne das return wird es garnicht gespeichert und somit
    # kann man es auch garnicht aufrufen oder zurückgeben!!
    return user_input


turtle = Turtle()

game_running = True
while game_running:
    draw = take_user_input()

    match draw:
        case "0":
            game_running = False
            break

        case "1":
            x_wert = float(input("X-Wert eingeben: "))
            y_wert = float(input("Y-Wert eingeben: "))
            p1 = Punkt(x_wert, y_wert)
            dot = Dot(p1=p1, turtle=turtle, color=random_color)
            dot.draw()

        case "2":
            x_wert = float(input("X-Wert eingeben: "))
            y_wert = float(input("Y-Wert eingeben: "))
            radius = float(input("Radius eingeben: "))
            p1 = Punkt(x_wert, y_wert)
            kreis = Kreis(p1=p1, radius=radius, turtle=turtle, color=random_color)
            kreis.draw()

        case "3":

            print("Punkt 1:")
            punkt1_x_wert = float(input("x-Wert eingeben: "))
            punkt1_y_wert = float(input("y-Wert eingeben: "))
            p1 = Punkt(x=punkt1_x_wert, y=punkt1_y_wert)
            print("Punkt 2:")
            punkt2_x_wert = float(input("x-Wert eingeben: "))
            punkt2_y_wert = float(input("y-Wert eingeben: "))
            p2 = Punkt(x=punkt2_x_wert, y=punkt2_y_wert)
            #                           Turtle() wird in output turtle gespeichert -> linie = Linie(p1, p2, turtle)
            linie = Linie(p1=p1, p2=p2, turtle=turtle, color=random_color)
            linie.draw()

        case "4":
            print("Punkt 1:")
            punkt1_x_wert = float(input("x-Wert eingeben: "))
            punkt1_y_wert = float(input("y-Wert eingeben: "))
            p1 = Punkt(x=punkt1_x_wert, y=punkt1_y_wert)
            print("Punkt 2:")
            punkt2_x_wert = float(input("x-Wert eingeben: "))
            punkt2_y_wert = float(input("y-Wert eingeben: "))
            p2 = Punkt(x=punkt2_x_wert, y=punkt2_y_wert)
            print("Punkt 3:")
            punkt3_x_wert = float(input("x-Wert eingeben: "))
            punkt3_y_wert = float(input("y-Wert eingeben: "))
            p3 = Punkt(x=punkt3_x_wert, y=punkt3_y_wert)
            print("Punkt 4:")
            punkt4_x_wert = float(input("x-Wert eingeben: "))
            punkt4_y_wert = float(input("y-Wert eingeben: "))
            p4 = Punkt(x=punkt4_x_wert, y=punkt4_y_wert)

            rechteck = Rechteck(p1=p1, p2=p2, p3=p3, p4=p4, turtle=turtle, color=random_color)
            rechteck.draw()

        case "5":
            print("Punkt 1:")
            punkt1_x_wert = float(input("x-Wert eingeben: "))
            punkt1_y_wert = float(input("y-Wert eingeben: "))
            p1 = Punkt(x=punkt1_x_wert, y=punkt1_y_wert)
            print("Punkt 2:")
            punkt2_x_wert = float(input("x-Wert eingeben: "))
            punkt2_y_wert = float(input("y-Wert eingeben: "))
            p2 = Punkt(x=punkt2_x_wert, y=punkt2_y_wert)
            print("Punkt 3:")
            punkt3_x_wert = float(input("x-Wert eingeben: "))
            punkt3_y_wert = float(input("y-Wert eingeben: "))
            p3 = Punkt(x=punkt3_x_wert, y=punkt3_y_wert)

            dreieck = Dreieck(p1=p1, p2=p2, p3=p3, turtle=turtle, color=random_color)
            dreieck.draw()

        case _:
            print("Sie können nur eine Zahl zwischen 0 und 5 wählen!")

screen.exitonclick()







