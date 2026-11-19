import sys, shutil
sys.path.insert(0, r"C:\Users\yusuf\AppData\Local\Temp\claude\ddc4959a59b64e86\170759c1-6726-4ee9-a655-d6a9b9f30954\scratchpad")
from hux_lib import *
S = "Stylized 3D animated feature-film look, warm golden light, cute friendly mood. No music, no subtitles, no on-screen text."
p = ("Extreme close-up of sleeping Hux's face, a wink-like gag. Perfectly still with both eyes closed for the first four seconds, only faint breathing. "
     "Then ONLY the single eye nearest the camera slowly opens wide and stays open, alert; the other eye stays tightly shut the whole time. Slow push-in. " + S)
out, dt = run(wan_flf(p, "anahtar2_s07a.png", "anahtar2_s07b.png", 20261217, "taslak2_s07_r2"))
f = out["17"]["images"][0]["filename"]
shutil.copy(rf"C:\ComfyUI\output\video\{f}", r"C:\YoutubeVideo\YouTubeCalisma\uretim\b1\klipler\taslak2_s07_r2.mp4")
print("s07_r2 ok", round(dt), flush=True)
