const socket = io();

function startSession() {
    socket.emit('startSession');
    alert('Session Started');
}

socket.on('sessionStarted', () => {
    console.log("Session started for all connected students.");
});

