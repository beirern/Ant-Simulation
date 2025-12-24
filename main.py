import random
import time
import tkinter as tk

# Main Screen
root = tk.Tk()
root.title("Ant Simulation")

last_time = time.perf_counter()

canvas = tk.Canvas(root, width=1280, height=720, bg="white")
canvas.pack()

# Make Ants
ants = []
for _ in range(100000):
        x_coord = random.random() * 1280
        y_coord = random.random() * 720
        ants.append([x_coord, y_coord])

def update(ants):
    for ant in ants:
        ant[0] += random.random() * 10 - 5
        ant[1] += random.random() * 10 - 5

def draw(canvas, ants):
    # Homes
    canvas.create_rectangle(
        10,
        10,
        50,
        50,
        fill="blue",  # Fill color
        outline="black", # Outline color
        width=2     # Outline width
    )

    canvas.create_rectangle(
        950,
        600,
        1000,
        650,
        fill="blue",  # Fill color
        outline="black", # Outline color
        width=2     # Outline width
    )

    canvas.create_rectangle(
        600,
        600,
        650,
        550,
        fill="blue",  # Fill color
        outline="black", # Outline color
        width=2     # Outline width
    )

    # Gathering Spots
    canvas.create_rectangle(
        10,
        600,
        50,
        650,
        fill="green",  # Fill color
        outline="black", # Outline color
        width=2     # Outline width
    )

    canvas.create_rectangle(
        1000,
        10,
        1050,
        60,
        fill="green",  # Fill color
        outline="black", # Outline color
        width=2     # Outline width
    )

    canvas.create_rectangle(
        600,
        600,
        650,
        550,
        fill="green",  # Fill color
        outline="black", # Outline color
        width=2     # Outline width
    )

    canvas.create_rectangle(
        300,
        350,
        350,
        400,
        fill="green",  # Fill color
        outline="black", # Outline color
        width=2     # Outline width
    )

    canvas.create_rectangle(
        450,
        100,
        500,
        150,
        fill="green",  # Fill color
        outline="black", # Outline color
        width=2     # Outline width
    )

    for ant in ants:
        canvas.create_rectangle(
            ant[0],
            ant[1],
            ant[0],
            ant[1],
            fill="black", outline="black", width=1
        )

def simulate(root, canvas, ants, last_time):
    current_time = time.perf_counter()
    delta_time = current_time - last_time
    last_time = current_time

    if delta_time > 0:
        fps = 1 / delta_time
    else:
        fps = 0

    print("fps:", fps)
    canvas.delete("all")
    update(ants)
    draw(canvas, ants)
    root.after(30, simulate, root, canvas, ants, last_time)

simulate(root, canvas, ants, last_time)
root.mainloop()