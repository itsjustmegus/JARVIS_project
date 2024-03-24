"""
    Name:    jarvis_project.py
    Author:  Gus Allred
    Created: 3/26/23
    Revised: 3/24/24
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
        # Flag for whether command has been processed or not
        # I got this idea from ChatGPT
        self.command_processed = False

    def take_user_input(self):
        """
            Recognizes user voice input using
            Speech Recognition module, converts it to text
        """
        # With your local microphone as the source
        with sr.Microphone() as source:
            print('Listening . . . .')
            # Energy threshold filters background noise
            # and requires a specific volume to recognize speech
            # I got this idea from ChatGPT
            self.r.energy_threshold = 4000
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
            # Flag for whether command has been processed or not
            # I got this idea from ChatGPT
            self.command_processed = True

        # Timeout error
        # I got this idea from ChatGPT
        except sr.WaitTimeoutError:
                print("Timeout occurred, listening again...")

        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            
        except sr.RequestError as e:
            # If there was an error communicating with Google Speech
            print(f"Google Speech did not respond: {e}")

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
        elif self.query == "write file":
            self.write_file()
            self.engine.runAndWait()
        elif self.query == "Wikipedia":
            self.get_wikipedia()
            self.display_wikipedia()
            self.engine.runAndWait()

        # Flag for whether command has been processed or not
        # I got this idea from ChatGPT
        self.command_processed = False

    def write_file(self):
        """
            Take user input to write to a file
        """
        # Constant for filename
        FILE_NAME = "results.txt"
        
        # Catch any exceptions
        try:
            # Open a file for writing
            with open(FILE_NAME, "w") as text_file:
            
                # Get input from the user
                print("What do you want to write to the file?")
                self.engine.say("What do you want to write to the file?")
                self.engine.runAndWait()
                jarvis.take_user_input()

                # Write the numbers to the file using Fstrings
                text_file.write(f'{self.query}\n')

                # Let the user know it worked
                print("Data was written to results.txt")
                self.engine.say("Data was written to results.txt")


        # Let the user know there was an exception
        except:
            print("There was trouble writing to the file.")
            self.engine.say("There was trouble writing to the file.")

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

    def menu(self):
        """Menu for user"""
        print("\n    - Hello Jarvis")
        print("    - Write File")
        # print("    - Read File")
        print("    - Wikipedia")
        print("    - Quit\n")


# Create a jarvis program object
jarvis = JARVIS()
print(utils.title("Jarvis Personal Assistant"))
jarvis.greet_user()

# Run menu loop
while True:
    jarvis.menu()
    jarvis.take_user_input()
    jarvis.voice_commands()