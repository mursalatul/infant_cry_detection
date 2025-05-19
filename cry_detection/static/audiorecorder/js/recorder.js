// static/audiorecorder/js/recorder.js

// UI elements
const recordButton    = document.getElementById('record');
const stopButton      = document.getElementById('stop');
const playbackSection = document.getElementById('playbackSection');
const playbackAudio   = document.getElementById('playbackAudio');
const submitButton    = document.getElementById('submitRecording');

let mediaRecorder, audioChunks = [], recordedBlob = null;

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

navigator.mediaDevices.getUserMedia({ audio: true })
  .then(stream => {
    mediaRecorder = new MediaRecorder(stream);

    mediaRecorder.addEventListener('dataavailable', e => {
      audioChunks.push(e.data);
    });

    mediaRecorder.addEventListener('stop', () => {
      // assemble blob
      recordedBlob = new Blob(audioChunks, { type: 'audio/webm' });
      audioChunks = [];

      // show playback + submit
      const url = URL.createObjectURL(recordedBlob);
      playbackAudio.src = url;
      playbackSection.style.display = 'flex';
    });

    // start recording
    recordButton.onclick = () => {
      audioChunks = [];
      recordedBlob = null;
      playbackSection.style.display = 'none';
      submitButton.disabled = false;

      mediaRecorder.start();
      recordButton.disabled = true;
      stopButton.disabled   = false;
    };

    // stop recording
    stopButton.onclick = () => {
      mediaRecorder.stop();
      recordButton.disabled = false;
      stopButton.disabled   = true;
    };
  })
  .catch(err => {
    console.error('Microphone error:', err);
    alert('Could not access your microphone.');
  });

// Submit recorded blob just like your form
submitButton.addEventListener('click', () => {
  if (!recordedBlob) return;

  const formData = new FormData();
  formData.append('audioFile', recordedBlob, 'recording.webm');

  fetch('/result/', {
    method: 'POST',
    headers: { 'X-CSRFToken': getCookie('csrftoken') },
    body: formData,
  })
  .then(res => res.text())
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
