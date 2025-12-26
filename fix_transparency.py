from PIL import Image
import os

def make_black_transparent(image_path, threshold=30):
    """Convert black pixels to transparent"""
    img = Image.open(image_path)
    
    if img.mode != 'RGBA':
        img = img.convert('RGBA')
    
    pixels = img.load()
    width, height = img.size
    
    changed_count = 0
    for y in range(height):
        for x in range(width):
            r, g, b, a = pixels[x, y]
            # If pixel is very dark (black-ish), make it transparent
            if r < threshold and g < threshold and b < threshold:
                pixels[x, y] = (r, g, b, 0)  # Set alpha to 0
                changed_count += 1
    
    img.save(image_path)
    return changed_count

# List of textures that need transparency
textures_to_fix = [
    'oak_leaves.png',
    'red_flower.png',
    'yello_flower.png',  # Typo in filename
    'tall_grass.png',
    'fern.png',
    'dead_bush.png',
    'sapling.png',
    'oak_sapling.png'
]

print('Making black pixels transparent...\n')

for texture_name in textures_to_fix:
    texture_path = f'textures/{texture_name}'
    if os.path.exists(texture_path):
        try:
            count = make_black_transparent(texture_path, threshold=40)
            print(f'✓ {texture_name}: Made {count} pixels transparent')
        except Exception as e:
            print(f'✗ {texture_name}: Error - {e}')
    else:
        print(f'- {texture_name}: File not found')

print('\nDone! Refresh your browser to see the changes.')
