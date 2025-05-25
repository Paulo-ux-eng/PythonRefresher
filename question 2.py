# Sphere Volume Calculator
import math


def calculate_sphere_volume():
    try:
        # Ask user for radius
        radius = float(input("Enter the radius of the sphere: "))

        # Check for valid radius (must be positive)
        if radius < 0:
            print("Radius cannot be negative. Please enter a positive number.")
            return

        # Calculate volume using formula: V = (4/3) * π * r³
        # Using ** operator for r³ (r cubed)
        volume = (4 / 3) * math.pi * (radius ** 3)

        # Print the result
        print(f"The volume of a sphere with radius {radius} is {volume:.2f} cubic units")

    except ValueError:
        print("Please enter a valid number.")


# Run the program
if __name__ == "__main__":
    calculate_sphere_volume()