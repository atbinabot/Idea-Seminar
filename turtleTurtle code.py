
import turtle 


#1
star = turtle.Turtle()

for i in range(30):
    star.forward(50)
    star.right(150)
    
turtle.done()

#2


spiral = turtle.Turtle()

for i in range(20):
    spiral.forward(i * 10)
    spiral.right(144)
    
turtle.done()

#3
polygon = turtle.Turtle()

num_sides = 6
side_length = 60
angle = 360.0 / num_sides 

for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)
    
turtle.done()

#4
painter = turtle.Turtle()

painter.pencolor("blue")

for i in range(50):
    painter.forward(50)
    painter.left(123) # Let's go counterclockwise this time 
    
painter.pencolor("red")
for i in range(50):
    painter.forward(100)
    painter.left(123)
    
turtle.done()

#5
dot_distance = 20
width = 10
height = 10

seurat.penup()

for y in range(height):
    for i in range(width):
        seurat.dot()
        seurat.forward(dot_distance)
    seurat.backward(dot_distance * width)
    seurat.right(90)
    seurat.forward(dot_distance)
    seurat.left(90)
    
turtle.done()