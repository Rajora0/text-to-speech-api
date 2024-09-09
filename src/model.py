import torch
from datasets import load_dataset
from transformers import pipeline

# Load the speaker embeddings dataset
def load_speaker_embeddings():
    embeddings_dataset = load_dataset("Matthijs/cmu-arctic-xvectors", split="validation")
    speaker_dict = {str(i): torch.tensor(embeddings_dataset[i]["xvector"]).unsqueeze(0) for i in range(len(embeddings_dataset))}
    return speaker_dict

# Initialize the text-to-speech pipeline
def initialize_synthesizer():
    synthesizer = pipeline("text-to-speech", model="microsoft/speecht5_tts", device='cuda')
    return synthesizer

# Synthesize speech
def synthesize_speech(text, speaker_embedding, synthesizer):
    return synthesizer(text, forward_params={"speaker_embeddings": speaker_embedding})

# Load models and embeddings
speaker_dict = load_speaker_embeddings()
synthesizer = initialize_synthesizer()
