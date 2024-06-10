# Voice Assistant Prototype

## Overview

This project is a basic Voice Assistant (prototype) developed using Python. It is designed to perform simple tasks based on voice commands. The assistant can interact with the user through speech, perform web searches, open applications, and provide information using Wikipedia. It utilizes various Python packages to achieve these functionalities.

**Note**: This is a prototype version and is not intended to handle advanced tasks or complex interactions.

## Features

- Voice recognition to accept user commands.
- Text-to-speech functionality to provide voice responses.
- Perform web searches using the default browser.
- Open and interact with basic applications.
- Fetch information from Wikipedia.
- Display current date and time.

## Required Packages

To run this project, you need to install the following Python packages:

```python
import sys
import webbrowser
import pyautogui
import speech_recognition as sr
import os
import webbrowser as wb
import datetime
import wikipedia
import pyttsx3
import time
import random
import ctypes
import distutils
```

## Installation

1. Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
2. Install the required packages using `pip`:

    ```bash
    pip install pyautogui speechrecognition wikipedia pyttsx3
    ```

3. Clone this repository or download the source code.

    ```bash
    git clone https://github.com/vjkanna2/Voice_Assistant.git
    cd Voice_Assistant
    ```

## Usage

1. Navigate to the directory where the project is located.
2. Run the main Python file.
3. The assistant will start and listen for your voice commands. Speak clearly and give commands such as:
   - "Search for [query] on Google."
   - "Tell me about [topic] from Wikipedia."
   - "What is the date and time?"

## Limitations

- This is a prototype and may not handle complex voice commands.
- The accuracy of voice recognition may vary based on the quality of the microphone and the clarity of speech.
- Limited to basic tasks and predefined functionalities.

## Contributions

Contributions to improve the Voice Assistant are welcome. Feel free to fork the repository and submit pull requests.
