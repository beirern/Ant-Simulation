import random
import time
import tkinter as tk
from optparse import OptionParser

MAX_NUM_ANTS = 100000
FULL_SCREEN_SIZE = (1280, 720)
NORMAL_SCREEN_SIZE = (320, 320)


class Coord(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Ant(object):
    def __init__(self, coord):
        self.location = coord


class Location(object):
    def __init__(self, x, y, width, height, function):
        self.coord1 = Coord(x, y)
        self.coord2 = Coord(x + width, y + height)
        self.function = function


def update(ants):
    for ant in ants:
        ant.location.x += random.randint(-5, 5)
        ant.location.y += random.randint(-5, 5)


def draw(canvas, ants):
    canvas.delete("all")

    homes = [
        Location(10, 10, 50, 50, "home"),
        Location(950, 600, 50, 50, "home"),
        Location(600, 550, 50, 50, "home"),
    ]

    gathering_spots = [
        Location(10, 600, 50, 50, "gathering"),
        Location(1000, 10, 50, 50, "gathering"),
        Location(600, 550, 50, 50, "gathering"),
        Location(300, 350, 50, 50, "gathering"),
        Location(450, 100, 50, 50, "gathering"),
    ]

    for ant in ants:
        canvas.create_rectangle(
            ant.location.x,
            ant.location.y,
            ant.location.x,
            ant.location.y,
            fill="black",
            outline="black",
            width=1,
        )

    for home in homes:
        canvas.create_rectangle(
            home.coord1.x,
            home.coord1.y,
            home.coord2.x,
            home.coord2.y,
            fill="blue",
            outline="black",
            width=2,
        )

    for gathering in gathering_spots:
        canvas.create_rectangle(
            gathering.coord1.x,
            gathering.coord1.y,
            gathering.coord2.x,
            gathering.coord2.y,
            fill="green",
            outline="black",
            width=2,
        )


def simulate(root, canvas, ants, last_time, debug):
    current_time = time.perf_counter()
    delta_time = current_time - last_time
    last_time = current_time

    if delta_time > 0:
        fps = 1 / delta_time
    else:
        fps = 0

    if debug:
        print("fps:", fps)
    update(ants)
    draw(canvas, ants)
    root.after(30, simulate, root, canvas, ants, last_time, debug)


if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option(
        "-n",
        "--num-ants",
        dest="num_ants",
        type="int",
        default=100000,
        help="number of ants to simulate, max 100000",
    )
    parser.add_option(
        "-f",
        "--full-screen",
        action="store_true",
        dest="full_screen",
        default=False,
        help="print the full screen to see all ants. Warning: Will lag out",
    )
    parser.add_option(
        "-d",
        "--debug",
        action="store_true",
        dest="debug",
        default=False,
        help="print debug output, e.g. fps",
    )

    (options, args) = parser.parse_args()
    num_ants = min(MAX_NUM_ANTS, options.num_ants)
    full_screen = options.full_screen
    debug = options.debug

    # Main Screen
    root = tk.Tk()
    root.title("Ant Simulation")

    canvas = (
        tk.Canvas(
            root, width=FULL_SCREEN_SIZE[0], height=FULL_SCREEN_SIZE[1], bg="white"
        )
        if full_screen
        else tk.Canvas(
            root, width=NORMAL_SCREEN_SIZE[0], height=NORMAL_SCREEN_SIZE[1], bg="white"
        )
    )
    canvas.pack()

    # Make Ants
    ants = []
    for _ in range(num_ants):
        x_coord = random.randint(0, FULL_SCREEN_SIZE[0])
        y_coord = random.randint(0, FULL_SCREEN_SIZE[1])
        ants.append(Ant(Coord(x_coord, y_coord)))

    last_time = time.perf_counter()
    simulate(root, canvas, ants, last_time, debug)
    root.mainloop()
