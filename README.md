# minimal-daw
Minimal DAW
A lightweight, web-based Digital Audio Workstation (DAW) for creating music with an interactive piano roll sequencer, MIDI recording, and audio synthesis. The project supports recording MIDI from a Yamaha digital piano, programming drums and bass tracks, selecting synth sounds (e.g., grand piano), and exporting projects as WAV files.
Features

Piano Roll Sequencer: Place and edit notes for piano tracks with a visual interface.
MIDI Recording: Capture input from a Yamaha digital piano via Web MIDI API.
Synth Sounds: Includes various piano sounds, such as grand piano, with support for additional synths and audio samples.
Drums and Bass: Programmable tracks for rhythm and bass (step sequencer to be added later).
Export: Render projects as WAV files (MP3 export planned).
Built with Flask, Tone.js, and Web MIDI API for a minimal, browser-based experience.

Prerequisites

Python 3.10.6+ (for Flask backend)
Flask 3.1 (web framework)
Google Chrome (for Web MIDI API support)
Yamaha Digital Piano with USB MIDI connectivity
Git (for version control)

Setup Instructions

Clone the Repository:
git clone <repository-url>
cd minimal-daw


Create a Virtual Environment:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install Dependencies:
pip install -r requirements.txt


Run the Flask App:
python app.py


Access the DAW:

Open Chrome and navigate to http://localhost:5000.
Connect your Yamaha piano via USB for MIDI input.



Usage

Sequencer: Use the piano roll to place and edit notes for piano tracks.
MIDI Recording: Enable MIDI input in Chrome to record from your Yamaha piano.
Synth Selection: Choose from piano sounds (e.g., grand piano) or upload custom audio samples.
Export: Save your project as a WAV file via the export button (once implemented).

Project Structure
minimal-daw/
├── app/
│   ├── static/
│   │   ├── css/style.css      # Sequencer styles
│   │   ├── js/main.js         # Sequencer logic with Tone.js
│   │   └── sounds/            # User-uploaded samples
│   └── templates/
│       └── index.html         # Main frontend template
├── app.py                     # Flask backend
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation

Contributing

Fork the repository and submit pull requests for new features or bug fixes.
Report issues via the repository’s issue tracker.
Future tasks include adding a step sequencer for drums and MP3 export.

License
MIT License. See LICENSE for details.
Acknowledgments

Built with Tone.js for audio synthesis.
Uses Web MIDI API for MIDI input.
Powered by Flask.

