# Character Case Checker using Functions

def get_character_input():
    while True:
        char = input("Enter a single character: ")
        if len(char) == 1:
            return char
        else:
            print("Please enter only one character.")


def is_uppercase(char):
    return char.isupper()

def is_lowercase(char):
    return char.islower()

def is_letter(char):
    return char.isalpha()



def determine_case(char):
    if not is_letter(char):
        return "not a letter"
    elif is_uppercase(char):
        return "uppercase"
    elif is_lowercase(char):
        return "lowercase"


def display_result(char, case_type):
    if case_type == "not a letter":
        print(f"'{char}' is not a letter.")
    else:
        print(f"The character '{char}' is {case_type}.")


def main():
    print("Character Case Checker")

    # Get character input
    character = get_character_input()

    # Determine the case
    case_result = determine_case(character)

    # Display the result
    display_result(character, case_result)


# Run the program
if __name__ == "__main__":
    main()