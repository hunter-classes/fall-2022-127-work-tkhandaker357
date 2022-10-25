import turtle

window = turtle.Screen()
drunk_pirate = turtle.Turtle()

for turns in [160, -43, 270, -97, -43, 200, -940, 17, -86]:
    drunk_pirate.forward(100)
    drunk_pirate.right(turns)

window.exitonclick()
window.mainloop()
