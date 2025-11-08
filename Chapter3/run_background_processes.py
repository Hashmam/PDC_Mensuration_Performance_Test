import math
import multiprocessing
import time

# =====================
# Mensuration Functions
# =====================

def perform_mensuration_calculations():
    """
    Perform comprehensive mensuration calculations for various 2D and 3D shapes
    Returns the total computed value
    """
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
    
    for i in range(100):
        total += math.sqrt(total * i + 1)
    
    return total

def calculate_2d_shapes():
    r = 7.5
    l, b, h = 12, 8, 5
    a = 6
    
    calculations = {
        'circle_area': math.pi * r ** 2,
        'circle_perimeter': 2 * math.pi * r,
        'rectangle_area': l * b,
        'rectangle_perimeter': 2 * (l + b),
        'square_area': a ** 2,
        'square_perimeter': 4 * a,
        'triangle_area': 0.5 * b * h
    }
    
    return calculations

def calculate_3d_shapes():
    r = 7.5
    l, b, h = 12, 8, 5
    a = 6
    
    calculations = {
        'cube_surface_area': 6 * a ** 2,
        'cube_volume': a ** 3,
        'cuboid_surface_area': 2 * (l*b + b*h + h*l),
        'cuboid_volume': l * b * h,
        'cylinder_surface_area': 2 * math.pi * r * (r + h),
        'cylinder_volume': math.pi * r ** 2 * h
    }
    
    return calculations


# =====================
# Multiprocessing Code
# =====================

def foo():
    name = multiprocessing.current_process().name
    print(f"Starting {name}\n")

    # Call mensuration calculations inside process
    total = perform_mensuration_calculations()
    print(f"{name} -> Mensuration Total = {total}\n")

    if name == 'background_process':
        for i in range(0, 5):
            print(f'---> {i}\n')
        time.sleep(1)
    else:
        for i in range(5, 10):
            print(f'---> {i}\n')
        time.sleep(1)
    
    print(f"Exiting {name}\n")


if __name__ == '__main__':
    background_process = multiprocessing.Process(
        name='background_process',
        target=foo
    )
    background_process.daemon = True

    NO_background_process = multiprocessing.Process(
        name='NO_background_process',
        target=foo
    )
    NO_background_process.daemon = False
    
    background_process.start()
    NO_background_process.start()
