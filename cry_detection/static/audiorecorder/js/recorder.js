// static/audiorecorder/js/recorder.js

// UI elements
const recordButton    = document.getElementById('record');
const stopButton      = document.getElementById('stop');
const playbackSection = document.getElementById('playbackSection');
const playbackAudio   = document.getElementById('playbackAudio');
const submitButton    = document.getElementById('submitRecording');

let mediaRecorder;
let audioChunks = [];
let recordedBlob = null;

// CSRF helper (Django)
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    document.cookie.split(';').forEach(cookie => {
      cookie = cookie.trim();
      if (cookie.startsWith(name + '=')) {
        cookieValue = decodeURIComponent(cookie.slice(name.length + 1));
      }
    });
  }
  return cookieValue;
}

// Request microphone access and setup recorder
navigator.mediaDevices.getUserMedia({ audio: true })
  .then(stream => {
    mediaRecorder = new MediaRecorder(stream);

    // Collect audio data
    mediaRecorder.addEventListener('dataavailable', event => {
      audioChunks.push(event.data);
    });

    // On stop, create Blob and show playback + submit
    mediaRecorder.addEventListener('stop', () => {
      recordedBlob = new Blob(audioChunks, { type: 'audio/webm' });
      audioChunks = [];

      const url = URL.createObjectURL(recordedBlob);
      playbackAudio.src = url;

      // Show playback section
      if (playbackSection.classList.contains('d-none')) {
        playbackSection.classList.replace('d-none', 'd-flex');
      }
      submitButton.disabled = false;
    });

    // Start recording
    recordButton.addEventListener('click', () => {
      audioChunks = [];
      recordedBlob = null;

      // Hide playback section
      if (playbackSection.classList.contains('d-flex')) {
        playbackSection.classList.replace('d-flex', 'd-none');
      }
      submitButton.disabled = true;

      mediaRecorder.start();
      recordButton.disabled = true;
      stopButton.disabled   = false;
    });

    // Stop recording
    stopButton.addEventListener('click', () => {
      mediaRecorder.stop();
      recordButton.disabled = false;
      stopButton.disabled   = true;
    });
  })
  .catch(error => {
    console.error('Microphone error:', error);
    alert('Could not access your microphone.');
  });

// Submit recorded blob via fetch() to /result/
submitButton.addEventListener('click', () => {
  if (!recordedBlob) return;

  const formData = new FormData();
  formData.append('audioFile', recordedBlob, 'recording.webm');

  fetch('/result/', {
    method: 'POST',
    headers: { 'X-CSRFToken': getCookie('csrftoken') },
    body: formData
  })
    .then(response => response.text())
    .then(html => {
      document.open();
      document.write(html);
      document.close();
    })
    .catch(err => {
      console.error('Upload failed:', err);
      alert('Failed to upload recording.');
    });
});
