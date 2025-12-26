from PIL import Image
import os

# Load the texture atlas
atlas = Image.open('texture_atlas.png')
width, height = atlas.size

# Block size (standard Minecraft texture)
BLOCK_SIZE = 32

# Calculate grid dimensions
cols = width // BLOCK_SIZE
rows = height // BLOCK_SIZE

print(f"Image size: {width}x{height}")
print(f"Block size: {BLOCK_SIZE}x{BLOCK_SIZE}")
print(f"Grid: {cols}x{rows} = {cols * rows} blocks")

# Create output directory
output_dir = 'extracted_blocks'
os.makedirs(output_dir, exist_ok=True)

# Common Minecraft block names (based on typical texture atlas layout)
# You can customize these names based on what you see in the image
block_names = [
    # Row 0
    'stone', 'cobblestone', 'bedrock', 'sand', 'gravel', 'wood_oak', 'wood_spruce', 'wood_birch',
    'iron_ore', 'gold_ore', 'diamond_ore', 'coal_ore', 'sponge', 'glass', 'white_cloth', 'red_cloth',
    # Row 1
    'orange_cloth', 'yellow_cloth', 'lime_cloth', 'green_cloth', 'cyan_cloth', 'blue_cloth', 'purple_cloth', 'magenta_cloth',
    'pink_cloth', 'black_cloth', 'gray_cloth', 'light_gray_cloth', 'brick', 'tnt_side', 'tnt_top', 'tnt_bottom',
    # Row 2
    'web', 'flower_red', 'flower_yellow', 'mushroom_red', 'mushroom_brown', 'sapling_oak', 'fire_layer_0', 'fire_layer_1',
    'redstone_ore', 'lapis_ore', 'lapis_block', 'dispenser_front', 'sandstone_side', 'sandstone_top', 'sandstone_bottom', 'wool',
    # Add more rows as needed
]

# Extract each block
block_index = 0
for row in range(rows):
    for col in range(cols):
        # Calculate block position
        left = col * BLOCK_SIZE
        top = row * BLOCK_SIZE
        right = left + BLOCK_SIZE
        bottom = top + BLOCK_SIZE
        
        # Extract block
        block = atlas.crop((left, top, right, bottom))
        
        # Generate filename
        if block_index < len(block_names):
            filename = f"{block_names[block_index]}.png"
        else:
            filename = f"block_{row}_{col}.png"
        
        # Save block
        filepath = os.path.join(output_dir, filename)
        block.save(filepath)
        
        print(f"Saved: {filename} (row {row}, col {col})")
        block_index += 1

print(f"\n✓ Extracted {block_index} blocks to '{output_dir}/' folder")
