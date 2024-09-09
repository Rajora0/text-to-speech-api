# api.py
from flask import Flask, request, jsonify, send_file
import io
import soundfile as sf
from model import speaker_dict, synthesizer, synthesize_speech

app = Flask(__name__)

@app.route('/synthesize', methods=['POST'])
def synthesize():
    data = request.json
    speaker_id = data.get('speaker')
    text = data.get('text')

    if speaker_id not in speaker_dict:
        return jsonify({"error": "Speaker not found"}), 400

    if not text:
        return jsonify({"error": "Text is required"}), 400

    # Get the speaker embedding
    speaker_embedding = speaker_dict[speaker_id]

    # Synthesize speech
    speech = synthesize_speech(text, speaker_embedding, synthesizer)

    # Create an in-memory file object for the WAV file
    audio_buffer = io.BytesIO()
    sf.write(audio_buffer, speech["audio"], samplerate=speech["sampling_rate"], format='wav')
    audio_buffer.seek(0)

    # Prepare metadata
    duration = len(speech["audio"]) / speech["sampling_rate"]
    file_size = len(audio_buffer.getvalue())

    metadata = {
        "text": text,
        "speaker": speaker_id,
        "duration": duration,
        "file_size": file_size
    }

    # Return the audio and metadata
    response = send_file(
        audio_buffer,
        as_attachment=True,
        download_name='speech.wav',
        mimetype='audio/wav'
    )
    response.headers['metadata'] = str(metadata)  # Adding metadata to the response headers
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
