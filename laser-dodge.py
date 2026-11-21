import turtle

screen = turtle.Screen()
screen.title("Dodge the Lasers!")
screen.bgcolor("black")
screen.setup(width=700, height=600)
screen.tracer(0)

finish_line = turtle.Turtle()
finish_line.color("gold")
finish_line.pensize(5)
finish_line.penup()
finish_line.goto(-330, 220)
finish_line.pendown()
finish_line.goto(330, 220)
finish_line.hideturtle()

player = turtle.Turtle()
player.shape("turtle")
player.color("limegreen")
player.penup()
player.goto(0, -240)
player.setheading(90)
player.speed(0)

score = 0

score_display = turtle.Turtle()
score_display.hideturtle()
score_display.penup()
score_display.color("white")
score_display.goto(0, 255)


def update_score_display():
  score_display.clear()
  score_display.write(f"Score: {score}", align="center", font=("Arial", 16, "bold"))


update_score_display()


def move_up():
  if player.ycor() < 240:
    player.setheading(90)
    player.sety(player.ycor() + 20)


def move_down():
  if player.ycor() > -250:
    player.setheading(270)
    player.sety(player.ycor() - 20)


def move_left():
  if player.xcor() > -320:
    player.setheading(180)
    player.setx(player.xcor() - 20)


def move_right():
  if player.xcor() < 320:
    player.setheading(0)
    player.setx(player.xcor() + 20)


screen.listen()
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")


def game_loop():
  global score

  if player.ycor() >= 220:
    score += 1
    update_score_display()
    player.goto(0, -240)
    player.setheading(90)

  screen.update()
  screen.ontimer(game_loop, 20)


game_loop()
turtle.done()