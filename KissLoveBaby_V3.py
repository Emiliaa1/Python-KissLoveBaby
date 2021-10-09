import turtle

#Turtle Setup
t = turtle.Turtle()
s = turtle.Screen()
t.speed(500)

#Paleta de culori

cl0 = "black"
cl1 = "gray"
cl2 = "silver"
cl3 = "light sky blue"
cl4 = "white"
cl5 = "dim gray"
cl6 = "tan"
cl7 = "saddle brown"
cl8 = "peru"
cl9 = "peach puff"
cl10 = "sienna"
cl11 = "navy"
cl12 = "teal"
cl13 = "dark slate gray"

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

#Functie triunghi
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

#Angajatori

#Trunchiuri
drpt(60,3,40,30,5,cl11)
drpt(105,-5,40,30,0,cl11)
drpt(150,-13,40,30,0,cl11)
t.lt(5)

# Fata jurat 1
t.pensize(2)
cerc(80,0,15,cl10)
linie(73,19,4,93,cl0)
linie(87,17,4,0,cl0)
t.lt(88)
triunghi(78,12,4,0,cl8)
t.color(cl0)
t.penup()
t.goto(76,7)
t.rt(90)
t.pendown()
t.circle(3,180)
t.rt(85)

#Fata jurat 2

cerc(125,-8,15,cl6)
linie(118,11,4,93,cl0)
linie(132,9,4,0,cl0)
t.lt(88)
triunghi(123,4,4,0,cl8)
t.color(cl0)
ln(120,0,130,-1)
t.lt(5)

#Fata jurat 3
cerc(170,-16,15,cl9)
linie(163,3,4,93,cl0)
linie(177,1,4,0,cl0)
t.lt(88)
triunghi(168,-4,4,0,cl8)
t.color(cl0)
t.penup()
t.goto(173,-11)
t.rt(270)
t.pendown()
t.circle(3,180)
t.rt(85)
t.lt(180)
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

#Hartie
t.pencolor(cl4)
t.fillcolor(cl4)
t.penup()
t.goto(60,-25)
t.begin_fill()
ln(60, -25, 80, -21)
ln(80, -21, 130, -30)
ln(130, -30, 110, -35)
ln(110, -35, 60, -25)
t.end_fill()

t.end_fill()

t.pensize(1)
t.color(cl0)
ln(84,-30,104,-25)

t.color("red")
ln(108,-34,104,-27)
ln(99,-30,114,-30)

t.color("green")
ln(70,-24,92,-24)
ln(92,-24,87,-26)

#Aspirantii la job

#Aspirantul 1

#Cap
cerc(-100, 0, 18, cl9)

#Fata

t.rt(90)
t.pensize(2)
linie(-103,22,4,0,cl0)
linie(-89,22,4,0,cl0)
triunghi(-96,16,4,0,cl8)
t.penup()
t.goto(-100,9)
t.color("pale violet red")
t.pendown()
t.begin_fill()
t.circle(5,180)
t.end_fill()
t.lt(270)

#Gat
drpt(-103, 0, 6, 7, 0,cl9 )

#Trunchi
drpt(-115, -7, 30, 40, 0, cl12)

#Pantaloni
drpt(-115, -47, 30, 10, 0, cl13)
drpt(-115, -57, 12, 30, 0, cl13)
drpt(-97, -57, 12, 30, 0, cl13)

#Mainile
drpt(-85, -16, 10, 25, 240, cl12)
drpt(-63, -3, 10, 8, 0, cl9)
drpt(-115, -7, 10, 35, 180, cl12)
drpt(-145, -25, 10, 8, 0, cl9)

#Pantofii
drpt(-115, -88, 12, 8, -60, cl0)
drpt(-97, -88, 12, 8, 0, cl0)

#Comunicare
cerc(10,40,50,"light gray")
cerc(-50,50,50,"white smoke")
triunghi(-80,70,40,60,"white smoke")
triunghi(40,80,40,60,"light gray")
