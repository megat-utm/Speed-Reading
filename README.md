# Speed-Reading
 [Demo Preview](https://github.com/megatirfanzack/Speed-Reading/assets/118198158/88f3c2ef-2abc-4667-89da-7520a257cfe6)

 read more about our course project at [Arxiv](https://arxiv.org/submit/5027786/view)

## Text Summarization Prototype

This repository contains a simple text summarization prototype built with Flask, PyTorch, and Hugging Face's Transformers library. The prototype includes a basic frontend built with HTML, CSS, and JavaScript, and a backend that uses a pre-trained model from Hugging Face's model hub to summarize text.

## Setup
Follow these steps to set up and run the prototype on your local machine.

### 1. Clone the Repository
First, clone the repository to your local machine. Open your terminal and run the following command:

```bash
git clone https://https://github.com/megatirfanzack/Speed-Reading.git
```

### 2. Create a Virtual Environment
Navigate to the project directory and create a virtual environment. 

```bash
cd Speed-Reading
```

This will help to keep the dependencies required by the project separate from your global Python environment.

If you're using Python 3, you can create a virtual environment using the following commands:

```bash
python3 -m venv myenv
```

To activate the virtual environment, use one of the following commands based on your operating system:

On macOS and Linux:

```bash
source myenv/bin/activate
```

On Windows:

```bash
activate.bat
```
or
```bash
myenv\Scripts\activate.bat
```

### 3. Install Dependencies
With the virtual environment activated, you can install the necessary dependencies using pip. Run the following command:

```bash
pip install -r requirements.txt
```
or
```bash
pip install flask transformers torch nltk
```

This will install Flask (for the web server), Transformers (for the pre-trained models), and PyTorch (for the underlying deep learning operations).

### 4. Run the Web Server
Run the following command to run the web server:
    
```bash
python3 -m flask run --host=0.0.0.0
```
or
```bash
python3 -m flask run
```
or
```bash
python app.py
```

You should see output similar to this in your terminal window:
```bash
Serving Flask app "Speed-Reading"
Listening on 0.0.0.0:5000
```
This means that the web server is running and is ready to accept requests. You can now open a web browser and navigate to http://localhost:5000 to view the prototype.

That's it! You should now have the text summarization prototype running on your local machine. Enjoy summarizing!
