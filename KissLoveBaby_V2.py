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
cl6 = "tan"
cl7 = "saddle brown"
cl8 = "peru"
cl9 = "peach puff"

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

#Functie cerc
def cerc(x,y,r,cl):
  t.penup()
  t.goto(x,y)
  t.color(cl)
  t.pendown()
  t.begin_fill()
  t.circle(r)
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
def ln(x1,y1,x2,y2):
  t.penup()
  t.goto(x1,y1)
  t.pendown()
  t.goto(x2,y2)

#Background
s.bgcolor(cl2)
#Podea
drpt(-200,-50,400,150,0,cl1)

#Umbra masa
t.penup()
t.goto(130,-130)
t.color(cl5)
t.begin_fill()
ln(130,-130,200,-170)
ln(200,-170,200,-50)
ln(200,-50,130,-50)
ln(130,-50,130,-130)
t.end_fill()

#Geam
drpt(-183,183,366,211,0,cl1)
drpt(-180,180,360,205,0,cl3)
t.pensize(4)
linie(-60,180,205,90,cl1)
linie(60,180,205,0,cl1)

t.color(cl4)
ln(-160,100,-90,160)
ln(-160,60,-90,120)
ln(-160,20,-90,80)

ln(-40,100,30,160)
ln(-40,60,30,120)
ln(-40,20,30,80)

ln(80,100,150,160)
ln(80,60,150,120)
ln(80,20,150,80)

#Pancarta
drpt(-83,183,166,26,270,cl5)
drpt(-80,180,160,20,0,cl4)
t.color(cl5)
t.penup()
t.goto(-67,166)
t.pendown()
t.write("INTERVIU KISSLOVEBABY",font=('Arial',8,'bold'))
t.penup()

#Masa

#Fata1
t.pencolor(cl8)
t.fillcolor(cl8)
t.goto(0,-15)
t.begin_fill()
ln(0,-15,0,-60)
ln(0,-60,130,-130)
ln(130,-130,130,-50)
ln(130,-50,0,-15)
t.end_fill()

#Fata2
t.fillcolor(cl6)
t.begin_fill()
ln(0,-15,50,-10)
ln(50,-10,190,-35)
ln(190,-35,130,-50)
ln(130,-50,0,-15)
t.end_fill()

#Fata3
t.fillcolor(cl7)
t.begin_fill()
ln(130,-50,130,-130)
ln(130,-130,190,-100)
ln(190,-100,190,-35)
ln(190,-35,130,-50)
t.end_fill()

#Jurati??
drpt()
cerc(80,0,15,cl9)
cerc(125,-8,15,cl9)
cerc(170,-16,15,cl9)

#Hartie
t.pencolor('white')
t.fillcolor('white')
t.penup()
t.goto(60,-25)
t.begin_fill()
ln(60, -25, 80, -21)
ln(80, -21, 130, -30)
ln(130, -30, 110, -35)
ln(110, -35, 60, -25)
t.end_fill()
