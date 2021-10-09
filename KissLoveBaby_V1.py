import turtle

#Turtle Setup
t = turtle.Turtle()
s = turtle.Screen()
t.speed(500)

#Paleta de culori

cl1 = "gray"
cl2 = "silver"
cl3 = "light sky blue"
cl4 = "white"
cl5 = "dim gray"

#Functie dreptunghi
def drpt (x, y, l, c, u, cl):
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

#Functie linie 1
def linie (x, y, l, u, cl):
  t.penup()
  t.goto(x, y)
  t.rt(u)
  t.color(cl)
  t.pendown()
  t.begin_fill()
  t.fd(l)
  t.end_fill()

#Functie linie 2
def ln(x1,y1,x2,y2,cl):
  t.penup()
  t.goto(x1,y1)
  t.color(cl)
  t.pendown()
  t.goto(x2,y2)

#Background
s.bgcolor(cl2)
#Podea
drpt(-200,-50,400,150,0,cl1)
#Geam
drpt(-183,183,366,211,0,cl1)
drpt(-180,180,360,205,0,cl3)
t.pensize(4)
linie(-60,180,205,90,cl1)
linie(60,180,205,0,cl1)

ln(-160,100,-90,160,cl4)
ln(-160,60,-90,120,cl4)
ln(-160,20,-90,80,cl4)

ln(-40,100,30,160,cl4)
ln(-40,60,30,120,cl4)
ln(-40,20,30,80,cl4)

ln(80,100,150,160,cl4)
ln(80,60,150,120,cl4)
ln(80,20,150,80,cl4)

#Pancarta
drpt(-83,183,166,26,270,cl5)
drpt(-80,180,160,20,0,cl4)
t.color(cl5)
t.penup()
t.goto(-67,166)
t.pendown()
t.write("INTERVIU KISSLOVEBABY",font=('Arial',8,'bold'))

#Masa
