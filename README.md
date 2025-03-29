# Terminal Typer: Practice typing in terminal

## Overview

Terminal Typer is a command-line application designed to help you improve your typing speed and accuracy. It uses Google's Gemini API to generate random paragraphs based on a prompt you provide, allowing you to practice typing in a fun and engaging way. The application tracks your typing speed, accuracy, and common mistakes, providing valuable feedback to help you improve. With features like real-time color-coded feedback and look-ahead word hiding, Terminal Typer offers a uniquely challenging typing practice environment right in your terminal.

## Features

### AI-Powered Text Generation
Terminal Typer leverages Google's Gemini API to generate unique, relevant, and varied typing practice material based on your prompts. Whether you want to practice typing technical jargon, creative stories, or educational content, simply provide a topic and start typing.

### Look-Ahead Training System
The application's innovative look-ahead training feature hides upcoming words as you type, encouraging you to read ahead and develop a smoother typing rhythm. You can customize how many words ahead are hidden based on your skill level.


### Comprehensive Performance Metrics
After each typing session, Terminal Typer provides detailed performance statistics:
- Words Per Minute (WPM)
- Typing accuracy percentage
- Total time spent typing
- Character counts (correct vs. incorrect)
- Analysis of your most common typing errors

### Flexible Practice Options
Choose to retry the same text to perfect your speed and accuracy or generate new content with different prompts for varied practice sessions.


## Why Look-Ahead Training?

The **Look-Ahead Training** feature was introduced to help typists develop a critical skill: reading ahead while typing. Many typists focus solely on the current word, which can slow down their typing speed and disrupt their flow. By hiding the next few words, this feature forces you to anticipate and mentally prepare for upcoming text. This practice improves:

- **Typing Flow:** Encourages smoother transitions between words.
- **Speed:** Reduces pauses caused by reading each word individually.
- **Focus:** Trains your brain to process text in chunks rather than word-by-word.
- **Adaptability:** Prepares you for real-world typing scenarios where reading ahead is essential, such as transcribing or coding.

This feature is especially useful for intermediate and advanced typists looking to push their limits and refine their skills. When you begin typing, all text is visible, but as soon as you complete your first word, the application will hide the specified number of upcoming words, challenging you to remember and anticipate what comes next.

## Prerequisites

Before you begin, ensure you have the following:

