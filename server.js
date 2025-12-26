const express = require('express');
const http = require('http');
const socketIO = require('socket.io');
const path = require('path');

const app = express();
const server = http.createServer(app);
const io = socketIO(server);

// Serve static files
app.use(express.static(__dirname));

// Default route - serve vanilla.html
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'vanilla.html'));
});

// Store connected players
const players = {};
const worldBlocks = {}; // Synchronized world state

io.on('connection', (socket) => {
    console.log(`Player connected: ${socket.id}`);
    
    // Add new player
    players[socket.id] = {
        id: socket.id,
        x: 0,
        y: 70,
        z: 0,
        rotationY: 0
    };
    
    // Send existing players to new player
    socket.emit('currentPlayers', players);
    
    // Send existing blocks to new player
    socket.emit('worldState', worldBlocks);
    
    // Notify all other players about new player
    socket.broadcast.emit('playerJoined', players[socket.id]);
    
    // Handle player movement
    socket.on('playerMovement', (data) => {
        if (players[socket.id]) {
            players[socket.id].x = data.x;
            players[socket.id].y = data.y;
            players[socket.id].z = data.z;
            players[socket.id].rotationY = data.rotationY;
            
            // Broadcast to all other players
            socket.broadcast.emit('playerMoved', {
                id: socket.id,
                x: data.x,
                y: data.y,
                z: data.z,
                rotationY: data.rotationY
            });
        }
    });
    
    // Handle block placement
    socket.on('blockPlaced', (data) => {
        const key = `${data.x},${data.y},${data.z}`;
        worldBlocks[key] = data.type;
        
        // Broadcast to all players
        io.emit('blockPlaced', data);
    });
    
    // Handle block breaking
    socket.on('blockBroken', (data) => {
        const key = `${data.x},${data.y},${data.z}`;
        delete worldBlocks[key];
        
        // Broadcast to all players
        io.emit('blockBroken', data);
    });
    
    // Handle disconnect
    socket.on('disconnect', () => {
        console.log(`Player disconnected: ${socket.id}`);
        delete players[socket.id];
        
        // Notify all players
        io.emit('playerLeft', socket.id);
    });
});

const PORT = 3000;
server.listen(PORT, () => {
    console.log(`Multiplayer server running on http://localhost:${PORT}`);
});
