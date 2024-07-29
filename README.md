## Language Translation
## Overview

This project is a language translation service built using Streamlit and Hugging Face Transformers. It supports translation between English and Greek, and Romanian and English. The pre-trained models are fine tuned for sequence-to-sequence language translation and provides a web interface for users to input text and get translations.

## Features

- Translate text between English and Greek
- Translate text between Romanian and English
- User-friendly web interface built with Streamlit

## Installation

To get started with this project, you'll need to set up a Python environment and install the necessary dependencies. Follow these steps:

1. **Clone the repository**

   ```bash
    https://github.com/RamanaNani/Language-translation.git
   cd Language-translation

2. Access data
   To try with multiple languages you can refer to this page [europarl](https://www.statmt.org/europarl/v10/training/)

3. Pretrained and finetuning the model
   Get pretrained models from Hugging face or research papers. These are the pretrained models that are used
   * Finetuning Translate text between English and Greek from pretrained models by using transformers: [English to Greek](https://huggingface.co/Helsinki-NLP/opus-mt-en-el)
   * Finetuning Translate text between Romanian and English from pretrained models by using transformers: [Romanian to English](https://huggingface.co/BlackKakapo/opus-mt-ro-en)

4. Install dependencies
   Install all the required packeges as mentioned in the `Pattern_Recognition_Greek.ipynb` and `Pattern_Recognition_Roman.ipynb`

5. Download model weights
   Place the pre-trained model weights in the appropriate directory as specified in your code. Ensure the paths in your code match the location of these weights.

6. User Interface
   Run `main.py` Start the Streamlit app by running the following command:
   ``` bash
   streamlit run main.py

   
