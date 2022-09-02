import turtle

window = turtle.Screen()

bar = turtle.Turtle()
bar.up()
bar.goto(0, 50)
bar.down()

def drawShape(shape, size, sides):
  for i in range(sides):
    shape.forward(size)
    shape.right(360 / sides)

drawShape(bar, 50, 4)

window.exitonclick()
window.mainloop()