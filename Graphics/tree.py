import turtle 

wn = turtle.Screen()
wn.setup(width=700, height=600)
wn.bgcolor("black")


t = turtle.Turtle()
t.speed(0)
t.pensize(10)
t.color("#c23616")
t.left(90)
t.backward(100)
t.pensize(2)




def draw(l):
    if (l<10):
        return
    else:
        t.speed(500)
        t.forward(l)
        t.color("yellow")
        t.circle(2)
        t.color("green")
        t.left(30)
        draw(3*l/4)
        t.right(60)
        draw(3*l/4)
        t.left(30)
        t.backward(l)
draw(100)          


wn.mainloop()