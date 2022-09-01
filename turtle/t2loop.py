import turtle

window = turtle.Screen()
foo = turtle.Turtle()

for i in range(4):
  foo.forward(50)
  foo.right(90)

foo.up()
foo.goto(100, 30)
foo.down()
foo.width(2)

for i in range(3):
  foo.forward(30)
  foo.left(120)
  
window.exitonclick()
window.mainloop()