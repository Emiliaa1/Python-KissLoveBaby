def linie (x, y, l, u, cl):
  t.penup()
  t.goto(x, y)
  t.lt(u)
  t.color(cl)
  t.pendown()
  t.begin_fill()
  t.fd(l)
  t.end_fill()
