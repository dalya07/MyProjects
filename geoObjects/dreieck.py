from punkt import Punkt
import random

class Dreieck():
    def __init__(self, p1: Punkt, p2: Punkt, p3: Punkt, turtle, color):
      self.punkt1 = p1
      self.punkt2 = p2
      self.punkt3 = p3
      self.myturtle = turtle
      self.color = color

    def draw(self):
      self.myturtle.color(random.choice(self.color))
      self.myturtle.penup()
      # für punkt 1
      self.myturtle.goto(x=self.punkt1.x, y=self.punkt1.y)
      self.myturtle.pendown()
      # für punkt 2
      self.myturtle.goto(x=self.punkt2.x, y=self.punkt2.y)
      # für punkt 3
      self.myturtle.goto(x=self.punkt3.x, y=self.punkt3.y)
      # geht zurück zu punkt 1
      self.myturtle.goto(x=self.punkt1.x, y=self.punkt1.y)
