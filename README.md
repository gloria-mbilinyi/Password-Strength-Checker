
# Password Strength Checker

A Python-based cybersecurity application that evaluates password strength and provides feedback to help users create stronger passwords.

## Features

- Checks password length.
- Detects uppercase letters.
- Detects lowercase letters.
- Checks for numeric digits.
- Detects special characters.
- Displays password strength as Weak, Medium, or Strong.
- Provides security recommendations.
- Includes a graphical user interface (GUI) built with Tkinter.
- Can be packaged as a standalone Windows executable using PyInstaller.

## Technologies Used

- Python
- Tkinter
- Regular Expressions (re)
- PyInstaller

## Password Strength Criteria

The application evaluates passwords using five basic requirements:

1. At least 8 characters.
2. At least one uppercase letter.
3. At least one lowercase letter.
4. At least one number.
5. At least one special character.

## Installation and Usage

### 1. Clone the Repository

```bash
git clone https://github.com/prettyglory/Password-Strength-Checker.git
```

### 2. Navigate to the Project Folder

```bash
cd Password-Strength-Checker
```

### 3. Run the Application

```bash
python password_checker.py
```

## Build a Windows Executable

Install PyInstaller:

```bash
pip install pyinstaller
```

Build the executable:

```bash
pyinstaller --clean --onefile --windowed --name PasswordSecurityChecker password_checker.py
```

The executable will be available inside the `dist` folder.

## Project Purpose

This project demonstrates basic password security assessment using Python. It is designed for educational purposes and encourages users to create stronger passwords.

## Author

**Prettyglory**

GitHub: https://github.com/prettyglory
