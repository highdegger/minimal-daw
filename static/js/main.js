// static/js/main.js - Tone.js setup for Minimal DAW
document.addEventListener('DOMContentLoaded', () => {
    // Initialize Tone.js
    const synth = new Tone.Synth({
        oscillator: { type: 'sine' },
        envelope: { attack: 0.005, decay: 0.1, sustain: 0.3, release: 1 }
    }).toDestination();

    // Placeholder piano roll canvas
    const canvas = document.getElementById('sequencer-canvas');
    const ctx = canvas.getContext('2d');
    canvas.width = canvas.offsetWidth;
    canvas.height = canvas.offsetHeight;

    // Draw grid (placeholder for piano roll)
    ctx.fillStyle = '#eee';
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    ctx.strokeStyle = '#999';
    for (let i = 0; i < canvas.height; i += 20) {
        ctx.beginPath();
        ctx.moveTo(0, i);
        ctx.lineTo(canvas.width, i);
        ctx.stroke();
    }

    // Sample upload handler
    document.getElementById('sample-upload').addEventListener('change', async (e) => {
        const file = e.target.files[0];
        if (file) {
            const formData = new FormData();
            formData.append('file', file);
            const response = await fetch('/api/upload-sample', {
                method: 'POST',
                body: formData
            });
            const result = await response.json();
            console.log(result);
        }
    });

    // Expose functions to global scope for HTML buttons
    window.startPlayback = async () => {
        await Tone.start();
        console.log('Playback started');
        // Placeholder: Trigger synth note
        synth.triggerAttackRelease('C4', '8n');
    };

    window.stopPlayback = () => {
        console.log('Playback stopped');
        Tone.Transport.stop();
    };
});