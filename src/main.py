# main.py

import os
import sys
from gemini_api import GeminiAPI
from typing_interface import TypingInterface
from metrics import Metrics
from config import Config

def main():
    config = Config()
    api_key = config.load_api_key()

    if not api_key:
        api_key = input("Please enter your Gemini API key: ")
        config.save_api_key(api_key)

    gemini_api = GeminiAPI(api_key)

    while True:  # Main loop to allow continuous practice
        prompt = input("Enter a prompt for text generation: ")
        text = gemini_api.fetch_random_paragraph(prompt)

        if text:
            print("\nText fetched successfully! Get ready to type...")
            
            # Create typing interface and start session
            typing_interface = TypingInterface(text)
            continue_practice = typing_interface.start_typing_practice()

            # If user doesn't want to continue with a new text, exit
            if not continue_practice:
                print("Thanks for practicing with Terminal Typer!")
                break
        else:
            print("Failed to fetch text from Gemini API.")
            break  # Exit loop if API fails
            

if __name__ == "__main__":
    main()