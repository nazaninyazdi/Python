def circle_info(radius):
    if radius <= 0:
        return None

    p = 3.14
    area = p * radius ** 2
    perimeter = 2 * p * radius

    return area, perimeter


print(circle_info(5))
print(circle_info(0))
print(circle_info(-2))