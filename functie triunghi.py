import turtle

t=turtle.Turtle()

def triunghi (x, y, l, u, cl):
  t.penup()
  t.goto(x, y)
  t.rt(u)
  t.color(cl)
  t.pendown()
  t.begin_fill()
  for i in range (3):
    t.fd(l)
    t.lt(120)
  t.end_fill()
