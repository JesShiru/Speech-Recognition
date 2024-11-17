# import necessary libraries

import streamlit as st
import speech_recognition as sr

# define the Speech Recognition Function
# that will handle the speech recognition process.
def transcribe_speech():
    # initialize recognizer class
    r = sr.Recognizer()

    # reading microphone as source
    with sr.Microphone() as source:
        st.info('Speak now...')

        #listen to speech and store audio in audio_text variable
        audio_text = r.listen(source)
        st.info('Transcribing')

        try:
            # using Google Speech Recognition
            text = r.recognize_google(audio_text)

            return text

        except:
            return "Sorry, I did not get that."
        
# define a function to save the transcription
def save_transcription(text):
    if text:
        with open("transcription.txt", "w") as file:
            file.write(text)
        st.success("Transcription saved to 'transcription.txt'.")

    
# define the main function
# that will handle the user interface of the app.
def main():
    st.title("Speech Recognition App")
    st.write("Click on the microphone to start speaking:")

    # add button to trigger speech recognition
    if st.button("Start Recording"):
        text = transcribe_speech()
        st.write("Transcription: ", text)

    # initialize session state variables
    if "paused" not in st.session_state:
        st.session_state.paused = False
    if "transcription" not in st.session_state:
        st.session_state.transcription = ""

    # save transcription
    if st.button("Save Transcription"):
        save_transcription(st.session_state.transcription)

if __name__ == "__main__":

    main()
