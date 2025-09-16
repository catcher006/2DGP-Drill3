# 2022184020 서성호
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
    for x in range(780, 20, -1):
        draw_boy(x, 550)

def move_right():
    for y in range(90, 560, 1):
        draw_boy(780, y)

def move_bottom_first():
    for x in range(400, 780, 1):
        draw_boy(x, 90)

def move_bottom_last():
    for x in range(20, 400, 1):
        draw_boy(x, 90)

def move_left():
    for y in range(560, 90, -1):
        draw_boy(20, y)


def move_rectangle():
    move_bottom_first()
    move_right()
    move_top()
    move_left()
    move_bottom_last()


def move_circle():
    r = 200

    for deg in range(0, 360, 1):
        x = 400 + r * math.cos(math.radians(deg) - math.radians(90))
        y = 290 + r * math.sin(math.radians(deg) - math.radians(90))

        draw_boy(x, y)


def move_triangle_bottom_first():
    for x in range(400, 650, 1):
        draw_boy(x, 90)


def move_triangle_right():
    for t in range(0, 101):
        x = 650 + (-250) * t / 100
        y = 90 + (500 * math.sqrt(3) / 2) * t / 100
        draw_boy(x, y)


def move_triangle_left():
    for t in range(0, 101):
        x = 400 + (-250) * t / 100
        y = 90 + 500 * math.sqrt(3) / 2 * (1 - t / 100)
        draw_boy(x, y)

def move_triangle_bottom_last():
    for x in range(150, 400, 1):
        draw_boy(x, 90)

def move_triangle():
    move_triangle_bottom_first()
    move_triangle_right()
    move_triangle_left()
    move_triangle_bottom_last()



while True:
    move_circle()
    move_rectangle()
    move_triangle()
    break
close_canvas()






