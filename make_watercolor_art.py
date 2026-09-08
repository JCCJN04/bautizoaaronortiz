from PIL import Image, ImageFilter, ImageDraw
import numpy as np
import random

# Ratio 4:5 -> 800 x 1000
w, h = 800, 1000
canvas = Image.new('RGB', (w, h), (245, 239, 230)) # warm linen cream #F5EFE6

# Linen subtle grain
for y in range(h):
    for x in range(w):
        noise = random.randint(-4, 4)
        canvas.putpixel((x, y), (245 + noise, 239 + noise, 230 + noise))

draw = ImageDraw.Draw(canvas)

# Delicate antique gold leaf splatters
random.seed(42)
for _ in range(70):
    sx = random.randint(40, w - 40)
    sy = random.randint(40, h - 40)
    s_size = random.randint(1, 4)
    # antique gold #C6A052
    draw.ellipse((sx, sy, sx + s_size, sy + s_size), fill=(198 + random.randint(-15, 15), 160 + random.randint(-15, 15), 82 + random.randint(-10, 10)))

# Elegant fine ink border
draw.rectangle((30, 30, w - 30, h - 30), outline=(198, 160, 82), width=1)
draw.rectangle((36, 36, w - 36, h - 36), outline=(62, 80, 51), width=1)

# Subtle watercolor washes in sage, olive, dusty navy, and soft crimson
overlay = Image.new('RGBA', (w, h), (0, 0, 0, 0))
o_draw = ImageDraw.Draw(overlay)

# Soft watercolor circles / washes
# Sage/Olive wash top
o_draw.ellipse((w*0.2, h*0.2, w*0.8, h*0.6), fill=(110, 132, 96, 40))
# Dusty navy wash left
o_draw.ellipse((w*0.1, h*0.35, w*0.55, h*0.75), fill=(70, 95, 130, 35))
# Soft crimson wash right
o_draw.ellipse((w*0.45, h*0.35, w*0.9, h*0.75), fill=(180, 85, 85, 35))
# Antique gold glow center
o_draw.ellipse((w*0.3, h*0.4, w*0.7, h*0.7), fill=(210, 175, 95, 50))

overlay = overlay.filter(ImageFilter.GaussianBlur(45))
canvas = Image.alpha_composite(canvas.convert('RGBA'), overlay).convert('RGB')

# Save initial watercolor illustration
canvas.save('watercolor_avengers.jpg', quality=95)
print('watercolor_avengers.jpg created!')
