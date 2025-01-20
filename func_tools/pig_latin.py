import sys


class PigLatin:
    """Class to convert words into Pig Latin."""

    @staticmethod
    def play(output=sys.stderr):
        """Convert user-input words into Pig Latin."""
        print("Welcome to the Pig Latin Converter!\n", file=output)
        print("Enter a word, and I'll convert it to Pig Latin for you.\n", file=output)

        while True:
            user_input = input("Enter a word: ").strip()

            # Validate input
            if not user_input.isalpha():
                print(
                    "Invalid input. Please enter a single word containing only alphabetic characters.\n",
                    file=output,
                )
                continue

            # Pig Latin conversion
            if user_input[0].lower() in ("a", "e", "i", "o", "u"):
                new_word = user_input + "way"
            else:
                new_word = user_input[1:] + user_input[0] + "ay"

            print(f"Pig Latin: {new_word}\n", file=output)

            # Check if the user wants to continue
            try_again = input(
                "\nTry another word? (Press Enter to continue, or type 'n' to quit): "
            ).strip()
            if try_again.lower() == "n":
                print("\nGoodbye! Thanks for playing with Pig Latin!", file=output)
                break
