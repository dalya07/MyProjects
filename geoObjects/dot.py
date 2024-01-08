from punkt import Punkt
import random

class Dot():
  def __init__(self, p1:Punkt, turtle, color):
    super().__init__()
    self.color = color
    self.punkt1 = p1
    self.myturtle = turtle
    self.color = color

  def draw(self):
    self.myturtle.color(random.choice(self.color))
    self.myturtle.penup()
    self.myturtle.goto(x=self.punkt1.x, y=self.punkt1.y)

    self.myturtle.pendown()
    self.myturtle.pensize(10)
    self.myturtle.dot()
    self.myturtle.pensize(1)
