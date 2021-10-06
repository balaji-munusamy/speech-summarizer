# speech-summarizer
Transcribes and summarizes speech or audio

### Pre-requisite
The app requires python3 to be installed in the machine since the programming language used is Python

### Installation Guide
Once the python is installed, install all the dependencies by running the below command.

  pip3 install -r requirements.txt
  
### Model download link

  1. Deepspeech model - https://github.com/mozilla/DeepSpeech/releases/download/v0.9.3/deepspeech-0.9.3-models.tflite
  2. Summarization model - https://huggingface.co/facebook/bart-large-cnn

### Steps to be followed

Speech file to be converted should meet below specifications.
  1. Sample rate - 16KHz
  2. Audio channel - Mono
  3. File format - .wav

Speech summarizer can be built by following below steps.

  1. Select a development environment of your choice
  2. Analyse speech files to check if the specifications are met
  3. Convert Speech to text
  4. Encode text to tokenized IDs
  5. Generate and decode summarized text
  6. Servers and webframeworks can be leveraged for servicing the request as REST API - optional step

### Build your Speech summarizer in 5 minutes

  1. Run Jupyter notebook for quick changes and experiments
  2. Run speech_summarizer.py by passing audio files and model files as input
