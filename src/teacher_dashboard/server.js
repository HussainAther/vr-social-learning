const express = require('express');
const app = express();
const server = require('http').createServer(app);
const io = require('socket.io')(server);
const PORT = 3000;

app.use(express.static('public'));

io.on('connection', (socket) => {
    console.log('Teacher connected');
    socket.on('startSession', () => {
        io.emit('sessionStarted');
    });
});

server.listen(PORT, () => console.log(`Teacher dashboard running on http://localhost:${PORT}`));

