import turtle

player_a_score = 0
player_b_score = 0

# window
win = turtle.Screen()
win.title("Pong")
win.bgcolor("black")
win.setup(width=1280, height=720)
win.tracer(0)

# player a paddle
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color('white')
paddle_a.shapesize(stretch_len=0.40, stretch_wid=5)
paddle_a.penup()
paddle_a.goto(-607, 0)

# player b paddle
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.color('white')
paddle_b.shapesize(stretch_len=0.40, stretch_wid=5)
paddle_b.penup()
paddle_b.goto(600, 0)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('white')
ball.penup()
ball.goto(0, 0)
ball.dx = 0.5
ball.dy = 0.5

# score borad
score = turtle.Turtle()
score.speed(0)
score.color('white')
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("   0       0   ", align='center', font=('Consolas', 50, 'normal'))


# paddle function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# paddle movemments
win.listen()
win.onkeypress(paddle_a_up, 'w')
win.onkeypress(paddle_a_down, 's')
win.onkeypress(paddle_b_up, 'Up')
win.onkeypress(paddle_b_down, 'Down')

# game loop
while True:
    win.update()

    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border check
    if ball.ycor() > 350:
        ball.sety(350)
        ball.dy *= -1

    if ball.ycor() < -350:
        ball.sety(-350)
        ball.dy *= -1

    if ball.xcor() > 640:
        ball.goto(0, 0)
        ball.dx *= -1
        player_a_score += 1
        score.clear()
        score.write("   {}       {}   ".format(player_a_score, player_b_score), align='center', font=('Consolas', 50, 'normal'))

    if ball.xcor() < -640:
        ball.goto(0, 0)
        ball.dx *= -1
        player_b_score += 1
        score.clear()
        score.write("   {}       {}   ".format(player_a_score, player_b_score), align='center', font=('Consolas', 50, 'normal'))

    # paddle and ball collision
    if (ball.xcor() > 596 and ball.xcor() < 600) and ((ball.ycor() < paddle_b.ycor() + 50) and (ball.ycor() > paddle_b.ycor() - 50)):
        ball.dx *= -1

    if (ball.xcor() < -603 and ball.xcor() > -607) and ((ball.ycor() < paddle_a.ycor() + 50) and (ball.ycor() > paddle_a.ycor() - 50)):
        ball.dx *= -1
