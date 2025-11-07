import math
import threading
import time
import os
from threading import Thread
from random import randint

# =========================
# Mensuration Calculations
# =========================
def mensuration_calculations():
    r = 7.5
    l, b, h = 12, 8, 5
    a = 6

    area_circle = math.pi * r ** 2
    peri_circle = 2 * math.pi * r
    area_rect = l * b
    peri_rect = 2 * (l + b)
    area_square = a ** 2
    peri_square = 4 * a
    area_triangle = 0.5 * b * h

    sa_cube = 6 * a ** 2
    vol_cube = a ** 3
    sa_cuboid = 2 * (l*b + b*h + h*l)
    vol_cuboid = l * b * h
    sa_cylinder = 2 * math.pi * r * (r + h)
    vol_cylinder = math.pi * r ** 2 * h

    total = (
        area_circle + peri_circle + area_rect + peri_rect +
        area_square + peri_square + area_triangle +
        sa_cube + vol_cube + sa_cuboid + vol_cuboid +
        sa_cylinder + vol_cylinder
    )

    return total


# Lock Definition
threadLock = threading.Lock()

class MyThreadClass(Thread):
    def __init__(self, name, duration):
        Thread.__init__(self)
        self.name = name
        self.duration = duration

    def run(self):
        # Perform mensuration calculation
        result = mensuration_calculations()

        # Acquire the Lock for printing
        threadLock.acquire()
        print(f"---> {self.name} running, Process ID: {os.getpid()}")
        print(f"Calculation Result = {result:.2f}")
        threadLock.release()

        time.sleep(self.duration)

        # Acquire lock again for finish message
        threadLock.acquire()
        print(f"---> {self.name} Finished\n")
        threadLock.release()


def main():
    start_time = time.time()

    # Creating Threads
    threads = []
    for i in range(1, 10):
        t = MyThreadClass(f"Thread#{i}", randint(1, 5))
        threads.append(t)

    # Starting Threads
    for t in threads:
        t.start()

    # Joining Threads
    for t in threads:
        t.join()

    print("End")
    print(f"--- {time.time() - start_time} seconds ---")


if __name__ == "__main__":
    main()
