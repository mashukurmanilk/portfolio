import os, math
from PIL import Image, ImageDraw, ImageFont

os.makedirs('assets', exist_ok=True)

def create_mockup(title, subtitle, tag, icon_text, accent_color, card_bg_theme, output_path):
    w, h = 900, 520
    im = Image.new('RGB', (w, h), color=(16, 12, 14))
    draw = ImageDraw.Draw(im)
    
    # Subtle gradient background
    c1, c2 = card_bg_theme
    for y in range(h):
        ratio = y / h
        r = int(c1[0] * (1 - ratio) + c2[0] * ratio)
        g = int(c1[1] * (1 - ratio) + c2[1] * ratio)
        b = int(c1[2] * (1 - ratio) + c2[2] * ratio)
        draw.line([(0, y), (w, y)], fill=(r, g, b))
    
    # Futuristic subtle grid
    for x in range(0, w, 40):
        draw.line([(x, 0), (x, h)], fill=(45, 25, 30))
    for y in range(0, h, 40):
        draw.line([(0, y), (w, y)], fill=(45, 25, 30))
        
    # Main browser/app container
    draw.rounded_rectangle([30, 25, w - 30, h - 25], radius=16, fill=(20, 14, 18), outline=(84, 13, 19), width=2)
    # Header bar
    draw.rounded_rectangle([30, 25, w - 30, 75], radius=16, fill=(35, 18, 25))
    draw.rectangle([30, 55, w - 30, 75], fill=(35, 18, 25))
    
    # Window controls (macOS style dots)
    draw.ellipse([50, 42, 64, 56], fill=(239, 68, 68))
    draw.ellipse([74, 42, 88, 56], fill=(245, 158, 11))
    draw.ellipse([98, 42, 112, 56], fill=(34, 197, 94))
    
    # URL bar
    draw.rounded_rectangle([140, 36, w - 60, 64], radius=8, fill=(15, 10, 13), outline=(65, 20, 25), width=1)
    slug = title.lower().replace(' ', '-').replace('(', '').replace(')', '')
    draw.text((160, 42), f"https://{slug}.portfolio-live.app", fill=(190, 180, 175))
    
    # Content Area
    # Sidebar
    draw.rounded_rectangle([50, 95, 220, h - 45], radius=12, fill=(28, 16, 22), outline=(55, 18, 24), width=1)
    draw.rounded_rectangle([65, 115, 205, 150], radius=8, fill=(84, 13, 19))
    draw.text((75, 125), f"{icon_text}  {title[:10]}", fill=(245, 158, 11))
    
    for i in range(5):
        y_pos = 170 + i * 38
        draw.rounded_rectangle([65, y_pos, 205, y_pos + 26], radius=6, fill=(40, 22, 28))
        draw.rectangle([75, y_pos + 10, 110, y_pos + 16], fill=(130, 70, 80))
        
    # Main hero banner inside app
    main_x1 = 240
    main_w = w - 50 - main_x1
    draw.rounded_rectangle([main_x1, 95, w - 50, 220], radius=12, fill=(45, 16, 24), outline=(138, 28, 36), width=1)
    
    # Decorative glow circle inside banner
    draw.ellipse([w - 180, 105, w - 70, 210], fill=(74, 14, 19))
    draw.text((main_x1 + 25, 115), title, fill=(245, 158, 11))
    draw.text((main_x1 + 25, 145), subtitle, fill=(230, 220, 225))
    
    # Badge
    draw.rounded_rectangle([main_x1 + 25, 175, main_x1 + 160, 202], radius=14, fill=(245, 158, 11))
    draw.text((main_x1 + 40, 182), tag, fill=(18, 12, 14))
    
    # Stats badge
    draw.rounded_rectangle([main_x1 + 180, 175, main_x1 + 310, 202], radius=14, fill=(74, 14, 19), outline=(245, 158, 11), width=1)
    draw.text((main_x1 + 195, 182), "Active / Deployed", fill=(245, 158, 11))
    
    # 3 Feature / Metric cards below
    cards_y1 = 240
    card_spacing = 15
    single_card_w = (main_w - (card_spacing * 2)) // 3
    
    features = [
        ("Dashboard Analytics", "Real-time metrics, interactive state synchronization"),
        ("Secured Architecture", "JWT auth tokens, strict route validation"),
        ("Responsive Layout", "Tailwind CSS fluid grid system & micro-animations")
    ]
    
    for idx, (f_title, f_desc) in enumerate(features):
        c_x1 = main_x1 + idx * (single_card_w + card_spacing)
        c_x2 = c_x1 + single_card_w
        c_y2 = h - 45
        
        draw.rounded_rectangle([c_x1, cards_y1, c_x2, c_y2], radius=10, fill=(30, 18, 24), outline=(75, 20, 28), width=1)
        
        # Mini thumbnail inside card
        draw.rounded_rectangle([c_x1 + 12, cards_y1 + 12, c_x2 - 12, cards_y1 + 105], radius=6, fill=(55, 18, 26))
        # Mini accent bar
        draw.rectangle([c_x1 + 12, cards_y1 + 100, c_x2 - 12, cards_y1 + 105], fill=(245, 158, 11))
        
        draw.text((c_x1 + 14, cards_y1 + 120), f_title, fill=(245, 158, 11))
        
        # Text placeholder lines
        draw.rounded_rectangle([c_x1 + 14, cards_y1 + 145, c_x2 - 14, cards_y1 + 153], radius=3, fill=(160, 130, 140))
        draw.rounded_rectangle([c_x1 + 14, cards_y1 + 160, c_x2 - 30, cards_y1 + 168], radius=3, fill=(110, 85, 95))
        draw.rounded_rectangle([c_x1 + 14, cards_y1 + 175, c_x2 - 40, cards_y1 + 183], radius=3, fill=(80, 60, 70))
        
        # Action button
        draw.rounded_rectangle([c_x1 + 14, c_y2 - 35, c_x2 - 14, c_y2 - 12], radius=5, fill=(84, 13, 19), outline=(138, 28, 36), width=1)
        draw.text((c_x1 + (single_card_w // 2) - 30, c_y2 - 29), "Inspect", fill=(255, 255, 255))
        
    im.save(output_path, 'PNG')
    print('Generated mockup:', output_path)

# Generate project mockups
create_mockup(
    'BookNook Library',
    'Full-Stack Digital Library & Management System',
    'MERN + NEXT.JS',
    '[BOOKS]',
    '#F59E0B',
    ((22, 12, 16), (48, 14, 22)),
    'assets/project-booknook.png'
)

create_mockup(
    'Private Cloud Vault',
    'Self-Hosted Personal Media Hub & Document Storage',
    'NEXT.JS 14 + PRISMA',
    '[VAULT]',
    '#F59E0B',
    ((20, 14, 26), (42, 16, 32)),
    'assets/project-vault.png'
)

create_mockup(
    'Cyber-HUD Data Nexus',
    'Gamified Productivity Suite & Web Audio Terminal',
    'REACT + VITE',
    '[CYBER]',
    '#F59E0B',
    ((16, 22, 24), (28, 42, 36)),
    'assets/project-cyberhud.png'
)

create_mockup(
    'B14 BPL Dream 11',
    'Fantasy Cricket Team Builder & Budget Manager',
    'REACT + DAISYUI',
    '[CRICKET]',
    '#F59E0B',
    ((28, 16, 18), (60, 26, 18)),
    'assets/project-bpldream.png'
)

create_mockup(
    'Bazar Dor Tracker',
    'Commodity Price Tracker & Household Budget Assistant',
    'FULL STACK REST',
    '[MARKET]',
    '#F59E0B',
    ((24, 18, 14), (52, 28, 16)),
    'assets/project-bazardor.png'
)

# Also generate a sleek developer profile avatar
def create_avatar(output_path):
    size = 400
    im = Image.new('RGBA', (size, size), color=(0, 0, 0, 0))
    draw = ImageDraw.Draw(im)
    
    # Outer glowing sun ring
    draw.ellipse([10, 10, size - 10, size - 10], outline=(245, 158, 11, 220), width=6)
    draw.ellipse([18, 18, size - 18, size - 18], outline=(138, 28, 36, 180), width=4)
    
    # Inner background circle (deep maroon gradient)
    draw.ellipse([26, 26, size - 26, size - 26], fill=(42, 12, 18, 255))
    
    # Silhouette / Developer icon
    # Head
    draw.ellipse([140, 90, 260, 210], fill=(235, 195, 160))
    # Hair / modern cut
    draw.chord([130, 75, 270, 170], 180, 360, fill=(40, 25, 20))
    draw.ellipse([135, 80, 265, 140], fill=(40, 25, 20))
    
    # Glasses (modern developer specs)
    draw.rounded_rectangle([155, 135, 195, 165], radius=6, outline=(245, 158, 11), width=4)
    draw.rounded_rectangle([205, 135, 245, 165], radius=6, outline=(245, 158, 11), width=4)
    draw.line([(195, 150), (205, 150)], fill=(245, 158, 11), width=4)
    
    # Smile
    draw.arc([180, 165, 220, 195], 20, 160, fill=(180, 90, 70), width=4)
    
    # Shoulders / hoodie (maroon with gold trim)
    draw.chord([60, 220, 340, 480], 180, 360, fill=(84, 13, 19))
    draw.arc([90, 220, 310, 480], 200, 340, fill=(245, 158, 11), width=4)
    
    # Gold badge: MM
    draw.ellipse([175, 290, 225, 340], fill=(245, 158, 11))
    draw.text((186, 305), "MM", fill=(18, 12, 14))
    
    im.save(output_path, 'PNG')
    print('Generated avatar:', output_path)

create_avatar('assets/profile-avatar.png')
print('All asset generation complete!')
