from graphics import *

data = {"Computewell": 6, "Dibblebit": 3, "Jones": 4, "Smith": 2}


def main():
    print("The graph displays a score comparison for 4 students")
    win = GraphWin("Student Scores", 500, 500)
    win.setCoords(0, 0, 10, 10)
    win.setBackground("white")
    usable_space_x = 7
    y = 8
    bounds = Rectangle(Point(3, 8), Point(8, 2))
    bounds.draw(win)
    for entry in data.items():
        label = Text(Point(2, y - 0.25), entry[0])
        label.draw(win)
        bar = Rectangle(
            Point(3, y), Point(2 + (entry[1] * usable_space_x) / 10, y - 0.5)
        )
        score = Text(bar.getCenter(), entry[1])
        score.move(0, -0.5)
        score.draw(win)
        bar.setFill("green")
        bar.draw(win)
        y -= 2
    win.getMouse()
    win.close()


main()
