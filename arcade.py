import time
from turtle import Screen, Turtle

from Demos.SystemParametersInfo import new_y


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()

        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(position)

    def go_up(self):
        newY = self.ycor() + 20
        self.goto(self.xcor(), newY)

    def go_down(self):
        newY = self.ycor() - 20
        self.goto(self.xcor(), newY)

class Ball(Turtle):
    def __init__(self):
        super().__init__()

        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move=10
        self.y_move=10

    def move(self):
        newX=self.xcor()+self.x_move
        newY=self.ycor()+self.y_move
        self.goto(newX,newY)

    def bounce_y(self):
        self.y_move*=-1

    def bounce_x(self):
        self.x_move*=-1

    def resetPosition(self):
        self.goto(0,0)
        self.bounce_x()

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.lScore=0
        self.rScore=0
        self.goto(-100,200)
        self.write(self.lScore, align="center", font=("Courier",70,"normal"))
        self.goto(100,200)
        self.write(self.rScore, align="center", font=("Courier",70,"normal"))
        self.updateScore()

    def lPoint(self):
        self.lScore+=1
        self.updateScore()

    def rPoint(self):
        self.rScore+=1
        self.updateScore()

    def updateScore(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.lScore, align="center", font=("Courier", 70, "normal"))
        self.goto(100, 200)
        self.write(self.rScore, align="center", font=("Courier", 70, "normal"))

screen = Screen()
screen.bgcolor("black")
screen.setup(width=880, height=600)
screen.title("Arcade Game")
screen.tracer(0)

rPaddle = Paddle((350, 0))
lPaddle = Paddle((-350, 0))
ball=Ball()
score=Scoreboard()

screen.listen()
screen.onkey(rPaddle.go_up, "Up")
screen.onkey(rPaddle.go_down, "Down")

screen.onkey(lPaddle.go_up,"w")
screen.onkey(lPaddle.go_down,"s")

gameIsOn = True
while gameIsOn:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()

    if ball.distance(rPaddle)<50 and ball.xcor()>320 or ball.distance(lPaddle)<50 and ball.xcor()<-320:
        ball.bounce_x()

    if ball.xcor()>380:
        ball.resetPosition()
        score.lPoint()

    if ball.xcor()<-380:
        ball.resetPosition()
        score.rPoint()

screen.exitonclick()
