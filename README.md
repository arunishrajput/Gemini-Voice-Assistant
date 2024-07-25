# Gemini Voice Assistant

Gemini Voice Assistant is a voice-activated assistant powered by Google Gemini AI and Python's speech recognition library. It listens for voice commands and interacts with the Gemini API to provide responses.

## Features

- Voice recognition using `speech_recognition` library
- Text-to-speech capabilities using `pyttsx3` library
- Integration with Google Gemini AI for intelligent responses
- Configurable wake words and exit commands
- Customizable voice output settings

## Prerequisites

- Python 3.6 or higher
- Microphone (for voice input)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/arunishrajput/gemini-voice-assistant.git
   cd gemini-voice-assistant
   ```

2. **Create a virtual environment and activate it (optional but recommended):**

   - Create virtual environment:

     ```bash
     python -m venv venv
     ```

   - Activate virtual environment:
     - For Windows:
       ```bash
       venv\Scripts\activate
       ```
     - For Linux/Mac:
       ```bash
       source venv/bin/activate
       ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

   Or install the libraries manually:

   ```bash
   pip install SpeechRecognition pyttsx3 google-generativeai
   ```

4. **Set up your Google Gemini API key:**

   Replace `Gemini_API_Key` in the script with your actual [Google Gemini API key](https://aistudio.google.com/app/apikey).

## Usage

1. **Run the script:**

   ```bash
   python main.py
   ```

2. **Interact with the assistant:**

   - Say the `wake word` (default is "gemini") to start sending responses to Gemini.
   - Use `exit words` (default: "exit", "stop", "quit", "bye", "goodbye") to stop sending responses to Gemini.

## Configuration

- **Wake Word:** Set your desired wake word in the `wake_word` variable.
- **Exit Words:** Customize the exit words in the `exit_words` list.
- **Voice Settings:** Adjust the `rate`, `volume`, and `voice properties` in the pyttsx3 output voice customization section.

## Contribution

- Feel free to fork this repository, create a feature branch, and submit a pull request. Contributions, issues, and feature requests are welcome!

## Acknowledgments

- [Google Gemini AI](https://aistudio.google.com/app/apikey)
- [SpeechRecognition](https://github.com/Uberi/speech_recognition)
- [pyttsx3](https://github.com/nateshmbhat/pyttsx3)
