# Square Area and Perimeter Calculator using Functions

def calculate_area(side_length):
    return side_length ** 2


def calculate_perimeter(side_length):
    return 4 * side_length


def get_side_length():
    try:
        side = float(input("Enter the side length of the square: "))
        if side <= 0:
            print("Side length must be positive. Please enter a valid number.")
            return None
        return side
    except ValueError:
        print("Please enter a valid number.")
        return None


def display_results(side_length, area, perimeter):
    print(f"\nFor a square with side length {side_length}:")
    print(f"Area = {area:.2f} square units")
    print(f"Perimeter = {perimeter:.2f} units")


def main():

    side_length = get_side_length()

    if side_length is not None:
        area = calculate_area(side_length)
        perimeter = calculate_perimeter(side_length)
        display_results(side_length, area, perimeter)


# Run the program
if __name__ == "__main__":
    main()