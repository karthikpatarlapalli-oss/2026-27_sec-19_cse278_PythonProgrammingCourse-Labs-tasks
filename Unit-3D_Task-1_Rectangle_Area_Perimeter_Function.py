def rectangle_area_perimeter(l,b):
    a = l * b
    p = 2 *(l + b)
    return a,p

length = 6
breadth = 5
area, perimeter = rectangle_area_perimeter(length , breadth)
print("Area:",area)
print("Perimeter:",perimeter)