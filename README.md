# Game Selector

This repository contains a Python-based game selector that allows users to choose from three interactive games:

1. **Pig Latin Converter**  
   Convert words or sentences into Pig Latin.

2. **Poor Man's Bar Chart**  
   Generate a simple bar chart to visualize character frequencies in a sentence.

3. **Silly Name Generator**  
   Generate random, funny names just like Sean would pick for Gus (from the show *Psych*).

---

## Getting Started

### Prerequisites
Ensure you have Python 3.7 or above installed on your system.

### Installation
Clone the repository:
```bash
git clone <repository-url>
cd <repository-folder>
```

### Run the Program
Run the main script to start the game selector:
```bash
python main.py
```

---

## Game Descriptions

### 1. Pig Latin Converter
Enter a word or sentence, and it will be converted to Pig Latin:
- If the word starts with a vowel, `way` is added to the end.
- If the word starts with a consonant, the first letter is moved to the end, followed by `ay`.

#### Example:
```plaintext
Input: apple
Output: appleway

Input: banana
Output: ananabay
```

### 2. Poor Man's Bar Chart
Visualize the frequency of characters in a sentence using a simple bar chart made of `*`.

#### Example:
```plaintext
Input: hello world

Character Frequency Bar Chart:
h: h
e: e
l: lll
o: oo
r: r
d: d
w: w
```

### 3. Silly Name Generator
Generate random, funny names using predefined lists of first and last names.

#### Example:
```plaintext
Name is: Chewy Wigglesworth
Name is: Butterbean Vinaigrette
```

---

## How to Play
1. Run `main.py`.
2. Select a game by entering its corresponding number:
   - `1` for Pig Latin Converter
   - `2` for Poor Man's Bar Chart
   - `3` for Silly Name Generator
3. Follow the on-screen instructions for each game.
4. Type `n` when prompted to exit a game.

---

## Folder Structure
```
.
├── func_tools
│   ├── pig_latin.py          # Contains the Pig Latin game logic
│   ├── poor_man_bar_chart.py # Contains the Poor Man's Bar Chart logic
│   ├── silly_name_generator.py # Contains the Silly Name Generator logic
├── main.py                   # Entry point for the game selector
└── README.md                 # Project documentation
```

---

## Contributing
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch-name`).
3. Make your changes and commit them (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch-name`).
5. Open a Pull Request.

---

## License
This project is licensed under the MIT (License)[https://github.com/imaditya123/Silly-Name-Ganerator#:~:text=README-,Apache%2D2.0%20license,-Game%20Selector] - see the LICENSE file for details.

---

## Acknowledgments
Inspired by the TV show *Psych* and simple Python scripting challenges.
