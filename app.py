from flask import Flask, render_template, request, jsonify
from transformers import pipeline, T5Tokenizer, T5ForConditionalGeneration
import re
import nltk

nltk.download('punkt')
    
app = Flask(__name__)

# Initialize the summarizer pipeline using the T5 model and tokenizer
tokenizer = T5Tokenizer.from_pretrained("t5-base", model_max_length=512)
model = T5ForConditionalGeneration.from_pretrained("t5-base")
summarizer = pipeline('summarization', model=model, tokenizer=tokenizer)

@app.route('/')
def index():
    return render_template('index.html')

def apply_half_bold(text):
    words = text.split(" ")
    formatted_text = ""
    for word in words:
        bold_index = len(word) // 2 
        bold_word = "<b>" + word[:bold_index] + "</b>" + word[bold_index:]
        formatted_text += bold_word + " "
    return formatted_text

def clean_text(text):
    text = re.sub(r'[^\w\s]', '', text)
    return text

@app.route('/summarize', methods=['POST'])
def summarize():
    # Extract text from the request
    text = request.json['text']

    # Split the text into paragraphs
    paragraphs = text.split('\n')

    summarized_text = ""
    for paragraph in paragraphs:
        # Check if paragraph length exceeds the maximum model length
        if len(paragraph) > 512:
            # Split the paragraph into smaller chunks
            chunked_paragraphs = [paragraph[i:i+512] for i in range(0, len(paragraph), 512)]
        else:
            chunked_paragraphs = [paragraph]

        # Use the summarization pipeline to summarize each chunk
        for i, chunk in enumerate(chunked_paragraphs):
            inputs = tokenizer.encode(chunk, return_tensors='pt', max_length=512, truncation=True)
            outputs = model.generate(inputs, max_length=510 if i < len(chunked_paragraphs) - 1 else 512, min_length=30, length_penalty=1.0, num_beams=5, early_stopping=True, do_sample=False,)
            summarized_chunk = tokenizer.decode(outputs[0], skip_special_tokens=True)
            summarized_chunk = clean_text(summarized_chunk)
            # Append the summarized chunk to the summarized text
            summarized_text += summarized_chunk + "\n"

    bolded = apply_half_bold(summarized_text)

    # Return the summarized text
    return jsonify(bolded)

if __name__ == '__main__':
    app.run(debug=True)
