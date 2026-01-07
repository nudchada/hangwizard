# HangWizard 🧙‍♂️

![Language](https://img.shields.io/badge/Language-Python-blue)
![Course](https://img.shields.io/badge/Course-CS50P-red)
![Status](https://img.shields.io/badge/Status-Completed-success)

**HangWizard** is a command-line Hangman game inspired by the Wizarding World of Harry Potter. This project was developed as the **Final Project for CS50's Introduction to Programming with Python (CS50P)**.

The game challenges players to guess names of wizards, witches, and magical creatures using a dataset fetched from a public API and processed for offline gameplay.

## 📂 Project Structure

* `main.py`: The main entry point for the game logic, user input handling, and rendering.
* `characters.py`: A utility script used to **fetch, clean, and cache** data from the external API.
* `HP_characters.txt`: Local database file containing cleaned names. This allows the game to run offline without hitting the API repeatedly.
* `requirements.txt`: Project dependencies.

## 🚀 Features

* **Smart Data Caching:** The project fetches data from the API once and stores it locally (`HP_characters.txt`). This approach minimizes API usage and allows for offline gameplay.
* **Input Validation:** Handles case-insensitive inputs and validates non-numeric guesses.
* **Dynamic Masking:** Automatically reveals special characters (spaces, hyphens) to improve user experience (e.g., `_ _ _ _ _ _` for "Harry Potter" becomes `_ _ _ _ _   _ _ _ _ _ _`).
* **Visual Progression:** Displays ASCII art updates as the game progresses.

## 🛠️ Installation & Usage

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/nudchada/hangwizard.git
    cd hangwizard
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the Game:**
    ```bash
    python main.py
    ```

### ℹ️ Note on Data Fetching
The file `characters.py` contains the logic to fetch data from the `dedolist.com` API.
* **By default, the fetching code is commented out** to preserve the existing curated list in `HP_characters.txt` and avoid unnecessary network requests.
* If you wish to update the dataset, uncomment the API request block in `characters.py` and run it once:
    ```bash
    python characters.py
    ```

## 🧠 Design Choices

### API vs. Local Storage
Instead of fetching data from the API every time the game starts (which requires internet access and increases latency), I implemented a **one-time data ingestion strategy**:
1.  `characters.py` connects to the API and parses the JSON response.
2.  It extracts relevant names and writes them to a text file.
3.  `main.py` simply reads from this text file.

This design ensures the game is **robust, fast, and offline-capable**, mimicking how real-world applications cache static data.
