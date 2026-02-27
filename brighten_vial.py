#!/usr/bin/env python3
"""Brighten vial images - creates *_bright.png versions."""
from PIL import Image, ImageEnhance

def brighten_image(path):
    img = Image.open(path).convert("RGB")
    pixels = img.load()
    gamma = 0.7
    for y in range(img.height):
        for x in range(img.width):
            r, g, b = pixels[x, y]
            r = int(255 * (r / 255) ** gamma)
            g = int(255 * (g / 255) ** gamma)
            b = int(255 * (b / 255) ** gamma)
            pixels[x, y] = (min(255, r), min(255, g), min(255, b))
    enhancer = ImageEnhance.Brightness(img)
    img = enhancer.enhance(1.2)
    out = path.replace(".png", "_bright.png")
    img.save(out)
    print(f"Saved {out}")

for name in ["GoodVialMore.png", "HazardVialMore.png", "BrokenVialMore.png"]:
    brighten_image(f"photos/{name}")
