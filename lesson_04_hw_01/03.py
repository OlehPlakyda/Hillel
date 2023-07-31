def cone_square_and_volume(radius, height):  # returns 2 floats
    v = 1/3 * 3.14 * radius**2 * height
    s = 3.14 * radius * (radius**2 + height**2)**0.5 + 3.14 * radius**2
    return s, v


radius = int(input('Enter the radius of the cone: '))
height = int(input('Enter the height of the cone: '))
result = cone_square_and_volume(radius, height)
print('square of cone =', result[0], '\nvolume of cone =', result[1])
