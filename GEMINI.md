# Project Overview

This project is a Python-based desktop application that serves as a testbed for a "Catch Phrase" style word guessing game. It features a timer that accelerates as it counts down and displays a word for the user to guess.

## Main Technologies

*   **Language:** Python 3
*   **GUI:** Tkinter (via the `tkinter` and `tkinter.ttk` modules)
*   **Data:** Words and categories are loaded from a CSV file.

## Architecture

The project is composed of three main parts:

1.  **`python_testbed.py`**: The main application script. It contains the `TickingTimer` class which encapsulates all the application logic, including state management (idle, running, reset), GUI setup and updates, and event handling (button presses, timer ticks).
2.  **`resources/word_lists.csv`**: A CSV file that acts as the database for words. Each line contains a word and a list of associated categories.
3.  **`helpers/`**: A directory containing utility scripts for data management.
    *   `gen_word_list.py`: Generates the `word_lists.csv` file by selecting random words from a system dictionary and assigning them random categories.
    *   `count_possessive_apostrophes.py`: A data analysis script used to inspect dictionary files.

# Building and Running

## Dependencies

The application uses standard Python libraries (`tkinter`, `random`, `time`, `enum`) and does not require any external packages to be installed.

## Running the Application

To run the application, execute the main script from the root directory:

```bash
python python_testbed.py
```

## Running Helper Scripts

To regenerate the word list, you can run the `gen_word_list.py` script. Note that it expects a dictionary file at `/usr/share/dict/canadian-english`.

```bash
python helpers/gen_word_list.py
```

# Development Conventions

*   **Code Style:** The code generally follows PEP 8 conventions for Python.
*   **Structure:** The application logic is encapsulated within the `TickingTimer` class. Application state is managed cleanly using a `TimerState` Enum.
*   **File Organization:** The project is organized into a main script, a `resources` directory for data, and a `helpers` directory for utility scripts, separating concerns.
