# Days to Seconds Calculator

def days_to_seconds():
    try:
        # Ask user for number of days
        days = float(input("Enter the number of days: "))

        # Calculate seconds (days * 24 hours * 60 minutes * 60 seconds)
        seconds = days * 24 * 60 * 60

        # Print the result
        print(f"{days} days equals {seconds:,.0f} seconds")

    except ValueError:
        print("Please enter a valid number.")


# Run the program
if __name__ == "__main__":
    days_to_seconds()