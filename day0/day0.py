from turtle import*


#we want to paint a house

#step1:draw a square

width(6)
color("blue")


forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

#end of square

#draving a door
speed(30)
forward(70)
color("black")
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)

penup()
goto(200, 200)
pendown()

color("yellow")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

penup()

goto(170, 140)
right(150)

pendown()
forward(30)
right(90)
forward(30)
right(90)
forward(30)
right(90)
forward(30)

penup()


goto(0, 140)
pendown()
right(90)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
right(30)
right(60)
forward(30)
exitonclick()