"""Build image assets for Yuki Ep.01 from the three reference images (deterministic)."""
import sys
from pathlib import Path
from PIL import Image, ImageFilter, ImageEnhance, ImageChops
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
REFS = ROOT.parents[1] / "storyboards" / "yuki-chicken-teriyaki" / "refs"
OUT = ROOT / "assets" / "img"
OUT.mkdir(parents=True, exist_ok=True)

def up(im, scale):
    im = im.resize((round(im.width * scale), round(im.height * scale)), Image.LANCZOS)
    return im.filter(ImageFilter.UnsharpMask(radius=2, percent=60, threshold=2))

def save(im, name, q=92):
    im.convert("RGB").save(OUT / name, quality=q)
    print(name, im.size)

# --- Kitchen: sunny -> gentle rainy afternoon --------------------------------
k = Image.open(REFS / "02-kitchen.jpg").convert("RGB")
a = np.asarray(k).astype(np.float32) / 255.0
h, w, _ = a.shape
yy, xx = np.mgrid[0:h, 0:w]
# window opening (exterior) region, feathered
win = ((xx > 30) & (xx < 492) & (yy > 20) & (yy < 612)).astype(np.float32)
win_img = Image.fromarray((win * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(10))
win = np.asarray(win_img).astype(np.float32)[..., None] / 255.0
r, g, b = a[..., 0], a[..., 1], a[..., 2]
lum = (0.299 * r + 0.587 * g + 0.114 * b)[..., None]
grey_blue = np.array([0.58, 0.63, 0.69])
# exterior: desaturate, cool, darken, add mist that grows toward the horizon
ext = lum * 0.55 + a * 0.25 + grey_blue * 0.30
sky = ((b > r + 0.12) & (b > g + 0.02)).astype(np.float32)[..., None]
sky = np.asarray(Image.fromarray((sky[..., 0] * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(3))).astype(np.float32)[..., None] / 255.0
overcast = np.array([0.70, 0.73, 0.77]) * (0.92 + 0.08 * lum)
ext = ext * (1 - sky) + overcast * sky
mist = np.clip((yy - 250) / 200.0, 0, 1) * np.clip((470 - yy) / 120.0, 0, 1)
ext = ext * (1 - 0.25 * mist[..., None]) + np.array([0.78, 0.81, 0.85]) * 0.25 * mist[..., None]
ext = ext * 0.9
# interior: remove hard sunlight a touch, keep it warm and golden
inte = a * np.array([1.02, 0.97, 0.88]) * 0.93
out = ext * win + inte * (1 - win)
kr = Image.fromarray((np.clip(out, 0, 1) * 255).astype(np.uint8))
save(up(kr, 2), "kitchen_rainy.jpg")
# close crops (from the 2x image)
K2 = up(kr, 2)
save(K2.crop((60, 860, 760, 1380)), "dog.jpg")                 # golden retriever at the window
save(K2.crop((1260, 1040, 1472, 1560)), "stove.jpg")          # stove and pot
save(K2.crop((20, 0, 720, 1244)), "window.jpg")               # window, vines, view (no figure)

# --- Yuki ------------------------------------------------------------------------
y = Image.open(REFS / "01-character-yuki.jpg").convert("RGB")
save(up(y, 2), "yuki.jpg")

# --- Recipe crops -----------------------------------------------------------------
rc = Image.open(REFS / "03-recipe.jpg").convert("RGB")
crops = {
    "bowl_hero.jpg": (0, 40, 292, 332),
    "tools.jpg": (262, 372, 480, 572),
    "list_chicken.jpg": (14, 372, 258, 476),
    "list_sauce.jpg": (14, 482, 258, 584),
    "list_serve.jpg": (14, 588, 258, 690),
    "step1.jpg": (34, 726, 126, 792),
    "step2.jpg": (152, 726, 248, 792),
    "step3.jpg": (272, 726, 368, 792),
    "step4.jpg": (390, 726, 486, 792),
    "step5.jpg": (506, 726, 602, 792),
    "step6.jpg": (624, 726, 720, 792),
}
for name, box in crops.items():
    im = rc.crop(box)
    s = 4 if name.startswith(("bowl", "tools", "list")) else 5
    save(up(im, s), name)

# --- Pre-blurred backgrounds + paper grain (cheaper than CSS filters at render time) ----
kit = Image.open(OUT / "kitchen_rainy.jpg")
kb = kit.resize((540, 810), Image.LANCZOS).filter(ImageFilter.GaussianBlur(9))
kb = ImageEnhance.Brightness(kb).enhance(0.82)
save(kb.resize((1080, 1620), Image.LANCZOS), "kitchen_blur.jpg", q=85)
wb = Image.open(OUT / "window.jpg").resize((350, 622), Image.LANCZOS).filter(ImageFilter.GaussianBlur(7))
save(wb.resize((1080, 1920), Image.LANCZOS), "window_blur.jpg", q=85)
g = np.random.default_rng(7).normal(128, 38, (512, 512)).clip(0, 255).astype(np.uint8)
Image.fromarray(g, "L").save(OUT / "grain.png")
print("grain.png (512, 512)")
