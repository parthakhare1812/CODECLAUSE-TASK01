import speech_recognition as sr

def recognize_speech():
    # Initialize the recognizer
    recognizer = sr.Recognizer()

    # Use the default microphone as the audio source
    with sr.Microphone() as source:
        print("\n--- System Ready ---")
        print("Adjusting for ambient noise... Please wait.")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Listening for your command...")
        
        # Capture the audio
        audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            # Using Google Web Speech API (requires internet)
            text = recognizer.recognize_google(audio)
            print(f"You said: '{text}'")
            
            # Basic Logic for Commands
            process_command(text.lower())

        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
        except sr.RequestError as e:
            print(f"Could not request results from service; {e}")

def process_command(command):
    if "hello" in command:
        print("Greeting detected: Hello there!")
    elif "time" in command:
        from datetime import datetime
        print(f"The current time is {datetime.now().strftime('%H:%M:%S')}")
    elif "stop" in command:
        print("Exiting program...")
        exit()
    else:
        print("Command not recognized, but I heard you!")

if __name__ == "__main__":
    while True:
        recognize_speech()