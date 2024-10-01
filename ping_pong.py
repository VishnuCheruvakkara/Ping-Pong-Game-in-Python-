import turtle

window = turtle.Screen()
window.title("Pong Game level 1")
window.bgcolor("black")
window.setup(width=800 , height=600)
window.tracer(0)

#score
s1 = 0
s2 = 0


#paddle A
p1= turtle.Turtle()
p1.speed(0)
p1.shape("square")
p1.color("white")
p1.shapesize(stretch_wid=5, stretch_len=1)
p1.penup()
p1.goto(-350, 0)

#paddle B
p2= turtle.Turtle()
p2.speed(0)
p2.shape("square")
p2.color("white")
p2.shapesize(stretch_wid=5, stretch_len=1)
p2.penup()
p2.goto(350, 0)
#ball 
ball= turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = -0.1

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player  A : 0  Player B : 0",align="center",font=("Courier", 24,"normal"))

#functions
def paddle1():
    y = p1.ycor()
    y += 20
    p1.sety(y)

def paddle2():
    y = p1.ycor()
    y -= 20
    p1.sety(y)

def paddle3():
    y = p2.ycor()
    y += 20
    p2.sety(y)

def paddle4():
    y = p2.ycor()
    y -= 20
    p2.sety(y)

#keyboard binding
window.listen()
window.onkeypress(paddle1, "w" )
window.onkeypress(paddle2, "s" )
window.onkeypress(paddle3, "Up" )
window.onkeypress(paddle4, "Down" )

#main game loop
while True :
      window.update()

      #move the ball
      ball.setx(ball.xcor() + ball.dx)
      ball.sety(ball.ycor() + ball.dy)
      
      # border cheching
      if ball.ycor() > 290:
          ball.sety(290)
          ball.dy *= -1

      if ball.ycor() < -290 :
          ball.sety(-290)
          ball.dy *= -1


      if ball.xcor() > 390 :
          ball.goto(0,0)
          ball.dx *= -1
          s1 += 1
          pen.clear()
          pen.write("Player  A : {}  Player B : {}".format(s1,s2), align="center",font=("Courier", 24,"normal"))
         
      if ball.xcor() < -390 :
          ball.goto(0,0)
          ball.dx *= -1
          s2 +=1
          pen.clear()
          pen.write("Player  A : {}  Player B : {}".format(s1,s2), align="center",font=("Courier", 24,"normal")) 

     #collition
      if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < p2.ycor() + 40 and ball.ycor()  > p2.ycor() -40) :
          ball.setx(340)
          ball.dx *= -1

      if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < p1.ycor() + 40 and ball.ycor()  > p1.ycor() -40) :
          ball.setx(-340)
          ball.dx *= -1
              








    
