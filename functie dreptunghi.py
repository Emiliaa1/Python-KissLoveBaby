import turtle

t=turtle.Turtle()

def dreptunghi (x, y, l, c, u, cl):
  t.penup()
  t.goto(x, y)
  t.rt(u)
  t.color(cl)
  t.pendown()
  t.begin_fill()
  for i in range (2):
    t.fd(l)
    t.rt(90)
    t.fd(c)
    t.rt(90)
  t.end_fill()
