import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

def create_cyberpunk_image(text, filename, width=1200, height=400, bg_color=(10, 10, 15), text_color=(0, 255, 255), subheading=""):
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
    try:
        font = ImageFont.truetype("arial.ttf", 60)
        subfont = ImageFont.truetype("arial.ttf", 30)
    except IOError:
        font = ImageFont.load_default()
        subfont = ImageFont.load_default()
    
    # Main Text
    # Draw simple "Glow" effect
    text_width = len(text) * 30 # Approx width
    x_pos = width//2 - text_width
    y_pos = height//2 - 30

    for offset in range(4, 0, -1):
        draw.text((x_pos - offset, y_pos - offset), text, font=font, fill=(text_color[0]//2, text_color[1]//2, text_color[2]//2))
    
    draw.text((x_pos, y_pos), text, font=font, fill=text_color)
    
    # Subheading
    if subheading:
         draw.text((width//2 - len(subheading)*8, y_pos + 70), subheading, font=subfont, fill=(200, 200, 200))

    # Save
    if not os.path.exists("assets"):
        os.makedirs("assets")
    img.save(f"assets/{filename}")
    print(f"Generated {filename}")

def create_badge(text, filename, color=(255, 0, 255)):
    width = 300
    height = 80
    img = Image.new('RGB', (width, height), color=(0,0,0))
    draw = ImageDraw.Draw(img)
    
    # Border
    draw.rectangle([0, 0, width-1, height-1], outline=color, width=3)
    
    # Text
    try:
        font = ImageFont.truetype("arial.ttf", 30)
    except IOError:
        font = ImageFont.load_default()
        
    draw.text((20, 25), text, font=font, fill=color)
    
    if not os.path.exists("assets"):
        os.makedirs("assets")
    img.save(f"assets/{filename}")
    print(f"Generated {filename}")

# Generate Banner
create_cyberpunk_image("ABHAY POTLE", "banner.png", width=1500, height=500, text_color=(0, 255, 255), subheading="DIRECTED BY ABHAY POTLE")

# Generate Thumbnails
create_cyberpunk_image("PATIENT FLOW", "data_thumb.png", width=800, height=450, text_color=(50, 150, 255), subheading="HEALTHCARE ANALYTICS")
create_cyberpunk_image("HORROR ENGINE", "horror_thumb.png", width=800, height=450, text_color=(255, 50, 50), subheading="INTERACTIVE WEB")
create_cyberpunk_image("NEON BLOCKS", "game_thumb.png", width=800, height=450, text_color=(200, 0, 255), subheading="AI HAND CONTROL")

# New Assets
create_badge("VIBE CODING", "vibe_coding.png", color=(255, 0, 255))
create_cyberpunk_image("SYSTEM SPECS", "specs_panel.png", width=1000, height=300, text_color=(0, 255, 0), subheading="3D HOLOGRAPHIC SCAN COMPLETE")
