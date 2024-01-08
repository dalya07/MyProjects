from punkt import Punkt
import random

class Linie():
  def __init__(self, p1: Punkt, p2: Punkt, turtle, color):
    super().__init__()
    self.punkt1 = p1
    self.punkt2 = p2
    # Turtle() wird in self.myturtle gespeichert
    self.myturtle = turtle
    self.color = color

  def draw(self):
    self.myturtle.color(random.choice(self.color))
    self.myturtle.penup()
    # für punkt 1
    self.myturtle.goto(x=self.punkt1.x, y=self.punkt1.y)
    # für punkt 2
    self.myturtle.pendown()
    self.myturtle.goto(x=self.punkt2.x, y=self.punkt2.y)

