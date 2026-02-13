from gtts import gTTS
import os
import win32api

def text_to_speech(text, language='en'):
    # Create a gTTS object
    tts = gTTS(text=text, lang=language, slow=False)
    
    # Save the audio to a file
    tts.save("output.mp3")
    
    # Play the audio file
    play_audio_file("output.mp3")

def play_audio_file(file_path):
    # Use win32api to play the audio file
    win32api.ShellExecute(0, "open", file_path, None, None, 1)

# Example usage:
text = "Hello, how are you?"
text_to_speech(text)
