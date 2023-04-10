
length = int(input("Enter an integer for the rectangle's length:"))
width = int(input("Enter an integer for the rectangle's width:"))
height = int(input("Enter an integer for the rectangle's height:"))
def rect_area(length, width, height):
    area = (length * width * height)
    return area
def rect_solid_area(length, width, height):
    solid_area = ((rect_area(length, width, 1) * 2) + (rect_area(length, 1, height) * 2) +
                  (rect_area(1, width, height) * 2))
    return print(solid_area)


rect_solid_area(length, width, height)

