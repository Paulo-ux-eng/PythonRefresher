# Python program to input 5 values and calculate their average

def main():
    # Initialize empty array to store values
    values = []

    print("Enter 5 values:")

    # Use loop to get 5 values from user
    for i in range(5):
        while True:
            try:
                value = float(input(f"Enter value {i + 1}: "))
                values.append(value)
                break
            except ValueError:
                print("Please enter a valid number.")

    # Calculate the average
    total = sum(values)
    average = total / len(values)

    # Display the results
    print(f"\nValues entered: {values}")
    print(f"Sum of values: {total}")
    print(f"Average: {average:.2f}")


# Run the program
if __name__ == "__main__":
    main()