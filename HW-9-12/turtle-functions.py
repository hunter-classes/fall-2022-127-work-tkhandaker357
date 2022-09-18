import turtle

window = turtle.Screen()

def ngon(size, sides, upright = True, startingx = 0, startingy = 0, width = 1, colour = "black"):
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

def hexagon():
  ngon(30, 6, False, 50, 50, 4, "blue")

hexagon()
ngon(50, 3, False, 20, 30, 8, "red")
ngon(50, 8, False)


window.exitonclick()
window.mainloop()