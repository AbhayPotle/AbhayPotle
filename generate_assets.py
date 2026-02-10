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
create_cyberpunk_image("SYSTEM SPECS", "specs_panel.png", width=1000, height=300, text_color=(0, 255, 0), subheading="3D HOLOGRAPHIC SCAN COMPLETE")

def create_cinematic_dashboard(filename):
    width = 1200
    height = 600
    bg_color = (2, 4, 8)
    img = Image.new('RGB', (width, height), color=bg_color)
    draw = ImageDraw.Draw(img, 'RGBA')

    # Perspective Grid Floor
    for i in range(0, 300, 20):
        y = 400 + i
        alpha = int(255 * (1 - i/300))
        draw.line([(0, y), (width, y)], fill=(0, 255, 255, alpha), width=1)
    
    for i in range(-600, 1800, 100):
        alpha = 100
        draw.line([(width//2, 200), (i, 600)], fill=(0, 255, 255, alpha), width=1)

    # Glowing Abstract Waves (Pseudo 3D)
    import math
    for x in range(0, width, 5):
        for layer in range(3):
            y_offset = math.sin(x * 0.01 + layer) * 50
            y = 250 + y_offset + (layer * 20)
            color = [(0, 150, 255, 50), (255, 0, 255, 50), (0, 255, 150, 50)][layer]
            draw.ellipse([x-2, y-2, x+2, y+2], fill=color)

    # Vertical Digital Pillars
    pillars = [(200, 150, (0, 200, 255)), (400, 250, (255, 0, 255)), (600, 200, (0, 255, 0)), (800, 300, (255, 100, 0)), (1000, 180, (255, 255, 0))]
    for px, ph, pcol in pillars:
        # Glow
        for g in range(5, 20, 5):
            draw.rectangle([px-g, 400-ph-g, px+40+g, 400+g], outline=(pcol[0], pcol[1], pcol[2], 30), width=1)
        # Main Pillar
        draw.rectangle([px, 400-ph, px+40, 400], fill=(pcol[0], pcol[1], pcol[2], 180))
        # Top Flare
        draw.ellipse([px-10, 400-ph-10, px+50, 400-ph+10], fill=(255, 255, 255, 100))

    # Floating UI elements (Abstract)
    for i in range(10):
        rx, ry = 50 + i*110, 50 + (i%3)*40
        draw.rectangle([rx, ry, rx+80, ry+30], outline=(0, 255, 255, 100), width=1)
        draw.line([(rx+5, ry+15), (rx+75, ry+15)], fill=(0, 255, 255, 150), width=2)

    # Scanline Overlay
    for y in range(0, height, 4):
        draw.line([(0, y), (width, y)], fill=(255, 255, 255, 10), width=1)

    # Vignette
    for i in range(100):
        alpha = int(150 * (i/100))
        draw.rectangle([0,0,width,height], outline=(0,0,0,alpha), width=100-i)

    if not os.path.exists("assets"):
        os.makedirs("assets")
    img.save(f"assets/{filename}")
    print(f"Generated {filename}")

create_cinematic_dashboard("analysis_dashboard.png")
create_badge("VIBE CODING", "vibe_coding.png", color=(255, 0, 255))
