# Text-to-Speech Application

# Text-to-Speech Application

This application uses Streamlit along with Transformers library to convert text input into speech audio using the SpeechT5 model for text-to-speech synthesis and HiFi-GAN for vocoding.

## Setup

### Installation

Ensure you have Python 3.6+ installed. Install required packages using pip:
    
```
pip install -r requirements.txt 
```

Make sure your `requirements.txt` includes the necessary libraries like `streamlit`, `transformers`, `datasets`, `torch`, and `soundfile`.

### Configuration

Modify `config.py` to set the model name, vocoder name, embeddings dataset, speaker index, samplerate, and output file configuration:

```python
MODEL_NAME = "microsoft/speecht5_tts"
VOCODER_NAME = "microsoft/speecht5_hifigan"
EMBEDDINGS_DATASET = "Matthijs/cmu-arctic-xvectors"
SPEAKER_INDEX = 10
SAMPLERATE = 16000
OUTPUT_FILE = "speech.wav"
```
### Running the Application
```
streamlit run app.py
```
The application will launch in your default web browser.

### Usage
* Enter the text you want to convert into speech in the provided text area.
* Click the "Convert" button to generate speech.
* The generated speech will be played back and available for download as **'speech.wav'**.