- **Python 3.6 or higher:** You can download Python from the [official Python website](https://www.python.org/downloads/).
- **Gemini API Key:** You'll need a valid API key from Google's Gemini API to generate text (see below for detailed instructions on obtaining one).
- **Terminal with ANSI color support:** Most modern terminals support this feature.

## API Keys
- Gemini API key: Free for limited use.

## Obtaining a Gemini API Key

Google's Gemini API offers a free tier that's suitable for personal projects like Terminal Typer. Here's how to get your API key:

1. **Create a Google AI Studio account**:
   - Visit [Google AI Studio](https://makersuite.google.com/)
   - Sign in with your Google account (create one if needed)

2. **Access API key management**:
   - In Google AI Studio, click on your profile icon in the top-right corner
   - Select "Get API key" or go to the API section

3. **Create a new API key**:
   - Click "Create API Key"
   - Give your key a name (e.g., "Terminal Typer")
   - Copy the generated API key to your clipboard

4. **API usage limits**:
   - The free tier currently includes a generous number of API calls per minute and per day
   - Personal projects like Terminal Typer typically stay well within these limits
   - Check the [Google AI Studio documentation](https://ai.google.dev/docs) for the most current information on quotas and limits

5. **Safeguard your API key**:
   - Never share your API key publicly
   - Terminal Typer stores your key locally in a config file

For more detailed information about the Gemini API, including capabilities and limitations, visit the [official Google AI documentation](https://ai.google.dev/docs/gemini_api_overview).

## Installation

### Quick Installation Guide

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/sarj7/Terminal_Typer.git
   cd Terminal_Typer
   ```

2. **Create and Activate a Virtual Environment:**
   ```bash
   python3 -m venv env_typer
   source env_typer/bin/activate  # On Linux/macOS
   env_typer\Scripts\activate  # On Windows
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

### Detailed Platform-Specific Instructions

#### macOS
- Install Python with Homebrew if not already installed: `brew install python`
- Use `python3` and `pip3` for all commands to ensure you're using Python 3
- Install dependencies: `pip3 install -r requirements.txt`
- Run the application: `python3 src/main.py`
- For best results, use Terminal.app or iTerm2

#### Linux
- Install Python and required packages: 
  ```bash
  sudo apt install python3 python3-pip python3-venv  # For Debian/Ubuntu
  # Or use your distribution's package manager
  ```
- Create and activate virtual environment:
  ```bash
  python3 -m venv env_typer
  source env_typer/bin/activate
  ```
- Install dependencies: `pip install -r requirements.txt`
- Run the application: `python3 src/main.py`

#### Windows
- During Python installation, check "Add Python to PATH" to make Python available from Command Prompt
- Open Command Prompt or PowerShell:
  ```
  python -m venv env_typer
  env_typer\Scripts\activate
  pip install -r requirements.txt
  python src\main.py
  ```
- Windows Terminal or PowerShell is recommended for best ANSI color support

## Configuration

When you run the application for the first time, it will prompt you to enter your Gemini API key:

```
Please enter your Gemini API key:
```

Enter the key you obtained from Google AI Studio. The application saves this key in a local configuration file (`config.json`) for future use. If you need to change the API key later, you can either:

1. Edit the `config.json` file directly
2. Delete the file to be prompted for a new key on next launch

## Detailed Usage Guide

### 1. Starting the Application

Launch Terminal Typer from your command line:

```bash
python3 src/main.py  # On macOS/Linux
python src\main.py   # On Windows
```

### 2. Generating Practice Text

When prompted, enter a specific topic or type of text you'd like to practice with:

```
Enter a prompt for text generation: 
```

Example prompts:
- "a paragraph about space exploration"
- "basic programming concepts"
- "a short story with descriptive language"
- "common English idioms and expressions"

The more specific your prompt, the more relevant the generated text will be for your practice needs.

### 3. Configuring Look-Ahead Challenge

Next, you'll be prompted to set the look-ahead difficulty:

```
How many words should be hidden ahead? 
```

Guidelines for different skill levels:
- **Beginners**: Enter 0-1 (no hiding or just one word)
- **Intermediate**: Enter 2-4 words
- **Advanced**: Enter 5-7 words
- **Expert**: Enter 8+ words

The application will initially show all text, but after you type the first word, it will begin hiding the specified number of words ahead of your current position.

### 4. Typing Practice Session

The terminal will display the generated text with the following interactive elements:

- Your current position is underlined
- Characters you've typed correctly appear in green
- Mistakes appear in red
- Words ahead of your current position (based on your setting) appear as underscores

As you type:
- The display updates in real-time (with anti-flicker protection)
- Your cursor automatically advances
- You can press Backspace/Delete to correct mistakes
- Press ESC at any time to end the session early

The screen will automatically scroll to keep your current typing position visible.

### 5. Reviewing Performance Metrics

After completing the typing session (either by typing the entire text or pressing ESC), you'll see detailed performance statistics:

```
--- Performance Metrics ---
Words Per Minute (WPM): 65.42
Accuracy: 97.8%
Time Taken: 45.6 seconds
Characters Typed: 312/320
Correct Characters: 305
Errors: 7

Most Common Errors:
  'e': 3 times
  't': 2 times
  'i': 1 time
  'o': 1 time
```

These metrics help you identify:
- Your typing speed (WPM)
- Overall accuracy
- Which characters you most commonly mistype
- How your performance changes over multiple sessions

### 6. Continuing Your Practice

After each session, you'll be asked if you want to:
1. Retry the same text to improve your performance
2. Generate new text with a different prompt
3. Exit the application

This flexibility allows you to focus on problem areas or continuously challenge yourself with new content.

## Troubleshooting

### Common Issues by Platform

#### Windows
- **Terminal colors not displaying correctly**: Make sure you're using Windows Terminal, PowerShell, or a terminal that supports ANSI color codes.
- **Permission errors**: Try running Command Prompt or PowerShell as Administrator.
- **Keyboard input issues**: If certain key combinations don't work, try running in Windows Terminal instead of cmd.exe.
- **ModuleNotFoundError**: Ensure you've installed all dependencies with `pip install -r requirements.txt` while your virtual environment is activated.

#### macOS
- **Permission denied during installation**: Use `sudo pip3 install -r requirements.txt` if needed.
- **Terminal compatibility**: The application works best with Terminal.app or iTerm2.
- **Python version conflict**: Use `python3` explicitly rather than `python` which might be linked to Python 2 on older macOS versions.
- **API key issues**: If your API key isn't being saved, check file permissions in your project directory.

#### Linux
- **Missing dependencies**: If you encounter errors about missing packages, install them using your distribution's package manager.
- **Display issues**: Make sure your terminal supports ANSI colors and Unicode characters.
- **Virtual environment activation fails**: Check that your shell is compatible with the activation script.
- **Terminal size detection problems**: Try manually resizing your terminal if the text display seems misaligned.

### API-Related Issues

- **Invalid API key error**: Double-check that you've correctly copied your Gemini API key.
- **API quota exceeded**: If you receive quota errors, you may have exceeded the free tier limits. Wait a while or check your usage in the Google AI Studio dashboard.
- **Slow text generation**: Network issues might cause delays. The application will eventually time out and provide a fallback text for practice.
- **Empty or irrelevant responses**: Try providing more specific prompts or check your API key permissions.

## Example Usage

Here's a detailed example of using Terminal Typer:

1. Run the application:
   ```
   $ python3 src/main.py
   ```

2. Enter your Gemini API key (first run only):
   ```
   Please enter your Gemini API key: AIza...
   ```

3. Enter a prompt for text generation:
   ```
   Enter a prompt for text generation: the science behind effective learning techniques
   Contacting Gemini API at: https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent
   Response structure preview: ['candidates', 'promptFeedback']
   ```

4. Configure the look-ahead challenge:
   ```
   How many words should be hidden ahead? 3
   ```

5. Type the generated text, seeing your progress with color-coded feedback and hidden upcoming words.

6. View your detailed performance metrics after completion:
   ```
   --- Performance Metrics ---
   Words Per Minute (WPM): 50.23
   Accuracy: 99.2%
   Time Taken: 60.0 seconds
   Characters Typed: 320/320
   Correct Characters: 318
   Errors: 2
   
   Most Common Errors:
     'r': 1 times
     't': 1 times
   ```

7. Choose to continue practicing:
   ```
   Would you like to try the same text again? (y/n): n
   Would you like to practice with new text? (y/n): y
   ```

8. Return to step 3 for a new practice session or exit the application.

## Advanced Usage Tips

- **Practice targeted skills**: Use specific prompts to generate text with terms relevant to your profession or interests.
- **Build speed gradually**: Start with a lower word-hiding count and increase it as you become more comfortable.
- **Focus on problem characters**: If your metrics show you consistently mistype certain characters, use prompts that will include those characters more frequently.
- **Regular short sessions**: Multiple short sessions (5-10 minutes) are often more effective than one long session for building typing skills.
- **Track progress over time**: Pay attention to your WPM and accuracy metrics to see your improvement over multiple sessions.

## Contributing

Contributions to Terminal Typer are welcome! If you have any ideas for improving the application, feel free to:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

Areas where contributions would be particularly valuable include:
- Additional performance metrics
- Support for typing practice with code snippets
- Multi-language support
- Custom theming options
- Historical performance tracking

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- Terminal Typer uses Google's Gemini API for text generation
- Thanks to all contributors who have helped improve this application
- Inspired by typing tutors like TypeRacer, Monkeytype, and others