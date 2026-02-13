"""Text-to-Speech Testing Module

Tests different text-to-speech engines for the gesture recognition system.
Provides both Google Text-to-Speech (gTTS) and Windows SAPI options.
"""

import os
import tempfile
import win32api
import win32com.client
from gtts import gTTS

# Configuration
DEFAULT_LANGUAGE = 'en'
DEFAULT_SPEED = False  # False = normal speed, True = slow
OUTPUT_FILE = "output.mp3"


def gtts_text_to_speech(text, language=DEFAULT_LANGUAGE, slow=DEFAULT_SPEED):
    """Convert text to speech using Google Text-to-Speech
    
    Args:
        text (str): Text to convert to speech
        language (str): Language code (default: 'en')
        slow (bool): Whether to speak slowly (default: False)
    """
    print(f"Using Google TTS for: '{text}'")
    
    try:
        # Create a gTTS object
        tts = gTTS(text=text, lang=language, slow=slow)
        
        # Save the audio to a file
        tts.save(OUTPUT_FILE)
        print(f"Audio saved to {OUTPUT_FILE}")
        
        # Play the audio file
        play_audio_file(OUTPUT_FILE)
        
    except Exception as e:
        print(f"Google TTS Error: {e}")


def sapi_text_to_speech(text, rate=0):
    """Convert text to speech using Windows SAPI
    
    Args:
        text (str): Text to convert to speech
        rate (int): Speech rate (-10 to 10, default: 0)
    """
    print(f"Using Windows SAPI for: '{text}'")
    
    try:
        # Initialize Windows Speech API
        speaker = win32com.client.Dispatch("SAPI.SpVoice")
        
        # Set speech rate if specified
        if rate != 0:
            speaker.Rate = rate
        
        # Speak the text
        speaker.Speak(text)
        
    except Exception as e:
        print(f"Windows SAPI Error: {e}")


def play_audio_file(file_path):
    """Play an audio file using Windows default player
    
    Args:
        file_path (str): Path to the audio file
    """
    try:
        if os.path.exists(file_path):
            print(f"Playing audio file: {file_path}")
            win32api.ShellExecute(0, "open", file_path, None, None, 1)
        else:
            print(f"Audio file not found: {file_path}")
            
    except Exception as e:
        print(f"Audio playback error: {e}")


def test_gesture_phrases():
    """Test TTS with common gesture phrases"""
    gesture_phrases = [
        "hello",
        "how are you",
        "good morning",
        "thank you",
        "goodbye",
        "help me",
        "I am fine",
        "nice to meet you"
    ]
    
    print("\n=== Testing Gesture Phrases ===")
    
    for i, phrase in enumerate(gesture_phrases):
        print(f"\nTesting phrase {i + 1}: '{phrase}'")
        
        # Test both TTS engines
        print("1. Windows SAPI:")
        sapi_text_to_speech(phrase)
        
        input("Press Enter to continue to Google TTS...")
        
        print("2. Google TTS:")
        gtts_text_to_speech(phrase)
        
        if i < len(gesture_phrases) - 1:
            input("Press Enter for next phrase...")


def interactive_test():
    """Interactive TTS testing"""
    print("\n=== Interactive TTS Test ===")
    print("Enter text to convert to speech (or 'quit' to exit)")
    
    while True:
        text = input("\nEnter text: ").strip()
        
        if text.lower() in ['quit', 'exit', 'q']:
            break
            
        if not text:
            continue
        
        print("Choose TTS engine:")
        print("1. Windows SAPI (fast)")
        print("2. Google TTS (requires internet)")
        
        choice = input("Enter choice (1 or 2): ").strip()
        
        if choice == '1':
            sapi_text_to_speech(text)
        elif choice == '2':
            gtts_text_to_speech(text)
        else:
            print("Invalid choice. Using Windows SAPI.")
            sapi_text_to_speech(text)


def main():
    """Main function for TTS testing"""
    print("=== Text-to-Speech Testing Module ===")
    
    # Basic functionality test
    print("\n1. Basic TTS Test")
    test_text = "Hello, this is a test of the text to speech system."
    
    print("Testing Windows SAPI...")
    sapi_text_to_speech(test_text)
    
    input("Press Enter to test Google TTS...")
    gtts_text_to_speech(test_text)
    
    # Menu for different test modes
    while True:
        print("\n=== TTS Test Menu ===")
        print("1. Test gesture phrases")
        print("2. Interactive testing")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ").strip()
        
        if choice == '1':
            test_gesture_phrases()
        elif choice == '2':
            interactive_test()
        elif choice == '3':
            print("Exiting TTS test...")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
    
    # Cleanup
    if os.path.exists(OUTPUT_FILE):
        try:
            os.remove(OUTPUT_FILE)
            print(f"Cleanup: Removed {OUTPUT_FILE}")
        except Exception as e:
            print(f"Cleanup warning: Could not remove {OUTPUT_FILE}: {e}")


if __name__ == "__main__":
    main()
