import colorsys
import turtle

# Screen setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Geometric Spiral Pattern")
screen.setup(width=800, height=800)

# Turtle configuration
t = turtle.Turtle()
t.speed(0)
turtle.tracer(2)  # Accelerates rendering; set to (1) or remove for slower drawing
t.pensize(2)
turtle.colormode(1.0)

# Total iterations and color cycles
n = 300

for i in range(n):
    # Smooth HSV to RGB color transition across the spectrum
    color = colorsys.hsv_to_rgb(i / 150, 1.0, 1.0)
    t.pencolor(color)

    # Drawing the 3-arm expanding spiral geometry
    t.forward(i * 1.2)
    t.right(120)
    t.forward(i * 0.8)
    t.right(59)

t.hideturtle()
turtle.update()
turtle.done()