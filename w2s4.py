"""
shape = (input("Enter shape (circle, square, triangle, rectangle): ")).lower()

match shape:
    case "circle":
        radius = float(input("Enter radius: "))
        area = 3.14159 * radius * radius
        print("Area of circle:", area)

    case "square":
        side = float(input("Enter side length: "))
        area = side * side
        print("Area of square:", area)

    case "triangle":
        base = float(input("Enter base: "))
        height = float(input("Enter height: "))
        area = 0.5 * base * height
        print("Area of triangle:", area)

    case "rectangle":
        length = float(input("Enter length: "))
        width = float(input("Enter width: "))
        area = length * width
        print("Area of rectangle:", area)

    case _:
       print("Invalid shape")
"""
"""
#8Drink Order system
drink=(input("choose drink")).lower()
match drink:
    case"coffe":
        print("price is £2.50")
    case "tea":
        print("price is £1.80")
    case _:
        print("price is £00.00")
"""
