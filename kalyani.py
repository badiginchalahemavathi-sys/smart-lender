import turtle
import random

# Screen setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=900, height=500)

# Turtle setup
t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.pensize(2)

colors = ["red", "blue", "lime", "yellow", "cyan", "magenta", "orange", "pink"]

# Define letter strokes on a 0-4 width, 0-6 height grid
LETTER_STROKES = {
    'K': [((0, 0), (0, 6)), ((4, 6), (0, 3)), ((1, 3.75), (4, 0))],
    'A': [((0, 0), (2, 6)), ((2, 6), (4, 0)), ((0.8, 2.4), (3.2, 2.4))],
    'L': [((0, 6), (0, 0)), ((0, 0), (4, 0))],
    'Y': [((0, 6), (2, 3)), ((4, 6), (2, 3)), ((2, 3), (2, 0))],
    'A': [((0, 0), (2, 6)), ((2, 6), (4, 0)), ((0.8, 2.4), (3.2, 2.4))],
    'N': [((0, 0), (0, 6)), ((0, 6), (4, 0)), ((4, 0), (4, 6))],
    'I': [((0, 6), (4, 6)), ((2, 6), (2, 0)), ((0, 0), (4, 0))]
}

def draw_star(x, y, color):
    t.penup()
    t.goto(x, y)
    t.color(color)
    t.pendown()
    for _ in range(8):
        t.forward(5)
        t.backward(5)
        t.right(45)

def render_name(text, start_x, start_y, scale=18, spacing=95):
    for idx, char in enumerate(text):
        if char not in LETTER_STROKES:
            continue
        char_origin_x = start_x + (idx * spacing)
        
        # Draw glowing burst stars along each stroke segment of the letter
        for start_pt, end_pt in LETTER_STROKES[char]:
            x1 = char_origin_x + start_pt[0] * scale
            y1 = start_y + start_pt[1] * scale
            x2 = char_origin_x + end_pt[0] * scale
            y2 = start_y + end_pt[1] * scale

            steps = 14
            for s in range(steps + 1):
                interp_x = x1 + (x2 - x1) * (s / steps)
                interp_y = y1 + (y2 - y1) * (s / steps)
                draw_star(interp_x, interp_y, random.choice(colors))

# Center and draw "KALYANI"
render_name("KALYANI", start_x=-320, start_y=-50)

turtle.done()