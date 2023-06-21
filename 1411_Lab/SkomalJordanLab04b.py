from graphics import *


def main():
    win = GraphWin("Move the circle", 500, 500)
    win.setCoords(0.0, 0.0, 10.0, 10.0)

    bg_color = input("What color should the background be? ")
    win.setBackground(bg_color)
    x1, y1 = eval(
        input(
            "What are the x,y coordinates (bound to between 0 and 10) of the circle? "
        )
    )
    rad1 = int(input("What is the radius of the circle? "))
    center1 = Point(x1, y1)

    circ1 = Circle(center1, rad1)
    circ1.setFill("blue")
    circ1.draw(win)

    # generate second circle
    rad2 = rad1 / 2
    center2 = center1.clone()
    center2.move(0, 2 * rad1)
    circ2 = Circle(center2, rad2)
    circ2.setFill("green")
    circ2.draw(win)

    line = Line(center1, center2)
    line.setFill("red")
    line.draw(win)

    print("Click the mouse to move the circle!")

    # loop to move the second circle
    for i in range(4):
        win.getMouse()
        line.undraw()
        match i:
            case 0:
                circ2.move(2 * rad1, -2 * rad1)
            case 1:
                circ2.move(-2 * rad1, -2 * rad1)
            case 2:
                circ2.move(-2 * rad1, 2 * rad1)
            case 3:
                circ2.move(2 * rad1, 2 * rad1)
        new_center = circ2.getCenter()
        line = Line(center1, new_center)
        line.setFill("red")
        line.draw(win)

    win.getMouse()
    win.close()


main()
