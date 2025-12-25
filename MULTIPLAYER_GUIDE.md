# Multiplayer Setup Guide 🎮

## Quick Start

### For Single Player:
1. Double-click `START_SINGLEPLAYER.bat`
2. Open browser to `http://localhost:8080/vanilla.html`
3. Play!

### For Multiplayer:
1. Double-click `START_SERVERS.bat`
2. Open browser to `http://localhost:8080/vanilla.html`
3. Have friends do the same!

## Manual Setup

### Prerequisites
```bash
# Install websockets (already done if you used START_SERVERS.bat)
pip install websockets
```

### Starting Servers Manually

**Terminal 1 - Multiplayer Server:**
```bash
cd Minecraft-3D-Game
python multiplayer_server.py
```

You should see:
```
==================================================
🎮 Minecraft Multiplayer Server
==================================================
Server starting on ws://localhost:8765
Players can now connect and play together!
```

**Terminal 2 - HTTP Server:**
```bash
cd Minecraft-3D-Game
python -m http.server 8080
```

### Playing the Game
1. Open your browser
2. Go to `http://localhost:8080/vanilla.html`
3. Choose a world type (all players must choose the SAME world type!)
4. Enter your nickname
5. Start playing!

## Multiplayer Features

### What Gets Synced:
- ✅ Player positions and rotations (30 times per second)
- ✅ Player nicknames (visible above players)
- ✅ Block placement (instant)
- ✅ Block breaking (instant)

### What You See:
- Other players appear as **blue boxes**
- Their **nicknames float above them**
- Block changes happen in **real-time**

### Important Notes:
- All players MUST choose the **same world type** at the start
- World generation is client-side, so everyone needs the same seed
- If multiplayer server isn't running, game falls back to single-player automatically

## Network Requirements

### Playing on Same Computer:
- No additional setup needed
- Both servers run on localhost

### Playing on Local Network (LAN):
1. Find your local IP address:
   ```bash
   ipconfig
   # Look for "IPv4 Address" under your network adapter
   # Example: 192.168.1.100
   ```

2. **On the server computer**, edit `vanilla.html` line ~1345:
   ```javascript
   // Change this line:
   ws = new WebSocket('ws://localhost:8765');
   
   // To this (use your server's IP):
   ws = new WebSocket('ws://192.168.1.100:8765');
   ```

3. **On the server computer**, edit `multiplayer_server.py` line ~123:
   ```python
   # Change this line:
   async with websockets.serve(handle_client, "localhost", 8765):
   
   # To this:
   async with websockets.serve(handle_client, "0.0.0.0", 8765):
   ```

4. **Other players** access the game at:
   ```
   http://192.168.1.100:8080/vanilla.html
   ```

5. Make sure Windows Firewall allows connections on ports 8080 and 8765

### Playing over Internet:
1. Set up port forwarding on your router for ports 8080 and 8765
2. Use your public IP address
3. Consider security implications - this is a basic server without authentication!

## Troubleshooting

### "Multiplayer server not available - playing solo"
- ✅ Normal behavior if multiplayer server isn't running
- Make sure `multiplayer_server.py` is running before starting the game
- Check that port 8765 isn't being used by another program

### "Connection refused" in browser console
- Make sure the HTTP server is running on port 8080
- Try `http://localhost:8080/vanilla.html` instead of `http://127.0.0.1:8080/vanilla.html`

### Can't see other players
- Make sure all players chose the SAME world type
- Check browser console for connection errors (F12)
- Verify multiplayer server shows player connections

### Players see different terrain
- This happens if players chose different world types
- Everyone must restart and choose the SAME world type

### "ModuleNotFoundError: No module named 'websockets'"
- Run: `pip install websockets`
- Or use `START_SERVERS.bat` which handles this automatically

## Technical Details

### Server Architecture:
- **HTTP Server** (port 8080): Serves the game files
- **WebSocket Server** (port 8765): Handles real-time multiplayer communication

### Message Types:
1. **join** - Player connects with nickname
2. **playerUpdate** - Position and rotation sync
3. **blockChange** - Block placement/breaking
4. **playerLeft** - Player disconnects

### Performance:
- Player updates sent ~10 times per second (33% of frames at 60 FPS)
- Block changes sent immediately
- Server broadcasts to all connected players
- No server-side world state (clients trust each other)

## Tips for Server Hosts

1. **Start the servers in this order:**
   - First: Multiplayer server (port 8765)
   - Second: HTTP server (port 8080)

2. **Make sure no other programs are using these ports**
   - Check with: `netstat -an | findstr "8080"`
   - And: `netstat -an | findstr "8765"`

3. **Monitor connections:**
   - Multiplayer server logs player joins/leaves
   - Watch the terminal for connection messages

4. **Restart if needed:**
   - Press `Ctrl+C` to stop each server
   - Run `START_SERVERS.bat` again

## Have Fun! 🎉

Build together, explore together, and enjoy the multiplayer experience!

For issues or questions, check the main README.md file.
