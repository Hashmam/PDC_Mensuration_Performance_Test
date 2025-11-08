import math
import multiprocessing
import time

# ------------------- Mensuration Functions -------------------

def perform_mensuration_calculations():
    """
    Perform comprehensive mensuration calculations for various 2D and 3D shapes
    Returns the total computed value
    """
    # Shape parameters
    r = 7.5  # radius
    l, b, h = 12, 8, 5  # length, breadth, height
    a = 6  # side
    
    # 2D Shape Calculations
    area_circle = math.pi * r ** 2
    peri_circle = 2 * math.pi * r
    area_rect = l * b
    peri_rect = 2 * (l + b)
    area_square = a ** 2
    peri_square = 4 * a
    area_triangle = 0.5 * b * h
    
    # 3D Shape Calculations
    sa_cube = 6 * a ** 2
    vol_cube = a ** 3
    sa_cuboid = 2 * (l*b + b*h + h*l)
    vol_cuboid = l * b * h
    sa_cylinder = 2 * math.pi * r * (r + h)
    vol_cylinder = math.pi * r ** 2 * h
    
    # Combine all calculations
    total = (
        area_circle + peri_circle + area_rect + peri_rect +
        area_square + peri_square + area_triangle +
        sa_cube + vol_cube + sa_cuboid + vol_cuboid +
        sa_cylinder + vol_cylinder
    )
    
    # Additional computation to increase CPU load
    for i in range(100):
        total += math.sqrt(total * i + 1)
    
    return total

# ------------------- Multiprocessing Code -------------------

def foo():
    name = multiprocessing.current_process().name
    print("\nStarting:", name)

    # Run mensuration calculation inside each process
    result = perform_mensuration_calculations()
    print(f"Calculation Result in {name}: {result}\n")

    if name == 'background_process':
        for i in range(0,5):
            print(f'---> {i}')
        time.sleep(1)
    else:
        for i in range(5,10):
            print(f'---> {i}')
        time.sleep(1)

    print("Exiting:", name, "\n")

# ------------------- Running Processes -------------------

if __name__ == '__main__':
    background_process = multiprocessing.Process(
        name='background_process',
        target=foo
    )
    background_process.daemon = False

    NO_background_process = multiprocessing.Process(
        name='NO_background_process',
        target=foo
    )
    NO_background_process.daemon = False
    
    background_process.start()
    NO_background_process.start()
