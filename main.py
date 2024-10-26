import turtle
turtle.Screen().bgcolor("Pink")
turtle.Screen().setup(400,500)
arrow=turtle.Turtle()
numSides=4
for i in range(numSides):
    arrow.forward(80)
    arrow.right(60)
    arrow.forward(60)
    arrow.right(120)
turtle.done()