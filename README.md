Aqui está um README adaptado para a API de geração de áudio:

---

# Text-to-Speech API with Speaker Embeddings

This repository contains a simple Flask API that generates speech from text input using a pre-trained TTS model and speaker embeddings. The API allows you to specify a speaker and text, synthesizing the speech and returning it along with metadata.

## Structure

- `app.py`: Main Flask application file. Defines the API endpoint and handles requests.
- `model.py`: Handles model loading, speaker embeddings, and speech synthesis.

```
📁 notebooks
    └── 📄 api-test.ipynb
    └── 📄 model.ipynb
    └── 📄 response_speech.wav
    └── 📄 speech.wav
📁 src
    └── 📄 model.py
    └── 📄 app.py
📄 README.md
📄 requirements.txt
```

## Setup and Usage

### 1. Install Dependencies

Create a `requirements.txt` file with the necessary packages:

```
flask
torch
datasets
transformers
soundfile
requests
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

### 2. Run the Flask API

Execute the Flask API:

```bash
python app.py
```

This will start the API server on `http://localhost:5000`.

### 3. Send Requests to the API

You can use tools like `curl`, Postman, or Python's `requests` library to send POST requests to the `/synthesize` endpoint.

#### Example using `curl`:

```bash
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"speaker": "0", "text": "Hello, my dog is cooler than you!"}' \
  http://127.0.0.1:5000/synthesize
```

#### Example using Python's `requests` library:

```python
import requests

api_url = 'http://127.0.0.1:5000/synthesize'
payload = {
    "speaker": "0",  # Replace with a valid speaker ID
    "text": "Hello, my dog is cooler than you!"
}

response = requests.post(api_url, json=payload)

if response.status_code == 200:
    with open("response_speech.wav", "wb") as f:
        f.write(response.content)
    metadata = response.headers.get('metadata', '')
    print("Metadata:", metadata)
else:
    print(f"Request error: {response.status_code}")
    print("Response:", response.text)
```

### Response

The API will respond with a WAV file containing the synthesized speech and metadata headers containing information about the text, speaker, duration of the audio, and file size.

### Notes

- **Speaker Embeddings**: The API uses pre-loaded speaker embeddings. You can modify the `model.py` to include different embeddings or change the model as needed.
- **Error Handling**: This is a basic implementation. Consider adding additional error handling, logging, and authentication for a production-ready application.

Feel free to adapt and extend this example based on your specific needs and deployment environment.