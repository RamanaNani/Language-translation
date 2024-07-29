import streamlit as st
import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Load models and tokenizers
models_and_tokenizers = {
    "en_el": {
        "tokenizer": AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-el"),
        "model": AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-en-el")
    },
    "ro_en": {
        "tokenizer": AutoTokenizer.from_pretrained("BlackKakapo/opus-mt-ro-en"),
        "model": AutoModelForSeq2SeqLM.from_pretrained("BlackKakapo/opus-mt-ro-en")
    }
}

# Load weights if you have them
model_weights_paths = {
    "en_el": "/Users/ramanareddy/Documents/Assignments_sem2/PR/project/UI/en_el_weights.pth",
    "ro_en": "/Users/ramanareddy/Documents/Assignments_sem2/PR/project/UI/ro_en_weights.pth",
}

for lang_pair, path in model_weights_paths.items():
    models_and_tokenizers[lang_pair]["model"].load_state_dict(torch.load(path, map_location=torch.device('cpu')))
    models_and_tokenizers[lang_pair]["model"].eval()


def translate(input_sentence, lang_pair):
    if len(input_sentence) < 2:
        return "Please enter valid input"

    tokenizer = models_and_tokenizers[lang_pair]["tokenizer"]
    model = models_and_tokenizers[lang_pair]["model"]
    inputs = tokenizer(input_sentence, max_length=128, padding=True, truncation=True, return_tensors="pt")
    translated_tokens = model.generate(**inputs, max_length=128, num_beams=4, early_stopping=True)
    translation = tokenizer.decode(translated_tokens[0], skip_special_tokens=True)

    return translation


st.title("Language Translation Service")

input_text = st.text_area("Enter text to translate:")
source_language = st.selectbox("Select the source language:", ["Romanian", "English"])

if st.button("Translate"):
    if source_language == "Romanian":
        lang_pair = "ro_en"
    else:
        lang_pair = "en_el"

    result = translate(input_text, lang_pair)
    st.write(f"**Translated Text:** {result}")
