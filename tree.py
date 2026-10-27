import colorsys
import math
import random
import turtle

# Screen setup
screen = turtle.Screen()
screen.setup(width=1000, height=850)
screen.bgcolor("#03020c")
screen.title("Cosmic Tree")
screen.colormode(1.0)
screen.tracer(5)

# Turtles setup
t = turtle.Turtle()
t.hideturtle()
t.speed(0)

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)


def refresh(step, interval=4):
    if step % interval == 0:
        screen.update()


def get_hsv(h, s=0.85, v=1.0):
    return colorsys.hsv_to_rgb(h % 1.0, s, v)


# Draw background stars
random.seed(42)
num_stars = 200

pen.penup()
for i in range(num_stars):
    x = random.randint(-480, 480)
    y = random.randint(-400, 400)
    pen.goto(x, y)
    star_color = get_hsv(random.random(), s=random.uniform(0.1, 0.4), v=random.uniform(0.6, 1.0))
    pen.dot(random.uniform(1, 3.5), star_color)
    refresh(i, interval=10)


# Recursive Cosmic Tree function
step_counter = 0


def draw_cosmic_branch(branch_len, angle_offset, depth, hue):
    global step_counter

    if depth == 0 or branch_len < 4:
        # Draw glowing cosmic leaves / blossoms
        t.penup()
        leaf_color = get_hsv(hue, s=0.9, v=1.0)
        t.dot(random.uniform(4, 7), leaf_color)
        t.pendown()
        return

    # Branch styling based on depth
    t.pensize(max(1, depth * 1.3))
    t.pencolor(get_hsv(hue, s=0.8, v=0.95))

    t.forward(branch_len)
    step_counter += 1
    refresh(step_counter, interval=8)

    # Branching angles & length reductions
    angle_left = 22 + random.uniform(-4, 6)
    angle_right = 24 + random.uniform(-4, 6)
    len_mult = random.uniform(0.72, 0.82)

    # Left branch
    t.left(angle_left)
    draw_cosmic_branch(branch_len * len_mult, angle_left, depth - 1, hue + 0.04)

    # Right branch
    t.right(angle_left + angle_right)
    draw_cosmic_branch(branch_len * len_mult, angle_right, depth - 1, hue + 0.07)

    # Return to base of current branch
    t.left(angle_right)
    t.penup()
    t.backward(branch_len)
    t.pendown()


# Position and render tree
t.penup()
t.goto(0, -320)
t.setheading(90)
t.pendown()

draw_cosmic_branch(branch_len=115, angle_offset=0, depth=10, hue=0.55)

screen.update()
turtle.done()