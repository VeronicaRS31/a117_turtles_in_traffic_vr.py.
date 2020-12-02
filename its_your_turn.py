#   a118_turtles_in_traffic.py
#   Move turtles horizontally and vertically across screen.
# horizontal is left and right. Vertical is up and down
#   Stopping turtles when they collide.
import turtle as trtl

# create two empty lists of turtles, adding to them later
horiz_turtles = []
vert_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
horiz_colors = ["red", "blue", "green", "orange", "purple", "gold"]
vert_colors = ["darkred", "darkblue", "lime", "salmon", "indigo", "brown"]
collision_color= "red"
deati_color= "pink"
col="red"
tloc = 50
for s in turtle_shapes:
#setting initial location of horizontal turtles
  ht = trtl.Turtle(shape=s)
  horiz_turtles.append(ht)
  ht.penup()
  new_color = horiz_colors.pop()
  ht.fillcolor(new_color)
  ht.goto(-350, tloc)# tloc is the  y corditate of horizontal turtles
  ht.setheading(0)# set it to go right
#settting initial location of vertical turtles
  vt = trtl.Turtle(shape=s)
  vert_turtles.append(vt)
  vt.penup()
  new_color = vert_colors.pop()
  vt.fillcolor(new_color)
  vt.goto( -tloc, 350)# tloc now represents the x cordinate for vertical turtles
  vt.setheading(270)#set it to go down
  
  tloc += 50

# TODO: move turtles across and down screen, stopping for collisions

steps = 0
while steps< 30:
  for t in horiz_turtles:
    t.forward(10)
    if t.xcor()>= 0 or t.xcor()<=-400:
      t.right(180)
  for t in vert_turtles:
    t.forward(15)
    if t.ycor()<=0 or t.ycor()>=400:
      t.right(180)
  steps= steps+1
  for h in horiz_turtles:
    for v in vert_turtles:
      xdistance= abs(h.xcor() - v.xcor())
      ydistance= abs(h.ycor() - v.ycor())
      if xdistance<=10 and ydistance<= 10:
        h.right(180)
        v.right(180)


for k in horiz_turtles:
  k.fillcolor(deati_color)
  for e in vert_turtles:
    e.fillcolor(deati_color)
  
print("end of program")
    



wn = trtl.Screen()
wn.mainloop()

