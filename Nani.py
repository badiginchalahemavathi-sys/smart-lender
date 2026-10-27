import turtle
import random

# Screen setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=900, height=600)

t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.pensize(2)

colors = ["red", "deepskyblue", "lime", "yellow", "cyan", "magenta", "orange", "violet"]

def interpolate_points(p1, p2, num_steps=20):
    """Generate evenly spaced points along a line segment."""
    points = []
    for step in range(num_steps + 1):
        ratio = step / num_steps
        x = p1[0] + (p2[0] - p1[0]) * ratio
        y = p1[1] + (p2[1] - p1[1]) * ratio
        points.append((x, y))
    return points

# Define letter stroke paths for "NANI"
letter_strokes = [
    # N
    [(-320, -70), (-320, 70), (-240, -70), (-240, 70)],
    # A
    [(-200, -70), (-150, 70), (-100, -70)],
    # A - Crossbar
    [(-175, -5), (-125, -5)],
    # N
    [(-60, -70), (-60, 70), (20, -70), (20, 70)],
    # I - Stem
    [(100, -70), (100, 70)],
    # I - Top bar
    [(70, 70), (130, 70)],
    # I - Bottom bar
    [(70, -70), (130, -70)],
]

# Generate coordinates along the name path
outline_points = []
for stroke in letter_strokes:
    for i in range(len(stroke) - 1):
        outline_points.extend(interpolate_points(stroke[i], stroke[i + 1], num_steps=18))

# Animate rays and burst stars around the perimeter of the name
for point in outline_points:
    t.penup()
    t.goto(0, 0)  # Origin of glowing rays
    c = random.choice(colors)
    t.color(c)
    t.pendown()
    t.goto(point[0], point[1])

    # Burst star at perimeter vertex
    for _ in range(8):
        t.forward(6)
        t.backward(6)
        t.right(45)

turtle.done()