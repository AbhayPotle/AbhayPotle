import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

def create_cyberpunk_image(text, filename, width=1200, height=400, bg_color=(10, 10, 15), text_color=(0, 255, 255)):
    # Create base image
    img = Image.new('RGB', (width, height), color=bg_color)
    draw = ImageDraw.Draw(img)

    # Add "Cyberpunk" grid
    for x in range(0, width, 40):
        draw.line([(x, 0), (x, height)], fill=(20, 20, 30), width=1)
    for y in range(0, height, 40):
        draw.line([(0, y), (width, y)], fill=(20, 20, 30), width=1)

    # Add random "glitch" rectangles
    for _ in range(20):
        x1 = random.randint(0, width)
        y1 = random.randint(0, height)
        x2 = x1 + random.randint(10, 100)
        y2 = y1 + random.randint(2, 10)
        color = random.choice([(0, 255, 255), (255, 0, 255), (0, 255, 0)])
        draw.rectangle([x1, y1, x2, y2], fill=color)

    # Draw Text (Centered)
    # Using default font since we can't guarantee a custom font
    try:
        font = ImageFont.truetype("arial.ttf", 60)
    except IOError:
        font = ImageFont.load_default()
    
    # Calculate text position (basic centering)
    # PIL GetBBox
    
    # Draw simple "Glow" effect by drawing text multiple times with offset
    for offset in range(4, 0, -1):
        draw.text((width//2 - len(text)*15 - offset, height//2 - 30 - offset), text, font=font, fill=(color[0]//2, color[1]//2, color[2]//2))
    
    draw.text((width//2 - len(text)*15, height//2 - 30), text, font=font, fill=text_color)
    
    # Save
    if not os.path.exists("assets"):
        os.makedirs("assets")
    img.save(f"assets/{filename}")
    print(f"Generated {filename}")

# Generate Banner
create_cyberpunk_image("ABHAY POTLE", "banner.png", width=1500, height=500, text_color=(0, 255, 255))

# Generate Thumbnails
create_cyberpunk_image("PATIENT FLOW", "data_thumb.png", width=800, height=450, text_color=(50, 150, 255))
create_cyberpunk_image("HORROR ENGINE", "horror_thumb.png", width=800, height=450, text_color=(255, 50, 50))
create_cyberpunk_image("NEON BLOCKS", "game_thumb.png", width=800, height=450, text_color=(200, 0, 255))
