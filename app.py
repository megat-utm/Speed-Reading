from flask import Flask, render_template, request, jsonify
from transformers import pipeline, T5Tokenizer , T5ForConditionalGeneration
import nltk
nltk.download('punkt')

app = Flask(__name__)

# Initialize the summarization pipeline here
summarizer = pipeline("summarization")
tokenizer = T5Tokenizer.from_pretrained("t5-base")
model = T5ForConditionalGeneration.from_pretrained("t5-base")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])

def summarize():
    # Extract text from the request
    text = request.json['text']

    # Split the text into paragraphs
    paragraphs = text.split('\n')

    summarized_text = ""
    for paragraph in paragraphs:
        # Only generate a summary if the paragraph contains more than 5 words
        if len(paragraph.split(' ')) > 5:
            # Use the summarization pipeline to summarize the paragraph
            inputs = tokenizer.encode("Generate a concise and coherent summary: " + paragraph, return_tensors='pt', max_length=1024, truncation=True)
            outputs = model.generate(inputs, max_length=512, min_length=30, length_penalty=1.0, num_beams=5, early_stopping=True)
            summarized_paragraph = tokenizer.decode(outputs[0], skip_special_tokens=True)

            # Append the summarized paragraph to the summarized text
            summarized_text += summarized_paragraph + "\n"

    # Post-processing to remove repeated sentences
    summarized_text = apply_half_bold(summarized_text)
    
    # Return the summarized text
    return jsonify(summarized_text)

def apply_half_bold(text):
    words = text.split(" ")
    formatted_text = ""
    for word in words:
        bold_index = len(word) // 2  # Integer division to get the floor value
        bold_word = "<b>" + word[:bold_index] + "</b>" + word[bold_index:]
        formatted_text += bold_word + " "
    return formatted_text


if __name__ == '__main__':
    app.run(debug=True)
