import speech_recognition as sr
import pyttsx3
from datetime import datetime

# Initialize the Text-to-Speech engine
engine = pyttsx3.init()

def speak(text):
    """Function to make the computer speak"""
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

def listen_and_process():
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("\n--- Listening ---")
        recognizer.pause_threshold = 1 # Wait 1 second of silence before stopping
        audio = recognizer.listen(source)

    try:
        # Convert Speech to Text
        command = recognizer.recognize_google(audio).lower()
        print(f"You said: {command}")
        
        # Logic for different commands
        if "hello" in command:
            speak("Hello! I am your Python assistant. How can I help you today?")
            
        elif "time" in command:
            current_time = datetime.now().strftime("%I:%M %p")
            speak(f"The current time is {current_time}")
            
        elif "your name" in command:
            speak("I don't have a name yet. You can call me Mini Project.")
            
        elif "stop" in command or "exit" in command:
            speak("Goodbye!")
            return False # This will break the loop
            
        else:
            speak("I heard you, but I don't know that command yet.")

    except sr.UnknownValueError:
        speak("I'n sorry, I didn't catch that. Could you repeat it?")
    except sr.RequestError:
        speak("I'm having trouble connecting to the recognition service.")
        
    return True

if __name__ == "__main__":
    speak("System online.")
    running = True
    while running:
        running = listen_and_process()