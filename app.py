from flask import Flask, jsonify, send_from_directory, render_template
import os

app = Flask(__name__)
AUDIO_FOLDER = 'static/audios'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/audios')
def list_audios():
    files = [
        f for f in os.listdir(AUDIO_FOLDER)
        if f.lower().endswith(('.mp3', '.wav', '.ogg', '.opus'))
    ]
    return jsonify(files)

@app.route('/audios/<filename>')
def serve_audio(filename):
    return send_from_directory(AUDIO_FOLDER, filename)

if __name__ == '__main__':
    app.run(debug=True)
