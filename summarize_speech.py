import os
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

DEEPSPEECH_MODEL = r"models/deepspeech-0.9.3-models.tflite"
INPUT_FILE = r"input/speech.wav"
OUTPUT_FILE = r"output/transcript.txt"
MODEL = r"models/bart-large-cnn"
CMD_TO_EXEC = f"deepspeech --model {DEEPSPEECH_MODEL} --audio {INPUT_FILE} > {OUTPUT_FILE}"

os.system(CMD_TO_EXEC)

transcribed_text = str()
with open(OUTPUT_FILE) as file:
    transcribed_text = file.read().strip()

tokenizer = AutoTokenizer.from_pretrained(MODEL)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL)

input_ids = tokenizer(f"summarize: {transcribed_text}", return_tensors='pt').input_ids
outputs = model.generate(input_ids)

print(tokenizer.decode(outputs[0], skip_special_tokens=True))
