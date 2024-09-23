

import turtle
import winsound

# Global settings
window = turtle.Screen()
window.title("Pong by Mahdi")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# Load sound effects
paddel_hit_sound = 'scored.wav'
score_sound = 'retro-game-coin-pickup.wav'
wall_hit_sound = 'arcade-game-jump.wav'

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape('square')
paddle_a.color('blue')
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-370, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.color('red')
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(370, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color('white')
ball.shapesize(stretch_wid=1, stretch_len=1)
ball.penup()
ball.goto(0, 0)
ball.dx = 0.3
ball.dy = -0.3

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color('yellow')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A:0   Player B:0", align="center",
          font=("courier", 24, "normal"))

# Functions


def show_menu():
    pen.clear()
    pen.goto(0, 0)
    pen.write("Welcome to Pong!\nChoose an option:\n1. Play with a Friend\n2. Play with AI\nPress 1 or 2 to select.",
              align="center", font=("courier", 24, "normal"))


def select_mode(mode):
    if mode == '1':
        window.onkeypress(paddle_a_up, 'w')
        window.onkeypress(paddle_a_down, 's')
        window.onkeypress(paddle_b_up, 'Up')
        window.onkeypress(paddle_b_down, 'Down')
        start_game('Friend')
    elif mode == '2':
        window.onkeypress(paddle_a_up, 'w')
        window.onkeypress(paddle_a_down, 's')
        start_game('AI')


def paddle_a_up():
    y = paddle_a.ycor()
    if y < 240:
        y += 40
        paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    if y > -240:
        y -= 40
        paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    if y < 240:
        y += 40
        paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    if y > -240:
        y -= 40
        paddle_b.sety(y)


def ai_move():
    if paddle_b.ycor() < ball.ycor() and paddle_b.ycor() < 240:
        paddle_b.sety(paddle_b.ycor() + 40)
    elif paddle_b.ycor() > ball.ycor() and paddle_b.ycor() > -240:
        paddle_b.sety(paddle_b.ycor() - 40)


def start_game(mode):
    global score_a, score_b
    score_a = 0
    score_b = 0
    pen.clear()
    pen.write("Player A:0   Player B:0", align="center",
              font=("courier", 24, "normal"))

    # Main game loop
    while True:
        window.update()

        # Move the ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # Border checking
        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1
            winsound.PlaySound(wall_hit_sound, winsound.SND_ASYNC)

        if ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1
            winsound.PlaySound(wall_hit_sound, winsound.SND_ASYNC)

        if ball.xcor() > 390:
            ball.goto(0, 0)
            ball.dx *= -1
            score_a += 1
            pen.clear()
            pen.write("Player A:{}   Player B:{}".format(
                score_a, score_b), align="center", font=("courier", 24, "normal"))
            winsound.PlaySound(score_sound, winsound.SND_ASYNC)

        if ball.xcor() < -390:
            ball.goto(0, 0)
            ball.dx *= -1
            score_b += 1
            pen.clear()
            pen.write("Player A:{}   Player B:{}".format(
                score_a, score_b), align="center", font=("courier", 24, "normal"))
            winsound.PlaySound(score_sound, winsound.SND_ASYNC)

        # Paddle and ball collisions
        if (340 < ball.xcor() < 350) and (paddle_b.ycor() - 50 < ball.ycor() < paddle_b.ycor() + 50):
            ball.setx(340)
            ball.dx *= -1
            winsound.PlaySound(paddel_hit_sound, winsound.SND_ASYNC)

        if (-350 < ball.xcor() < -340) and (paddle_a.ycor() - 50 < ball.ycor() < paddle_a.ycor() + 50):
            ball.setx(-340)
            ball.dx *= -1
            winsound.PlaySound(paddel_hit_sound, winsound.SND_ASYNC)

        # AI movement if playing against AI
        if mode == 'AI':
            ai_move()


# Show the menu
show_menu()

# Keyboard binding for menu selection
window.listen()
window.onkeypress(lambda: select_mode('1'), '1')
window.onkeypress(lambda: select_mode('2'), '2')

turtle.done()
