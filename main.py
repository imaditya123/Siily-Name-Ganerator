from func_tools import PoorManBarChart, PigLatin, SillyNameGenerator


def main():
    """Main function to select and play the desired game."""
    print("Welcome! Select the game you want to play:")
    print("1. Pig Latin")
    print("2. Poor Man's Bar Chart")
    print("3. Silly Name Generator\n")

    try:
        user_input = int(input("Enter your choice (1, 2, or 3): "))
        
        if user_input == 1:
            PigLatin.play()
        elif user_input == 2:
            PoorManBarChart.play()
        elif user_input == 3:
            SillyNameGenerator.play()
        else:
            print("Invalid choice. Please run the program again and select a valid option.")
    except ValueError:
        print("Invalid input. Please enter a number (1, 2, or 3).")


if __name__ == "__main__":
    main()
