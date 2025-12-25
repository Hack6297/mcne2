# Deployment Guide for Minecraft Nesa Explorer 5 Edition

## Quick Deploy to Render

### Prerequisites
1. GitHub account
2. Render account (free tier works)

### Step 1: Push to GitHub
```bash
cd "c:\Users\Admin\Documents\Minecraft-3D-Game"
git init
git add vanilla.html render.yaml textures/ index-nesa.html README-NESA.md
git commit -m "Initial commit - Minecraft Nesa Explorer 5 Edition"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/minecraft-nesa-explorer-5.git
git push -u origin main
```

### Step 2: Deploy on Render
1. Go to https://render.com
2. Click "New +" → "Static Site"
3. Connect your GitHub repository
4. Render will auto-detect the `render.yaml` configuration
5. Click "Create Static Site"
6. Wait for deployment (usually 1-2 minutes)

### Alternative: Manual Configuration
If auto-detect doesn't work:
- **Build Command**: `echo "No build needed"`
- **Publish Directory**: `.`
- **Redirect Rule**: `/* → /vanilla.html`

### Step 3: Access Your Game
Once deployed, Render will provide a URL like:
`https://minecraft-nesa-explorer-5.onrender.com`

## Files Required for Deployment
- ✅ `vanilla.html` - Main game file
- ✅ `render.yaml` - Render configuration
- ✅ `textures/` - All texture PNG files (27 textures)
- ✅ `index-nesa.html` - Landing page with redirect
- ✅ `README-NESA.md` - Documentation

## Important Notes
- All textures must be in the `textures/` folder
- Three.js is loaded from CDN (no local files needed)
- Game is fully static - no server needed
- Free tier on Render works perfectly

## Troubleshooting
**Textures not loading?**
- Ensure all 27 PNG files are in `textures/` folder
- Check file names match exactly (case-sensitive)

**Game not loading?**
- Check browser console for errors
- Ensure Three.js CDN is accessible
- Try hard refresh (Ctrl+Shift+R)

## Custom Domain (Optional)
1. In Render dashboard, go to your static site
2. Click "Settings" → "Custom Domain"
3. Add your domain and configure DNS

Enjoy your deployed Minecraft Nesa Explorer 5 Edition! 🎮⛏️
