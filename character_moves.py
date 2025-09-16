from pico2d import *

open_canvas()
boy = load_image('character.png')
grass = load_image('grass.png')


def move_top():
    pass


def move_left():
    pass


def move_bottom():
    pass


def move_right():
    pass


def move_rectangle():
    print("Moving rectangle")
    move_top()
    move_right()
    move_bottom()
    move_left()
    pass


def move_circle():
    print("Moving circle")

    r = 200

    for deg in range(0, 360, 10):
        x = 400 + r * math.cos(math.radians(deg))
        y = 300 + r * math.sin(math.radians(deg))

        clear_canvas_now()
        boy.draw_now(x,y)
        delay(0.1)
    pass


while True:
    move_circle()
    move_rectangle()
    # break
    pass
close_canvas()
