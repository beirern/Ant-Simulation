import random
import time
import tkinter as tk
from optparse import OptionParser

MAX_NUM_ANTS = 100000
FULL_SCREEN_SIZE = (1280, 720)
NORMAL_SCREEN_SIZE = (320, 320)


def update(ants):
    for ant in ants:
        ant[0] += random.randint(-5, 5)
        ant[1] += random.randint(-5, 5)


def draw(canvas, ants):
    canvas.delete("all")

    # Homes
    canvas.create_rectangle(
        10,
        10,
        50,
        50,
        fill="blue",  # Fill color
        outline="black",  # Outline color
        width=2,  # Outline width
    )

    canvas.create_rectangle(
        950,
        600,
        1000,
        650,
        fill="blue",  # Fill color
        outline="black",  # Outline color
        width=2,  # Outline width
    )

    canvas.create_rectangle(
        600,
        600,
        650,
        550,
        fill="blue",  # Fill color
        outline="black",  # Outline color
        width=2,  # Outline width
    )

    # Gathering Spots
    canvas.create_rectangle(
        10,
        600,
        50,
        650,
        fill="green",  # Fill color
        outline="black",  # Outline color
        width=2,  # Outline width
    )

    canvas.create_rectangle(
        1000,
        10,
        1050,
        60,
        fill="green",  # Fill color
        outline="black",  # Outline color
        width=2,  # Outline width
    )

    canvas.create_rectangle(
        600,
        600,
        650,
        550,
        fill="green",  # Fill color
        outline="black",  # Outline color
        width=2,  # Outline width
    )

    canvas.create_rectangle(
        300,
        350,
        350,
        400,
        fill="green",  # Fill color
        outline="black",  # Outline color
        width=2,  # Outline width
    )

    canvas.create_rectangle(
        450,
        100,
        500,
        150,
        fill="green",  # Fill color
        outline="black",  # Outline color
        width=2,  # Outline width
    )

    for ant in ants:
        canvas.create_rectangle(
            ant[0], ant[1], ant[0], ant[1], fill="black", outline="black", width=1
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
        ants.append([x_coord, y_coord])

    last_time = time.perf_counter()
    simulate(root, canvas, ants, last_time, debug)
    root.mainloop()
