from graphics import *

data = [1, 2, 3, 4, 5]


def main():
    win = create_window("Spahetti Code")
    for i, dollars in enumerate(data):
        draw_bar(win, i, dollars, 5, 5)
    win.getMouse()
    win.close()


def create_window(name="Graphics!"):
    window = GraphWin(name, 500, 500)
    window.setCoords(0, 0, 10, 10)
    window.setBackground("white")
    return window


def draw_bar(win, x, y, length, max_y):
    bar = Rectangle(Point(x, 0), Point(x + 1, y))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(win)


main()
