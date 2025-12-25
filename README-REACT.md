# Minecraft React Edition 🎮

A Minecraft-style voxel game built with React, Three.js, and react-three-fiber.

## Features
- ⚛️ Built with React and react-three-fiber
- 🎮 First-person controls with realistic physics
- 🧱 Place and remove blocks
- 💾 Auto-save world to localStorage
- 🎨 Multiple block types (Grass, Dirt, Stone, Wood, Sand, Glass)
- 🌍 Infinite world (add blocks anywhere)

## Tech Stack
- **React** - UI framework
- **react-three-fiber** - React renderer for Three.js
- **@react-three/drei** - Useful helpers for R3F
- **@react-three/cannon** - Physics engine
- **Zustand** - State management
- **Vite** - Build tool

## Installation

```bash
npm install
```

## Development

```bash
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) in your browser.

## Controls
- **WASD** - Move around
- **Space** - Jump
- **Mouse** - Look around (click to lock pointer)
- **Left Click** - Add block on surface
- **Alt + Click** - Remove block
- **1-6** - Select block type
  - 1: Grass
  - 2: Dirt
  - 3: Stone
  - 4: Wood
  - 5: Sand
  - 6: Glass

## Build for Production

```bash
npm run build
npm run preview
```

## Project Structure

```
src/
├── components/        # React components
│   ├── Cube.jsx      # Individual block component
│   ├── Cubes.jsx     # All blocks manager
│   ├── Ground.jsx    # Ground plane
│   ├── Player.jsx    # Player physics & controls
│   ├── FPV.jsx       # First-person view handler
│   ├── UI.jsx        # User interface overlay
│   └── Crosshair.jsx # Crosshair overlay
├── hooks/            # Custom React hooks
│   └── useKeyboard.js # Keyboard input handler
├── store/            # State management
│   └── useStore.js   # Zustand store
├── textures/         # Texture generation
│   └── textures.js   # Block textures
├── App.jsx           # Main app component
└── main.jsx          # Entry point
```

## How It Works

- **State Management**: Zustand manages global state for blocks and selected texture
- **Physics**: Cannon.js (via @react-three/cannon) handles player physics and collisions
- **Rendering**: react-three-fiber renders the 3D scene using Three.js
- **Persistence**: World state automatically saves to localStorage

## Tips
- Click anywhere to lock your pointer for mouse look
- Press ESC to unlock pointer
- Your world is automatically saved!
- Use the "Reset World" button to clear everything
