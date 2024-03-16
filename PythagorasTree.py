import sys
import turtle


def draw_pythagoras_tree(n=None):
    def pythagoras_tree_turtle(n, l):
        color_increment = 0xFF // (n + 2)
        color = color_increment * 2

        def pythagoras_tree(t, l, n):
            nonlocal color
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

    DEFAULT_N = 6
    n = n or DEFAULT_N
    window = turtle.Screen()
    window.bgcolor("#FCE8F9")
    pythagoras_tree_turtle(n, 550)
    window.mainloop()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: python PythagorasTree.py [n]")
        print("\tn - tree factor, default n = 6")
    n = None if len(sys.argv) < 2 else int(sys.argv[1])
    draw_pythagoras_tree(n)
