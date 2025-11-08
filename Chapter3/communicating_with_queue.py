import math
import multiprocessing
import random
import time

# ----------------- Mensuration Calculations -----------------

def perform_mensuration_calculations():
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

    total = (area_circle + peri_circle + area_rect + peri_rect +
             area_square + peri_square + area_triangle +
             sa_cube + vol_cube + sa_cuboid + vol_cuboid +
             sa_cylinder + vol_cylinder)

    for i in range(100):
        total += math.sqrt(total * i + 1)

    return total

# ----------------- Producer-Consumer Classes -----------------

class producer(multiprocessing.Process):
    def __init__(self, queue):
        multiprocessing.Process.__init__(self)
        self.queue = queue

    def run(self):
        for i in range(10):
            # Instead of random, we now calculate mensuration result
            item = perform_mensuration_calculations()
            self.queue.put(item)
            print(f"Process Producer: Calculated value appended -> {self.name}")
            time.sleep(1)
            print(f"Queue size now: {self.queue.qsize()}")

class consumer(multiprocessing.Process):
    def __init__(self, queue):
        multiprocessing.Process.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            if self.queue.empty():
                print("\nQueue is empty. Consumer stopping...\n")
                break
            else:
                time.sleep(2)
                item = self.queue.get()
                print(f"Process Consumer: Retrieved value = {item:.2f} by {self.name}\n")
                time.sleep(1)

# ----------------- Main Execution -----------------

if __name__ == '__main__':
    queue = multiprocessing.Queue()
    process_producer = producer(queue)
    process_consumer = consumer(queue)

    process_producer.start()
    process_consumer.start()

    process_producer.join()
    process_consumer.join()
