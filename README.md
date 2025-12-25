# 3D Minecraft Beta Game 🎮

A feature-rich 3D Minecraft Beta-style game built with Three.js, now with **MULTIPLAYER** support!

## ✨ Features
- 🌍 **5 World Types**: Normal, Snowy, Desert, Extreme (massive mountains), Flat
- 🧱 **23 Block Types**: Grass, Dirt, Stone, Ores, Wood, Glass, Water, and more!
- 🎯 **Survival Mode**: Health (10 hearts) and Hunger (10 bars) systems
- 👾 **Mobs**: Zombies and Skeletons with AI that chase the player
- ⚒️ **Crafting System**: Press C to craft items from recipes
- 🏃 **Physics**: Realistic gravity, jumping, and fall damage
- 👥 **MULTIPLAYER**: Play with friends online with nicknames and real-time block syncing
- 🎨 **Beta-Style**: Nostalgic Minecraft Beta 1.7.3 aesthetics

## 🎮 Controls
- **WASD** - Move around
- **Mouse** - Look around
- **Left Click** - Break block
- **Right Click** - Place block
- **Space** - Jump
- **C** - Open crafting menu
- **1-9** - Select hotbar slots
- **Mouse Wheel** - Scroll through blocks

## 🚀 How to Run

### Single Player Mode
1. Install Python 3 if not already installed
2. Open terminal in the game folder
3. Run: `python -m http.server 8080`
4. Open browser and go to: `http://localhost:8080/vanilla.html`
5. Choose a world type and enter your nickname
6. Start playing!

### Multiplayer Mode
1. **Install WebSocket library**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Start the multiplayer server** (in one terminal):
   ```bash
   python multiplayer_server.py
   ```
   You should see:
   ```
   ================================================
   🎮 Minecraft Multiplayer Server
   ================================================
   Server starting on ws://localhost:8765
   ```

3. **Start the HTTP server** (in another terminal):
   ```bash
   python -m http.server 8080
   ```

4. **Open the game** in your browser:
   - Go to `http://localhost:8080/vanilla.html`
   - Choose a world type
   - Enter your nickname
   - You'll automatically connect to multiplayer!

5. **Have your friends connect**:
   - They need to use the same world type
   - Each player gets a unique nickname
   - Players see each other as blue boxes with name labels
   - All block changes are synchronized in real-time!

> **Note**: If the multiplayer server isn't running, the game will automatically fall back to single-player mode.

## 🌍 World Types
- **Normal**: Rolling hills with trees, flowers, and varied terrain
- **Snowy**: Everything covered in snow - perfect for winter builds
- **Desert**: Sandy dunes as far as the eye can see
- **Extreme**: MASSIVE mountains reaching 250 blocks high!
- **Flat**: Completely flat world - ideal for creative building

## 📦 Crafting Recipes (Press C)
- **Oak Planks**: 1 Oak Log → 4 Planks
- **Sticks**: 2 Oak Planks → 4 Sticks
- **Cobblestone**: Made by breaking stone
- **Glass**: Smelt sand
- **Bricks**: Smelt clay

## 👾 Mobs
- **Zombies** (Green): Slow but dangerous
- **Skeletons** (White): Faster enemies
- Both will chase you when within 50 blocks!
- Deal 1 damage on contact

## 💡 Tips
- Don't fall from high places - you'll take fall damage!
- Keep your hunger bar full or you'll starve
- Extreme worlds have mountains over 200 blocks tall
- In multiplayer, you can see other players' names above them
- All block changes sync instantly with other players

## 📁 Files
- `vanilla.html` - Main game file with all logic
- `multiplayer_server.py` - WebSocket server for multiplayer
- `requirements.txt` - Python dependencies
- `textures/` - 23 block textures

## 🔧 Requirements
- **Browser**: Modern web browser with WebGL support
- **Python**: Python 3.7+ for servers
- **Internet**: For Three.js CDN (or use local copy)
- **Multiplayer**: `websockets` library (install with pip)

## 🎉 Have Fun!
Build amazing structures, explore different world types, and play with friends in multiplayer mode!
