# Terminal Typer: Practice typing in terminal

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

### Platform-Specific instruction

#### macOS
- Install Python with `brew install python` if needed
- Use `python3` and `pip3` for all commands
- Run with `python3 src/main.py`

#### Linux
- Install Python with your distro's package manager (e.g., `sudo apt install python3 python3-pip python3-venv`)
- Run with `python3 src/main.py`

#### Windows
- During Python installation, check "Add Python to PATH"
- Run with `python src\main.py`
- Use Windows Terminal or PowerShell for best results

## Configuration

When you run the application for the first time, it will prompt you to enter your Gemini API key:

```
Please enter your Gemini API key:
```

Enter your key, and the application will save it securely for future use.

## Usage

1.  **Run the Application:**
    ```bash
    python3 src/main.py  # On macOS/Linux
    python src\main.py   # On Windows
    ```

2.  **Enter a Prompt:**
    When prompted, enter a topic for text generation (e.g., "a short story about a cat").

3.  **Start Typing:**
    Type the generated text. The application provides real-time feedback:
    - **Green:** Correctly typed characters
    - **Red:** Incorrectly typed characters
    - **Underlined:** Current character to type
    - Press **ESC** to finish early

4.  **View Performance Metrics:**
    After completing the session, you'll see your:
    - Words Per Minute (WPM)
    - Accuracy percentage
    - Time taken
    - Character counts and errors
    - Most common mistakes

5.  **Practice Again:**
    Choose to retry the same text or generate new text with a different prompt.

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

Here's a quick example of using Terminal Typer:

1. Run the application and enter a prompt:
   ```
   Enter a prompt for text generation: the benefits of meditation
   ```

2. Type the generated text, then view your metrics:
   ```
   --- Performance Metrics ---
   Words Per Minute (WPM): 50.23
   Accuracy: 99.2%
   Time Taken: 60.0 seconds
   Characters Typed: 320/320
   Correct Characters: 318
   Errors: 2
   ```

3. Choose to try again or practice with new text.

## Contributing

Contributions are welcome! If you have any ideas for improving the application, feel free to submit a pull request or open an issue on the [GitHub repository](https://github.com/sarj7/Terminal_Typer.git).

## License

This project is licensed under the [MIT License](LICENSE).