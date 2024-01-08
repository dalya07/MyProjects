from turtle import Turtle
ALIGN = "center"
FONT = ("Arial", 20, "normal")

# now it can do everything a turtle class can do
class Scoreboard(Turtle):

    def __init__(self):
      super().__init__()
      self.score = 0
      self.goto(x=0 , y=265)
      self.color("white")
      self.write(f"Score: {self.score}",align=ALIGN, font=FONT)
      self.hideturtle()
      self.penup()

    def game_over(self):
      self.goto(0, 0)
      self.write("GAME OVER", align=ALIGN, font=FONT)

    def increase_score(self):
      self.clear()
      self.score += 1
      self.write(f"Score: {self.score}",align=ALIGN, font=FONT)
