"""
    Name:    jarvis_project.py
    Author:  Augustus Allred
    Created: 3/26/23
    Purpose: JARVIS program that allows the user to use voice recognition
             make menu choices and voice commands
"""

import utils
# pip install wikipedia
import wikipedia
# We have to install pyaudio, we do not have to import it
# SpeechRecognition uses pyaudio directly
# pip install pyaudio
# pip install SpeechRecognition
from sys import exit
import speech_recognition as sr
from sys import exit
from time import sleep
# pip install pyttsx3
import pyttsx3

class JARVIS:
    def __init__(self) -> None:
        # Create SpeechRecognition recognizer object
        self.r = sr.Recognizer()

        """ VOICE PROPERTIES CONSTANTS """
        RATE = 150      # integer default 200 words per minute
        VOLUME = .9     # float 0.0-1.0 inclusive default 1.0
        VOICE = 0       # Set 1 for Zira (female), 0 for David (male)
        # Initialize the pyttsx3 voice engine
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', RATE)
        self.engine.setProperty('volume', VOLUME)
        # Retrieves all available voices from your system
        voices = self.engine.getProperty("voices")
        self.engine.setProperty("voice", voices[VOICE].id)
        # Run engine to set properties
        self.engine.runAndWait()

    def take_user_input(self):
        """
            Recognizes user voice input using
            Speech Recognition module, converts it to text
        """
        # With your local microphone as the source
        with sr.Microphone() as source:
            print('Listening . . . .')
            self.r.pause_threshold = 1
            # Start listening for speech
            audio = self.r.listen(source)

        try:
            print('Recognizing . . .')
            # Capture the recognized word in a string variable
            recognized_words = self.r.recognize_google(
                audio, language='en-US', show_all=True)
            # Google Speech Recognition returns a list of dictionaries
            # Pull only the transcript witht eh highest confidence
            self.query = recognized_words['alternative'][0]['transcript']
            print(self.query)
            # Get text from command line
            spoken_text = self.query
            # Call the say method to speak the text
            self.engine.say(spoken_text)
            self.engine.runAndWait()
            # If you say quit, the program will exit

        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            
        except sr.RequestError as e:
            # If there was an error communicating with Google Speech
            print(f"Google Speech did not respond: {e}")

    def menu(self):
        print("\n    - Hello Jarvis")
        print("    - Wikipedia")
        print("    - Quit\n")

    def voice_commands(self):
        if self.query == "quit":
            # Quit program
            print("\nHave a good day!")
            self.engine.say("Have a good day!")
            self.engine.runAndWait()
            self.engine.stop()
            sleep(2)
            exit(0)
        elif self.query == "hello Jarvis":
            self.hello_response = "Hello, Gus!"
            print(self.hello_response)
            # Get text from command line
            spoken_text = self.hello_response
            # Call the say method to speak the text
            self.engine.say(spoken_text)
            self.engine.runAndWait()
        elif self.query == "Wikipedia":
            self.get_wikipedia()
            self.display_wikipedia()
            self.engine.runAndWait()


    def get_wikipedia(self):
        """
            Searck Wikipedia
        """
        print("Search Wikipedia")
        self.engine.say("Search Wikipedia")
        self.engine.runAndWait()
        try:
            jarvis.take_user_input()
            # Type in your search term
            self.query = self.query
            # Return a summary result of 3 sentences
            self.__summary = wikipedia.summary(self.query, sentences=3)
            
        except:
            # Use raise for troubleshooting exceptions
            # If there is an exception, allow the user to try again.
            spoken_text = "Try a different search term."
            self.engine.say(spoken_text)

    def display_wikipedia(self):
        """
            Display Wikipedia search results
        """
        print(self.__summary)
        self.engine.say(self.__summary)

    def greet_user(self):
        """
            Greet user
        """
        self.engine.say("Hello, I am Jarvis.")
        self.engine.say("What woud you like me to do for you?")
        self.engine.runAndWait()



# Create a jarvis program object
jarvis = JARVIS()
print(utils.title("Jarvis Personal Assistant"))
jarvis.greet_user()
while True:
    jarvis.menu()
    jarvis.take_user_input()
    jarvis.voice_commands()