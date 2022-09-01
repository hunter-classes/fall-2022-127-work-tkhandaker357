import turtle

window = turtle.Screen()

# crush draws a square
crush = turtle.Turtle()
crush.forward(60)
crush.left(90)
crush.forward(60)
crush.left(90)
crush.forward(60)
crush.left(90)
crush.forward(60)
crush.left(90)

# crush2 draws a triangle
crush2 = turtle.Turtle()
crush2.up()
crush2.goto(100, 100)
crush2.down()

crush2.forward(60)
crush2.right(90 + 30)
crush2.forward(60)
crush2.right(90 + 30)
crush2.forward(60)
crush2.right(90 + 30)

window.exitonclick()
window.mainloop()