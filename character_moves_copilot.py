from pico2d import *
import math

open_canvas()
boy = load_image('character.png')
grass = load_image('grass.png')

def draw_boy(x: float, y: float):
    clear_canvas_now()
    grass.draw_now(400, 30)
    boy.draw_now(x, y)
    delay(0.01)

def move_right(start_x, y):
    print("Moving right")
    for x in range(start_x, 750, 10):
        draw_boy(x, y)

def move_left(start_x, y):
    print("Moving left")
    for x in range(start_x, 50, -10):
        draw_boy(x, y)

def move_up(x, start_y):
    print("Moving up")
    for y in range(start_y, 550, 10):
        draw_boy(x, y)

def move_down(x, start_y):
    print("Moving down")
    for y in range(start_y, 90, -10):
        draw_boy(x, y)

def move_rectangle():
    print("Moving in rectangle")
    # 시작점: (50, 90)
    move_right(50, 90)    # 아래쪽 가로선
    move_up(750, 90)      # 오른쪽 세로선
    move_left(750, 550)   # 위쪽 가로선
    move_down(50, 550)    # 왼쪽 세로선

def move_circle():
    print("Moving in circle")
    cx, cy = 400, 300  # 원의 중심
    r = 200  # 반지름

    for deg in range(0, 360, 5):
        x = cx + r * math.cos(math.radians(deg))
        y = cy + r * math.sin(math.radians(deg))
        draw_boy(x, y)

def move_triangle_bottom_first():
    for x in range(400, 650, 1):
        draw_boy(x, 90)

def move_triangle_right():
    # (650, 90) -> (400, 90 + h)
    x2, y2 = 650, 90
    x3 = 400
    h = 500 * math.sqrt(3) / 2
    y3 = 90 + h
    for t in range(0, 101):
        x = x2 + (x3 - x2) * t / 100
        y = y2 + (y3 - y2) * t / 100
        draw_boy(x, y)

def move_triangle_left():
    # (400, 90 + h) -> (150, 90)
    x3 = 400
    h = 500 * math.sqrt(3) / 2
    y3 = 90 + h
    x1, y1 = 150, 90
    for t in range(0, 101):
        x = x3 + (x1 - x3) * t / 100
        y = y3 + (y1 - y3) * t / 100
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
    move_rectangle()
    move_circle()
    move_triangle()

close_canvas()
