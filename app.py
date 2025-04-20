# app.py - Flask backend for minimal DAW
from flask import Flask, render_template, jsonify, request
import os

app = Flask(__name__)

# Configuration
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['ALLOWED_EXTENSIONS'] = {'wav', 'mp3'}

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def allowed_file(filename):
    """Check if file extension is allowed."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def index():
    """Render the main DAW interface."""
    return render_template('index.html')

@app.route('/api/upload-sample', methods=['POST'])
def upload_sample():
    """Handle audio sample uploads."""
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    if file and allowed_file(file.filename):
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)
        return jsonify({'message': 'File uploaded', 'filename': file.filename}), 200
    return jsonify({'error': 'Invalid file type'}), 400

@app.route('/api/synth-settings', methods=['GET', 'POST'])
def synth_settings():
    """Get or update synth settings (placeholder for Tone.js integration)."""
    if request.method == 'POST':
        settings = request.json
        # Placeholder: Store settings (e.g., piano type) for future use
        return jsonify({'message': 'Settings updated', 'settings': settings}), 200
    return jsonify({'settings': {'instrument': 'grand_piano'}}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)