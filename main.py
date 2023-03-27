import random
from tkinter import *
from tkinter import messagebox

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class Point(object):
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y
        self.point = "+"


N = 100

list_points = []
list_points2 = []
window = Tk()
window.geometry()
window.configure()
window.title("kdz2")
frame_1 = Frame()
frame_1.configure()
frame_1.pack(side=BOTTOM)
frame_2 = Frame()
frame_2.configure()
frame_2.pack(side=TOP)
frame_3 = Frame(frame_2)
frame_3.configure()
frame_3.pack(side=LEFT)
frame_4 = Frame(frame_2)
frame_4.configure()
frame_4.pack(side=RIGHT)
fig, ax = plt.subplots(figsize=(4, 4))
canvas_1 = FigureCanvasTkAgg(fig, master=frame_3)
canvas_1.get_tk_widget().configure()


def calculateABCD(nu_x_beg, nu_x_end, nu_y_beg, nu_y_end):
    l = []
    if nu_y_end >= -nu_x_end + 1 and nu_y_beg <= -nu_x_beg + 1:
        if nu_y_end <= -nu_x_beg + 1:
            if nu_y_beg <= -nu_x_end + 1:
                xbeg = 1 - nu_y_end
                xend = nu_x_end
                ybeg = -nu_x_end + 1
                yend = nu_y_end

            else:
                xbeg = 1 - nu_y_end
                xend = 1 - nu_y_beg
                ybeg = nu_y_beg
                yend = nu_y_end
        else:
            if nu_y_beg >= -nu_x_beg + 1:
                xbeg = nu_x_beg
                xend = 1 - nu_y_beg
                ybeg = nu_y_beg
                yend = -nu_x_beg + 1
            else:
                xbeg = nu_x_beg
                xend = nu_x_end
                ybeg = 1 - nu_x_end
                yend = 1 - nu_x_beg
    l.append(xbeg)
    l.append(xend)
    l.append(ybeg)
    l.append(yend)
    return l


def paint():
    ax.clear()
    plt.plot([0, 0], [0, 5000], color="k", ms=1)
    plt.plot([2, 2.125], [0.125, 0], color="k", ms=1)
    plt.plot([2, 2.125], [-0.125, 0], color="k", ms=1)
    plt.plot([0, 5000], [0, 0], color="k", ms=1)
    plt.plot([0, 0.125], [2.125, 2], color="k", ms=1)
    plt.plot([0, -0.125], [2.125, 2], color="k", ms=1)
    ax.set_facecolor('white')
    ax.set_xlabel('f1')
    ax.set_ylabel('f2')


def generate_points():
    paint()
    list_points.clear()

    while len(list_points) != N:
        check = 0
        X0 = 0.01 * random.randint(0, 7900)
        Y0 = 0.01 * random.randint(0, 7900)
        list_points.append(
            Point((0.2 * (X0 - 70) ** 2 + 0.8 * (Y0 - 20) ** 2), (0.2 * (X0 - 10) ** 2 + 0.8 * (Y0 - 70) ** 2)))
    for i in range(len(list_points)):
        plt.plot(list_points[i].X, list_points[i].Y, "o", ms=3, color="g")
    canvas_1.draw()


def Parettooptimization():
    for i in range(len(list_points)):
        list_points[i].dels = "+"
        list_points[i].seen = "-"
    if len(list_points) == 0:
        messagebox.showinfo("Предупреждение:", "Cначала сгенерируйте точки")
    else:
        paint()
        for i in range(len(list_points)):
            if list_points[i].point != "-":
                for k in range(len(list_points)):
                    if k != i:
                        if list_points[k].X >= list_points[i].X and list_points[k].Y >= list_points[i].Y and \
                                list_points[k].point == "+":
                            list_points[k].point = "-"
                            break
            if list_points[i].point == "+":
                plt.plot(list_points[i].X, list_points[i].Y, "o", ms=3, color="g")

        canvas_1.draw()


def Ooptimization():
    if list_points2:
        list_points2.clear()
    l = calculateABCD(0.3, 0.4, 0.4, 0.7)  # POINTS
    if len(list_points) == 0:
        messagebox.showinfo("Предупреждение:", "Cначала сгенерируйте точки")
    else:
        paint()
        for i in range(len(list_points)):
            if list_points[i].point != "-":
                for k in range(len(list_points)):
                    if k != i and list_points[k].point != "-":
                        if list_points[k].X <= list_points[i].X and list_points[k].Y <= list_points[i].Y:
                            list_points[k].point = "-"
        for i in range(len(list_points)):
            list_points2.append(Point(list_points[i].X, list_points[i].Y))
        for i in range(len(list_points2)):
            if list_points2[i].point != "-":
                for k in range(len(list_points2)):
                    if k != i:
                        if ((list_points2[i].X - list_points2[k].X) * l[0] + (
                                list_points2[i].Y - list_points2[k].Y) * l[1]) > 0 and (
                                (list_points2[i].X - list_points2[k].X) * l[3] + (
                                list_points2[i].Y - list_points2[k].Y) * l[2]) > 0:
                            list_points2[i].point = "-"
        for i in range(len(list_points2)):
            if list_points2[i].point == "+":
                plt.plot(list_points2[i].X, list_points2[i].Y, "o", ms=3, color="g")

        canvas_1.draw()


def view_all():
    for p in list_points:
        print("[" + str(p.X) + ";" + str(p.Y) + "]")
    for i in range(len(list_points)):
        list_points[i].dels = "+"
        list_points[i].seen = "-"
    if len(list_points) == 0:
        messagebox.showinfo("Предупреждение:", "Cначала сгенерируйте точки")
    else:
        paint()

        for i in range(len(list_points)):
            plt.plot(list_points[i].X, list_points[i].Y, "o", ms=3, color="g")
        canvas_1.draw()


generate_btn = Button(frame_1, text="Генерация точек", command=generate_points, font="Times 10", width=50)
generate_btn.pack(side=TOP, fill=X, ipadx=6, padx=4, ipady=4, pady=5)
optimize_btn = Button(frame_1, text="Паретто-оптимальные решения", command=Parettooptimization, font="Times 10")
optimize_btn.pack(side=TOP, fill=X, ipadx=6, padx=4, ipady=4, pady=0, )
optimize2_btn = Button(frame_1, text="Ω-оптимльные решения", command=Ooptimization, font="Times 10")
optimize2_btn.pack(side=TOP, fill=X, ipadx=6, padx=4, ipady=4, pady=0, )
showall_btn = Button(frame_1, text="Все", command=view_all, font="Times 10")
showall_btn.pack(side=TOP, fill=X, ipadx=6, padx=4, ipady=4, pady=5)
canvas_1.get_tk_widget().pack(side=TOP, ipadx=6, padx=4, ipady=4, pady=5)
paint()
window.resizable(width=False, height=False)
canvas_1.draw()
window.mainloop()
