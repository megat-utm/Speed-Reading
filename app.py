from flask import Flask, render_template, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# TODO: Initialize the summarization pipeline here
summarizer = pipeline("summarization")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    # TODO: Extract text from the request
    text = request.json['text']

    # TODO: Use the summarization pipeline to summarize the text
    summarized_text = summarizer(text, max_length=150, min_length=30, do_sample=False)

    # TODO: Return the summarized text
    return jsonify(summarized_text[0]['summary_text'])


if __name__ == '__main__':
    app.run(debug=True)