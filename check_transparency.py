from PIL import Image

# Check oak_leaves
img = Image.open('textures/oak_leaves.png')
print(f'Oak Leaves - Mode: {img.mode}')
print(f'Size: {img.size}')

# Check if has transparency
if img.mode == 'RGBA':
    pixels = list(img.getdata())
    # Find black pixels
    black_pixels = [p for p in pixels if p[0] < 30 and p[1] < 30 and p[2] < 30]
    if black_pixels:
        print(f'Found {len(black_pixels)} black-ish pixels')
        print(f'Sample black pixel: {black_pixels[0]} (R,G,B,A)')
        if black_pixels[0][3] == 255:
            print('BLACK PIXELS ARE OPAQUE - Need to make them transparent!')
    else:
        print('No black pixels found')
else:
    print('Image does not have alpha channel!')

# Check flower
try:
    flower_img = Image.open('textures/red_flower.png')
    print(f'\nRed Flower - Mode: {flower_img.mode}')
    if flower_img.mode == 'RGBA':
        pixels = list(flower_img.getdata())
        black_pixels = [p for p in pixels if p[0] < 30 and p[1] < 30 and p[2] < 30]
        if black_pixels:
            print(f'Found {len(black_pixels)} black-ish pixels')
            print(f'Sample: {black_pixels[0]} (R,G,B,A)')
except Exception as e:
    print(f'Could not check flower: {e}')
