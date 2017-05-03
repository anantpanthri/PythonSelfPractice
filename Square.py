import turtle

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
    window.bgcolor("grey")
    sonu = turtle.Turtle()
    draw_square(sonu)
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