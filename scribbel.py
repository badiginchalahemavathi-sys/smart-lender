import math
import random
import time
import turtle

# Screen Setup
screen = turtle.Screen()
screen.setup(width=720, height=800)
screen.bgcolor("black")
screen.title("Neon String Heart")
screen.colormode(1.0)
screen.tracer(0)

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)


# Parametric Heart Curve Formula
def get_heart_point(t, scale=14.0):
    x = 16 * (math.sin(t) ** 3) * scale
    y = (
        13 * math.cos(t)
        - 5 * math.cos(2 * t)
        - 2 * math.cos(3 * t)
        - math.cos(4 * t)
    ) * scale
    return x, y


# Layer 1: Outer Scattered Purple / Violet Wisps
pen.pensize(0.9)
for i in range(1200):
    t_val = random.uniform(0, 2 * math.pi)
    x, y = get_heart_point(t_val, scale=random.uniform(13.5, 15.5))

    angle = random.uniform(0, 2 * math.pi)
    length = random.uniform(20, 65)

    # Violet to deep purple hues
    r_col = random.uniform(0.55, 0.75)
    g_col = random.uniform(0.08, 0.22)
    b_col = random.uniform(0.75, 1.00)
    pen.pencolor(r_col, g_col, b_col)

    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.goto(x + length * math.cos(angle), y + length * math.sin(angle))

    if i % 30 == 0:
        screen.update()
        time.sleep(0.002)


# Layer 2: Deep Crimson & Ruby Red Inner Tangled Web
pen.pensize(1.1)
for i in range(2400):
    t1 = random.uniform(0, 2 * math.pi)
    t2 = t1 + random.uniform(-0.8, 0.8)

    # Smaller scales fill the center cavity
    x1, y1 = get_heart_point(t1, scale=random.uniform(3.0, 12.5))
    x2, y2 = get_heart_point(t2, scale=random.uniform(3.0, 12.5))

    # Rich red with subtle warm undertones
    r_col = random.uniform(0.85, 1.0)
    g_col = random.uniform(0.02, 0.15)
    b_col = random.uniform(0.15, 0.35)
    pen.pencolor(r_col, g_col, b_col)

    pen.penup()
    pen.goto(x1, y1)
    pen.pendown()
    pen.goto(x2, y2)

    if i % 40 == 0:
        screen.update()
        time.sleep(0.002)


# Layer 3: Vibrant Neon Magenta & Hot Pink Rim
pen.pensize(1.4)
for i in range(3200):
    t1 = random.uniform(0, 2 * math.pi)
    # Chord step around the boundary to create dense rim strokes
    t2 = t1 + random.uniform(-0.45, 0.45)

    scale1 = random.uniform(13.2, 14.8)
    scale2 = random.uniform(13.2, 14.8)

    x1, y1 = get_heart_point(t1, scale=scale1)
    x2, y2 = get_heart_point(t2, scale=scale2)

    # Vivid neon magenta / hot pink
    r_col = 1.0
    g_col = random.uniform(0.10, 0.35)
    b_col = random.uniform(0.70, 0.95)
    pen.pencolor(r_col, g_col, b_col)

    pen.penup()
    pen.goto(x1, y1)
    pen.pendown()
    pen.goto(x2, y2)

    if i % 35 == 0:
        screen.update()
        time.sleep(0.002)

screen.update()
turtle.done()