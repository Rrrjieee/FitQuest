// Get a reference to the video element
const videoElement = document.getElementById('webcam-element');

// Check if the browser supports WebRTC
if ((!navigator.mediaDevices) || (!navigator.mediaDevices.getUserMedia)) {
    console.error('Unfortunately, WebRTC is not supported by this browser.');
}

// Access the user's camera
navigator.mediaDevices
    .getUserMedia({ video: true })
    .then(function (stream) {
        // Set the video element's source to the camera stream
        videoElement.srcObject = stream;
    })
    .catch(function (error) {
        // Get a reference to the modal element
        var prompt = document.getElementById('camera_declined_prompt');

        // Show the modal
        prompt.style.display = 'block';
        prompt.classList.add('show');
    });