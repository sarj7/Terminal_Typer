# Terminal Typer: Typing Practice Application

## Overview

Terminal Typer is a command-line application designed to help you improve your typing speed and accuracy. It uses the Gemini API to generate random paragraphs based on a prompt you provide, allowing you to practice typing in a fun and engaging way. The application tracks your typing speed, accuracy, and common mistakes, providing valuable feedback to help you improve.

## Features

-   **AI-Powered Text Generation:** Uses the Gemini API to generate unique and relevant typing practice text based on your prompts.
-   **Real-Time Feedback:** Provides immediate visual feedback on your typing accuracy, highlighting errors as you type.
-   **Performance Metrics:** Tracks and displays key typing metrics such as Words Per Minute (WPM), accuracy, and common errors.
-   **Continuous Practice:** Allows you to practice with the same text or generate new text with different prompts for continuous improvement.

## Prerequisites

Before you begin, ensure you have the following:

-   **Python 3.6 or higher:** You can download Python from the [official Python website](https://www.python.org/downloads/).
-   **Gemini API Key:** You'll need a valid API key from Google's Gemini API to generate text. You can obtain one by signing up on the [Google AI Studio website](https://makersuite.google.com/).

## Installation

### Quick Installation Guide

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/sarj7/Terminal_Typer.git
    cd Terminal_Typer
    ```

2.  **Create and Activate a Virtual Environment:**
    ```bash
    python3 -m venv env_typer
    source env_typer/bin/activate  # On Linux/macOS
    env_typer\Scripts\activate  # On Windows
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

### Platform-Specific Installation Instructions

#### macOS

1. **Install Python (if not already installed):**
   ```bash
   # Using Homebrew
   brew install python

   # Or download from https://www.python.org/downloads/macos/
   ```

2. **Clone the Repository:**
   ```bash
   git clone https://github.com/sarj7/Terminal_Typer.git
   cd Terminal_Typer
   ```

3. **Create and Activate a Virtual Environment:**
   ```bash
   python3 -m venv env_typer
   source env_typer/bin/activate
   ```

4. **Install Dependencies:**
   ```bash
   pip3 install -r requirements.txt
   ```

5. **Run the Application:**
   ```bash
   python3 src/main.py
   ```

#### Linux

1. **Install Python (if not already installed):**
   ```bash
   # Ubuntu/Debian
   sudo apt update
   sudo apt install python3 python3-pip python3-venv

   # Fedora
   sudo dnf install python3 python3-pip

   # Arch Linux
   sudo pacman -S python python-pip
   ```

2. **Clone the Repository:**
   ```bash
   git clone https://github.com/sarj7/Terminal_Typer.git
   cd Terminal_Typer
   ```

3. **Create and Activate a Virtual Environment:**
   ```bash
   python3 -m venv env_typer
   source env_typer/bin/activate
   ```

4. **Install Dependencies:**
   ```bash
   pip3 install -r requirements.txt
   ```

5. **Run the Application:**
   ```bash
   python3 src/main.py
   ```

#### Windows

1. **Install Python:**
   - Download Python from the [official website](https://www.python.org/downloads/windows/)
   - During installation, check "Add Python to PATH"
   - Verify installation by opening Command Prompt and running `python --version`

2. **Clone the Repository:**
   ```cmd
   git clone https://github.com/sarj7/Terminal_Typer.git
   cd Terminal_Typer
   ```

3. **Create and Activate a Virtual Environment:**
   ```cmd
   python -m venv env_typer
   env_typer\Scripts\activate
   ```

4. **Install Dependencies:**
   ```cmd
   pip install -r requirements.txt
   ```

5. **Run the Application:**
   ```cmd
   python src\main.py
   ```

### Detailed Installation Guide

1.  **Clone the Repository:**

    Open your terminal (or command prompt on Windows) and clone the repository to your local machine using Git:

    ```bash
    git clone https://github.com/sarj7/Terminal_Typer.git
    cd Terminal_Typer
    ```

   This command downloads the project files to your computer.

2.  **Create a Virtual Environment:**

    A virtual environment is an isolated space for your project's dependencies. This prevents conflicts with other Python projects on your system.

    -   **On Linux/macOS:**

        Run the following command to create a virtual environment named `env_typer`:

        ```bash
        python3 -m venv env_typer
        ```

    -   **On Windows:**

        Run the following command to create a virtual environment named `env_typer`:

        ```bash
        python -m venv env_typer
        ```

    This command creates a new directory named `env_typer` that contains the virtual environment.

3.  **Activate the Virtual Environment:**

    Before installing dependencies, you need to activate the virtual environment.

    -   **On Linux/macOS:**

        Run the following command to activate the virtual environment:

        ```bash
        source env_typer/bin/activate
        ```

        Your terminal prompt will change to indicate that the virtual environment is active (e.g., `(env_typer) $`).

    -   **On Windows:**

        Run the following command to activate the virtual environment:

        ```bash
        env_typer\Scripts\activate
        ```

        Your command prompt will change to indicate that the virtual environment is active (e.g., `(env_typer) >`).

4.  **Install Dependencies:**

    Now that the virtual environment is active, you can install the required Python packages using pip. Navigate to the project directory (if you're not already there) and run the following command:

    ```bash
    pip install -r requirements.txt
    ```

    This command reads the `requirements.txt` file and installs all the necessary libraries, including the Gemini API client.

## Configuration

1.  **Set Up Your Gemini API Key:**

    When you run the application for the first time, it will prompt you to enter your Gemini API key. This key is used to authenticate with the Gemini API and generate typing practice text.

    ```bash
    python src/main.py
    ```

    The application will ask for your API key:

    ```
    Please enter your Gemini API key:
    ```

    Enter your API key, and the application will save it securely on your local machine for future use.

## Usage

1.  **Run the Application:**

    To start the Terminal Typer application, run the `main.py` script:

    **macOS/Linux:**
    ```bash
    python3 src/main.py
    ```

    **Windows:**
    ```cmd
    python src\main.py
    ```

2.  **Enter a Prompt:**

    The application will prompt you to enter a prompt for text generation. This prompt is used to generate relevant typing practice text.

    ```
    Enter a prompt for text generation:
    ```

    For example, you can enter "a short story about a cat" or "a technical description of blockchain technology."

3.  **Start Typing:**

    Once you enter a prompt, the application will generate a paragraph of text and display it on the screen. Start typing the text as accurately as possible. The application will highlight errors in real-time, showing correct characters in green and incorrect characters in red.

    ```
    Type the following text:
    --------------------------------------------------------------------------------
    [Generated text based on your prompt]
    --------------------------------------------------------------------------------
    Progress: 0% | Press ESC to finish
    ```

4.  **Typing Feedback:**

    As you type, the application provides real-time feedback:

    -   **Green:** Indicates a correctly typed character.
    -   **Red:** Indicates an incorrectly typed character.
    -   **Underlined:** Shows the current character you should be typing.

5.  **Complete the Session:**

    Continue typing until you have completed the entire paragraph or press the `ESC` key to finish the session prematurely.

6.  **View Performance Metrics:**

    After completing the session, the application will display your typing performance metrics, including:

    -   **Words Per Minute (WPM):** Your typing speed.
    -   **Accuracy:** The percentage of characters you typed correctly.
    -   **Time Taken:** The duration of the typing session.
    -   **Characters Typed:** The number of characters you typed.
    -   **Correct Characters:** The number of characters you typed correctly.
    -   **Errors:** The number of typing errors you made.
    -   **Most Common Errors:** The most frequent typing mistakes you made during the session.

    ```
    Typing session completed!

    --- Performance Metrics ---
    Words Per Minute (WPM): 45.67
    Accuracy: 98.5%
    Time Taken: 60.0 seconds
    Characters Typed: 300/300
    Correct Characters: 295
    Errors: 5

    Most Common Errors:
      'e': 2 times
      'a': 1 times
    ```

7.  **Practice Again:**

    After viewing your performance metrics, the application will ask if you want to practice again with the same text or generate new text with a different prompt.

    ```
    ----------------------------------------
    Would you like to try the same text again? (y/n):
    ```

    -   Enter `y` to practice with the same text again.
    -   Enter `n` to generate new text with a different prompt or exit the application.

    If you choose to generate new text, the application will ask:

    ```
    Would you like to practice with new text? (y/n):
    ```

    -   Enter `y` to enter a new prompt and generate new text.
    -   Enter `n` to exit the application.

## Troubleshooting

### Common Issues by Platform

#### Windows
- **Terminal colors not displaying correctly**: Make sure you're using Windows Terminal, PowerShell, or a terminal that supports ANSI color codes.
- **Permission errors**: Try running Command Prompt or PowerShell as Administrator.
- **Keyboard input issues**: If certain key combinations don't work, try running in Windows Terminal instead of cmd.exe.

#### macOS
- **Permission denied during installation**: Use `sudo pip3 install -r requirements.txt` if needed.
- **Terminal compatibility**: The application works best with Terminal.app or iTerm2.
- **Python version conflict**: Use `python3` explicitly rather than `python` which might be linked to Python 2 on older macOS versions.

#### Linux
- **Missing dependencies**: If you encounter errors about missing packages, install them using your distribution's package manager.
- **Display issues**: Make sure your terminal supports ANSI colors and Unicode characters.
- **Virtual environment activation fails**: Check that your shell is compatible with the activation script.

## Example

Here's an example of how to use the Terminal Typer application:

1.  Run the application:

    ```bash
    python src/main.py
    ```

2.  Enter a prompt:

    ```
    Enter a prompt for text generation: the benefits of meditation
    ```

3.  Start typing the generated text:

    ```
    Type the following text:
    --------------------------------------------------------------------------------
    Meditation offers numerous benefits for both mental and physical well-being. Regular
    practice can reduce stress, improve focus, and enhance emotional stability.
    --------------------------------------------------------------------------------
    Progress: 0% | Press ESC to finish
    ```

4.  Complete the session and view your metrics:

    ```
    Typing session completed!

    --- Performance Metrics ---
    Words Per Minute (WPM): 50.23
    Accuracy: 99.2%
    Time Taken: 60.0 seconds
    Characters Typed: 320/320
    Correct Characters: 318
    Errors: 2

    Most Common Errors:
      'e': 1 times
      't': 1 times

    ----------------------------------------
    Would you like to try the same text again? (y/n): n
    Would you like to practice with new text? (y/n): y
    Enter a prompt for text generation: the history of the internet
    ```

## Contributing

Contributions are welcome! If you have any ideas for improving the application, feel free to submit a pull request or open an issue on the [GitHub repository](https://github.com/sarj7/Terminal_Typer.git).

## License

This project is licensed under the [MIT License](LICENSE).