import pyttsx3  

def text_to_speech():
    engine = pyttsx3.init()  # Initialize TTS engine
    
    # Set properties (optional: adjust voice and speed)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)  # Choose a voice
    engine.setProperty('rate', 150)  # Adjust speed (default: 200)

    text = input("Enter text to convert into speech: ")  # Get user input
    if not text.strip():
        print("Error: No text entered. Please try again.")
        return

    engine.say(text)  # Speak the text
    engine.runAndWait()  # Wait for speech to complete

    # Ask to save as audio file
    save_option = input("Do you want to save the audio? (yes/no): ").strip().lower()
    if save_option == "yes":
        filename = input("Enter filename (without extension): ") + ".mp3"
        engine.save_to_file(text, filename)
        engine.runAndWait()
        print(f"✅ Audio saved as {filename}")

if __name__ == "__main__":
    text_to_speech()
