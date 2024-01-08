from punkt import Punkt
import random

class Kreis():
    def __init__(self, p1: Punkt, radius, turtle, color):
        self.punkt1 = p1
        self.radius = radius
        self.myturtle = turtle
        self.color = color

    def draw(self):
        self.myturtle.color(random.choice(self.color))
        self.myturtle.penup()
        self.myturtle.goto(x=self.punkt1.x, y=self.punkt1.y)

        self.myturtle.pendown()
        self.myturtle.circle(radius=self.radius)


