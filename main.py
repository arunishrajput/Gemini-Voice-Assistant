import speech_recognition as sr
import pyttsx3
import google.generativeai as genai

# Initializing pyttsx3
listening = True
sending_to_gemini = False
engine = pyttsx3.init()

# Set up the Google Gemini API
genai.configure(api_key="Gemini_API_Key")

# Set up the model
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 0,
    "max_output_tokens": 8192,
}

safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
]

# Customizing The output voice
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
volume = engine.getProperty('volume')

model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

convo = model.start_chat(history=[])

def get_response(user_input):
    convo.send_message(user_input)
    gemini_reply = convo.last.text
    print(gemini_reply)
    return gemini_reply

exit_words = ["exit", "stop", "quit"]  # Add your exit words here
wake_word = "gemini"  # Set your wake word here

while listening:
    with sr.Microphone() as source:
        recognizer = sr.Recognizer()
        recognizer.adjust_for_ambient_noise(source)
        recognizer.dynamic_energy_threshold = 3000

        try:
            print("Listening...")
            audio = recognizer.listen(source, timeout=5.0)
            response = recognizer.recognize_google(audio)
            print(response)

            if any(exit_word in response.lower() for exit_word in exit_words):
                sending_to_gemini = False
                print("Stopped sending responses to Gemini.")
                continue

            if wake_word in response.lower() and not sending_to_gemini:
                sending_to_gemini = True
                print("Resumed sending responses to Gemini.")

            if sending_to_gemini:
                response_from_gemini = get_response(response)
                engine.setProperty('rate', 200)
                engine.setProperty('volume', volume)
                engine.setProperty('voice', 'greek')
                engine.say(response_from_gemini)
                engine.runAndWait()

        except sr.UnknownValueError:
            print("Didn't recognize anything.")
