import os
import base64
from io import BytesIO
from PIL import Image

src_dir = r"C:\Users\Jayjean\.gemini\antigravity-ide\brain\9f548728-14eb-49c4-884a-7bb49bc81661\.user_uploaded"

p_recomp = os.path.join(src_dir, "media_1789909695951.png")
p_fatloss = os.path.join(src_dir, "media_1789909724203.png")
p_muscle = os.path.join(src_dir, "media_1789909741573.jpg")

# 1. Recomposition:
im_recomp = Image.open(p_recomp).convert("RGB")
w, h = im_recomp.size
# Check top brown border: crop top 6px and bottom 2px if needed
# Let's crop: left=0, top=6, right=w, bottom=h
im_recomp_cropped = im_recomp.crop((0, 6, w, h))

# 2. Fat loss:
im_fatloss = Image.open(p_fatloss).convert("RGB")
w, h = im_fatloss.size
# Left arrow is in the leftmost 20-25px. Crop 24px from left, 4px from right, 4px from bottom
im_fatloss_cropped = im_fatloss.crop((24, 0, w - 4, h - 2))

# 3. Muscle gain:
im_muscle = Image.open(p_muscle).convert("RGB")
w, h = im_muscle.size
# Left arrow is ~28px from left, right arrow is ~28px from right. Bottom has dots (~15px)
im_muscle_cropped = im_muscle.crop((28, 0, w - 28, h - 16))

# Helper to resize proportionally if too large (e.g. max dim 750) and convert to base64 JPEG
def to_base64_jpg(img, max_w=720, quality=84):
    w, h = img.size
    if w > max_w:
        ratio = max_w / float(w)
        new_h = int(h * ratio)
        img = img.resize((max_w, new_h), Image.Resampling.LANCZOS)
    buf = BytesIO()
    img.save(buf, format="JPEG", quality=quality, optimize=True)
    b64 = base64.b64encode(buf.getvalue()).decode("utf-8")
    return f"data:image/jpeg;base64,{b64}"

b64_recomp = to_base64_jpg(im_recomp_cropped)
b64_fatloss = to_base64_jpg(im_fatloss_cropped)
b64_muscle = to_base64_jpg(im_muscle_cropped)

import json
data = {
    "fatloss": b64_fatloss,
    "muscle": b64_muscle,
    "recomp": b64_recomp
}

with open("images_b64.json", "w") as f:
    json.dump(data, f)

print(f"Successfully processed images. Sizes: fatloss={len(b64_fatloss)}, muscle={len(b64_muscle)}, recomp={len(b64_recomp)}")
