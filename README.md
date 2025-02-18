# Tower of Hanoi Game

A graphical implementation of the classic Tower of Hanoi puzzle game using Python and Tkinter.

![Tower of Hanoi Game](screenshot.png)

## Description

The Tower of Hanoi is a classic mathematical puzzle that consists of three rods and a number of disks of different sizes which can slide onto any rod. The puzzle starts with the disks neatly stacked in ascending order of size on one rod, creating a conical shape. The objective is to move the entire stack to another rod, following these rules:

- Only one disk can be moved at a time
- Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack or on an empty rod
- No larger disk may be placed on top of a smaller disk

## Features

- Interactive graphical user interface
- Customizable number of disks (3-8)
- Move counter to track progress
- Auto-solve demonstration
- Visual feedback for selected towers
- Win detection with move count display

## Requirements

- Python 3.x
- Tkinter (usually comes with Python installation)

## How to Run

1. Make sure you have Python installed on your system
2. Clone this repository or download the `tower_of_hanoi.py` file
3. Open a terminal/command prompt
4. Navigate to the game directory
5. Run the game using Python:

```bash
python tower_of_hanoi.py
```

## How to Play

1. Choose the number of disks (3-8) using the spinbox
2. Click "New Game" to start
3. Click on a tower to select it (source)
4. Click on another tower to move the top disk (destination)
5. Try to move all disks to the rightmost tower
6. Use "Show Solution" to see the automatic solution

## Controls

- Left mouse click: Select/deselect towers and move disks
- Number spinbox: Select number of disks (3-8)
- New Game button: Start a new game with selected number of disks
- Show Solution button: Demonstrate the solution automatically

## Tips

- The minimum number of moves required to solve the puzzle is 2^n - 1, where n is the number of disks
- Start with 3 disks to learn the basic strategy
- The game prevents illegal moves automatically
- The status bar shows the current number of moves and selected tower

## Contributing

Feel free to fork this repository and submit pull requests for any improvements you'd like to make.

## License

This project is open source and available under the MIT License.