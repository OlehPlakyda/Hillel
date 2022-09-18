def cone_square_and_volume(radius, height):  # returns 2 floats
    global s, v
    v = 1/3 * 3.14 * radius**2 * height
    s = 3.14 * radius * (radius**2 + height**2)**0.5 + 3.14 * radius**2


s, v = 0, 0
radius = int(input('Enter the radius of the cone: '))
height = int(input('Enter the height of the cone: '))
cone_square_and_volume(radius, height)
print('square of cone =', s, '\nvolume of cone =', v)
