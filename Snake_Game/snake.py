from turtle import Turtle

POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
  def __init__(self):
    # Segments = شرائح
    self.segments = []
    self.creat_snake()
    self.head = self.segments[0]


  def creat_snake(self):
    for position in POSITION:
      turtle = Turtle(shape="square")
      turtle.penup()
      turtle.goto(position)
      turtle.color("white")
      self.segments.append(turtle)


  def move(self):
  # Move the snake continously forwards
  #                        start,      stop, step
    for seg_num in range(len(self.segments) - 1, 0, -1):
      #To tell the last segment to go to the position of the second
      # last segment
      new_x = self.segments[seg_num -1].xcor()
      new_y = self.segments[seg_num -1].ycor()
      self.segments[seg_num].goto(new_x, new_y)
    self.head.forward(MOVE_DISTANCE)


  # Sagt für den ersten viereck (head) wie viele Pixel er drehen soll
  def up(self):
    if self.head.heading() != DOWN:
      self.head.setheading(UP)

  def down(self):
    if self.head.heading() != UP:
      self.head.setheading(DOWN)

  def left(self):
    if self.head.heading() != RIGHT:
      self.head.setheading(LEFT)

  def right(self):
    if self.head.heading() != LEFT:
      self.head.setheading(RIGHT)