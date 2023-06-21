from graphics import *
import time


def main():
    win_name = input("Please name the window: ")
    color1 = input("Please input a standard color: ")
    x1, y1 = eval(input("what are the x, y coordinates of the circle? "))
    radius1 = float(input("what is the radius of the circle? "))

    win = GraphWin(win_name, 500, 500)
    center1 = Point(x1, y1)
    circ1 = Circle(center1, radius1)
    circ1.setFill(color1)
    circ1.draw(win)

    color2 = input("What color would you like the second circle to be? ")
    x2, y2 = eval(input("what are the x, y coords of the second circle? "))
    radius2 = float(input("what is the radius of the 2nd circle? "))
    center2 = Point(x2, y2)
    circ2 = Circle(center2, radius2)
    circ2.setFill(color2)
    circ2.draw(win)

    line = Line(center1, center2)
    line.setFill("red")
    line.draw(win)

    win.getMouse()

    for i in range(10):
        circ1.move(10, 10)
        line.undraw()
        time.sleep(2)

    new_center = circ1.getCenter()
    line = Line(new_center, center2)
    line.setFill("red")
    line.draw(win)

    win.getMouse()


main()
