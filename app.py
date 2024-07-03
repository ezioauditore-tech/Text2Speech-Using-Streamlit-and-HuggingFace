
import streamlit as st
from text2speech import TextToSpeech

def main():
    st.title("Text to Speech Converter")

    text = st.text_area("Enter the text you want to convert to speech:")

    if st.button("Convert"):
        if text:
            tts = TextToSpeech()
            output_file = tts.generate_speech(text)
            st.success("Speech generated successfully!")
            st.audio(output_file, format="audio/wav")
        else:
            st.error("Please enter some text.")

if __name__ == "__main__":
    main()