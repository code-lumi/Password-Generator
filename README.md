# Secure Random Password Generator 🔒

A lightweight, customizable command-line password generator built with Python. It allows users to define custom length and character criteria, guarantees the inclusion of selected character types, evaluates password strength, and features an interactive loop for multiple generations.

---

## 🚀 Features

* **Customizable Length:** Set your desired password length (minimum 6 characters recommended for security).
* **Character Set Selection:** Choose whether to include Uppercase letters (`A-Z`), Lowercase letters (`a-z`), Numbers (`0-9`), and Special Symbols (`!@#$%^&*...`).
* **Guaranteed Inclusion:** Ensures that at least one character from each selected set is included in the final password.
* **Randomized Positioning:** Shuffles characters to prevent predictable patterns (e.g., symbols always appearing at the end).
* **Strength Evaluator:** Analyzes the generated password based on length and variety to provide a real-time rating (Strong, Moderate, Weak).
* **Interactive Loop:** Generates multiple passwords seamlessly without needing to restart the script.

---

## 📋 Prerequisites

Make sure you have **Python 3.x** installed on your system. You can check your Python version by running:

```bash
python --version