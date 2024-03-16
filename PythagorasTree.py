import sys
import turtle

DEFAULT_N = 6
DEFAULT_SIZE = 550
color = 0


def pythagoras_tree_turtle(n=DEFAULT_N, l=DEFAULT_SIZE):
    color_increment = 0xFF // (n + 2)
    global color
    color = color_increment * 2

    def pythagoras_tree(t, l, n):
        global color
        t.color(f"#00{color:02x}00")
        t.forward(l)
        if n:
            color += color_increment
            for angle in [45, 90]:
                t.left(angle)
                pythagoras_tree(t, l / 1.4, n - 1)
            color -= color_increment
            t.color(f"#00{color:02x}00")
            t.left(45)
            t.forward(l)
            return
        t.left(180)
        t.forward(l)

    t = turtle.Turtle()
    t.clear()
    t.speed(0)
    t.shape("classic")
    t.penup()
    t.goto(0, -300)
    t.left(90)
    t.pendown()
    pythagoras_tree(t, l / 3, n)


def main():
    if len(sys.argv) < 2:
        print(f"Usage: python PythagorasTree.py [n]")
        print("\tn - tree factor, default n = 6")
    n = DEFAULT_N if len(sys.argv) < 2 else int(sys.argv[1])
    l = DEFAULT_SIZE

    window = turtle.Screen()
    window.bgcolor("#FCE8F9")

    pythagoras_tree_turtle(n, l)

    window.mainloop()


if __name__ == "__main__":
    main()
