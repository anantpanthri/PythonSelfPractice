import turtle

#this function will draw a flower in a window
def draw_flower(sonu):
    sonu.shape("turtle")
    sonu.color("red")
    sonu.speed(0)
    for i in range(1, 40):
        sonu.forward(50)
        sonu.left(60)
        sonu.forward(50)
        sonu.left(120)
        sonu.forward(50)
        sonu.left(60)
        sonu.forward(50)
        sonu.right(10)
    sonu.right(60)
    sonu.color("black")
    sonu.forward(200)
    sonu.left(120)
    #leaf begins
    sonu.color("green")
    sonu.forward(50)
    sonu.left(60)
    sonu.forward(50)
    sonu.left(120)
    sonu.forward(50)
    sonu.left(60)
    sonu.forward(50)
    sonu.left(150)
    sonu.forward(90)
    sonu.left(160)
    sonu.forward(58)
    sonu.left(50)
    sonu.color("black")
    sonu.forward(100)
    sonu.right(90)
    sonu.forward(100)
    sonu.left(180)
    sonu.forward(200)
    sonu.left(90)
    sonu.forward(500)
    sonu.left(90)
    sonu.forward(200)

    sonu.left(90)
    sonu.forward(500)

    sonu.left(90)

#this function will draw a square
def draw_square(sonu):
    sonu.shape("turtle")
    sonu.speed(0)
    sonu.color("black")
    k=0
    for i in range(1,250):
        if k<4:
         sonu.forward(100)
         sonu.right(90)
         k+=1
        else:
         sonu.right(10)
         k=0

def draw_triangle(tom):
    for i in range(1,4):
        tom.forward(100)
        tom.left(120)

def draw_art():
    window= turtle.Screen()
    window.bgcolor("white")
    sonu = turtle.Turtle()
    draw_flower(sonu)

   # draw_square(sonu)
    ''' hanu = turtle.Turtle()
        hanu.shape("arrow")
        hanu.color("black")
        window.bgcolor("yellow")
        hanu.circle(100)
        window.bgcolor("grey")
        tom = turtle.Turtle()
        draw_triangle(tom)'''

    window.exitonclick()
draw_art()