import turtle

window = turtle.Screen()

def drawShape(size, sides, upright = True, width = 1, colour = "black", startingx = 0, startingy = 0):
  shape = turtle.Turtle()
  shape.color(colour)
  shape.width(width)

  shape.penup()
  shape.goto(startingx, startingy)
  shape.pendown()
  
  for i in range(sides):
    shape.forward(size)
    if upright:
      shape.left(360 / sides)
    else:
      shape.right(360 / sides)

drawShape(30, 6, False, 4, "blue", 50, 50)
drawShape(50, 3)

window.exitonclick()
window.mainloop()