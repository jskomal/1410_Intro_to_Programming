from graphics import *


def main():
    win = GraphWin("Celsius Convertor", 300, 300)
    win.setBackground("white")
    win.setCoords(0.0, 0.0, 4.0, 4.0)
    input_label = Text(Point(1.5, 3), "Temp in C")
    input_label.draw(win)
    input_text = Entry(Point(2.5, 3), 5)
    input_text.setText("0.0")
    input_text.draw(win)
    output = Text(Point(1.5, 1), "Temp in F")
    output.draw(win)
    output_deg = Text(Point(2.5, 1), "32.0")
    output_deg.draw(win)
    button_text = Text(Point(2.0, 2.0), "Convert it!")
    button_text.draw(win)
    button = Rectangle(Point(1, 1.5), Point(3, 2.5))
    button.draw(win)
    button_p1 = button.getP1()
    button_p2 = button.getP2()
    mouse_pos = win.getMouse()
    print(mouse_pos)
    mouse_x = mouse_pos.getX()
    mouse_y = mouse_pos.getY()
    print(mouse_x, mouse_y)
    if mouse_x > 1 and mouse_x < 3 and mouse_y > 1.5 and mouse_y < 2.5:
        celcius = float(input_text.getText())
        fahrenheit = round(9.0 / 5.0 * celcius + 32, 2)
        output_deg.setText(fahrenheit)
        button_text.setText("Exit")

        win.getMouse()
        win.close()
    else:
        win.getMouse()
        win.close()
        main()


main()
