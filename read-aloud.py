# IMPORT THE REQUIRED MODULES 
import streamlit as stream
import pyttsx3

# CONFIGURATION
stream.set_page_config(page_title="SPEAKUP", page_icon=":speaker")

# DEFINITION FOR TEXT TO SPEECH
def text_to_speech(text):
    engine = pyttsx3.init()

    # PROPERTIES OF THE SPEECH
    engine.setProperty('rate', 130)  
    engine.setProperty('volume', 0.9)  

    # CONVERSION
    engine.say(text)
    engine.runAndWait()

# MAIN
def main():
    stream.title("SPEAK ALOUD")

    # INPUT FIELD
    text_input = stream.text_area("ENTER A SENTENCE:")

    # SPEAK UP BUTTON
    if stream.button("SPEAK UP"):
        if text_input:
            text_to_speech(text_input)
        else:
            stream.warning("PLEASE ENTER A SENTENCE TO SPEAK")

if __name__ == "__main__":
    main()

