from pico2d import *

open_canvas()
boy = load_image('character.png')
grass = load_image('grass.png')

def draw_boy(x: float, y: float):
    clear_canvas_now()
    grass.draw_now(400, 30)
    boy.draw_now(x, y)
    delay(0.1)


def move_top():
    print("Moving top")
    for x in range(780, 20, -1):
        draw_boy(x, 550)

def move_right():
    print("Moving right")
    for y in range(90, 560, 1):
        draw_boy(780, y)

def move_bottom_first():
    print("Moving bottom")
    for x in range(20, 780, 1):
        draw_boy(x, 90)

def move_bottom_last():
    print("Moving bottom")
    for x in range(20, 780, 1):
        draw_boy(x, 90)

def move_left():
    print("Moving left")
    for y in range(560, 90, -1):
        draw_boy(20, y)


def move_rectangle():
    print("Moving rectangle")
    move_bottom_first()
    move_right()
    move_top()
    move_left()
    move_bottom_last()


def move_circle():
    print("Moving circle")

    r = 200

    for deg in range(0, 360, 1):
        x = 400 + r * math.cos(math.radians(deg) - math.radians(90))
        y = 300 + r * math.sin(math.radians(deg) - math.radians(90))

        draw_boy(x, y)


while True:
    move_circle()
    move_rectangle()
    break
close_canvas()
