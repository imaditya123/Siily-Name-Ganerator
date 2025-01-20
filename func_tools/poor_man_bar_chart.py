import sys
import string
from collections import Counter
class PoorManBarChart:
    """Class to generate a simple bar chart for character frequencies."""

    @staticmethod
    def play(output=sys.stderr):
        """Generate a poor man's bar chart from a user-input sentence."""
        print("Welcome to the Poor Man's Bar Chart Generator!\n", file=output)
        print("Enter a sentence, and I'll generate a bar chart of character frequencies.\n", file=output)

        while True:
            user_input = input("Enter a sentence: ").strip()

            if not user_input:
                print("Invalid input. Please enter a non-empty sentence.\n", file=output)
                continue

            # Remove spaces and convert to lowercase
            sanitized_input = user_input.replace(" ", "").lower()

            # Count character frequencies
            char_counts = Counter(filter(lambda c: c in string.ascii_lowercase, sanitized_input))

            # Display the bar chart
            print("\nCharacter Frequency Bar Chart:\n", file=output)
            for char in sorted(char_counts):
                print(f"{char}: {char * char_counts[char]}", file=output)

            # Check if the user wants to continue
            try_again = input("\nTry another sentence? (Press Enter to continue, or type 'n' to quit): ").strip()
            if try_again.lower() == "n":
                print("\nGoodbye! Thanks for using the Poor Man's Bar Chart Generator!", file=output)
                break
