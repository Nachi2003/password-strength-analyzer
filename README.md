# 🛡️ Password Strength Analyzer

A powerful and user-friendly desktop application to analyze password strength in real-time. This tool serves as a defensive security utility, helping users understand the weaknesses in their passwords and learn how to create stronger ones. It features both a Command-Line Interface (CLI) and a Graphical User Interface (GUI).

## ✨ Features

  * **Detailed Strength Analysis:** Provides a comprehensive analysis using Dropbox's `zxcvbn` library, including a score (0-4), estimated crack time, and actionable feedback.
  * **Real-time GUI Feedback:** The graphical interface analyzes passwords and updates a visual strength bar *as you type*.
  * **Visual Strength Bar:** An intuitive, color-coded progress bar gives immediate visual feedback on password strength (Red $\rightarrow$ Orange $\rightarrow$ Yellow $\rightarrow$ Blue $\rightarrow$ Green).
  * **Educational Warnings & Suggestions:** Offers specific warnings (e.g., "This is a top-10 common password") and suggestions (e.g., "Add another word or two").
  * **Versatile CLI Tool:** Includes a feature-rich CLI for terminal users, capable of checking passwords against user-provided personal information (names, dates, pets) to highlight their risks.
  * **Cross-Platform:** Built with Python and Tkinter, it runs on Windows, macOS, and Linux.

## ⚙️ Installation

To get this project running on your local machine, follow these steps.

**1. Prerequisites:**

  * You must have **Python 3.6 or newer** installed.

**2. Get the Project:**

  * Download or clone this repository to your local machine.
    ```bash
    git clone https://github.com/Nachi2003/password-strength-analyzer.git
    cd password-strength-analyzer
    ```

**3. Install Dependencies:**

  * Install the required Python library using pip.
    ```bash
    pip install zxcvbn
    ```

-----

## 🚀 Usage

You can run either the GUI application or the CLI tool.

### 🖥️ GUI Version

For a user-friendly experience, run the GUI application.

1.  Navigate to the project directory in your terminal.
2.  Run the following command:
    ```bash
    python strength_gui.py
    ```
3.  A window will appear. Simply start typing in the password field to see the real-time analysis.

### ⌨️ CLI Version

For terminal power-users, the CLI provides more advanced options.

1.  Navigate to the project directory in your terminal.
2.  **Basic Usage:** Run the script with a password as an argument. **Remember to use quotes\!**
    ```bash
    python strength_analyzer.py "MyP@ssword123!"
    ```
3.  **Advanced Usage (Checking against personal info):**
    Use the `-i` or `--inputs` flag to provide a list of words to check against. This demonstrates how personal information weakens a password.
    ```bash
    python strength_analyzer.py "Fluffy2025!" -i Fluffy 2025 Nachi
    ```

-----

## 📁 Project Structure

```
password-strength-analyzer/
├── strength_analyzer.py   # The Command-Line Interface (CLI) tool
├── strength_gui.py  # The Graphical User Interface (GUI) application
|__ screenshot    
└── README.md              # This file
```

-----

## 🛠️ Technologies Used

  * **Python:** The core programming language.
  * **Tkinter:** For building the graphical user interface.
  * **zxcvbn:** The password strength estimation library.
  * **argparse:** For parsing command-line arguments in the CLI tool.

-----

## 🙏 Acknowledgments

  * This tool is powered by the excellent **zxcvbn** library created by the team at Dropbox.
