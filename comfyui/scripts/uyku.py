import sys, shutil
sys.path.insert(0, r"C:\Users\yusuf\AppData\Local\Temp\claude\ddc4959a59b64e86\170759c1-6726-4ee9-a655-d6a9b9f30954\scratchpad")
from hux_lib import *
P = ("Keep the exact character from image 1: Hux the honey badger, NOT a panda: long narrow snout, small flat ears close to the head with a small notch in the left ear, "
     "the silver-white fur is a cap from the forehead over the top of the head and down the back like a cape, the face, cheeks and the area around the eyes are black, "
     "thick expressive eyebrows, wry lopsided smile. Place him in the burrow of image 2: Hux is fast asleep, curled up in a loose ball on the bed of dry grass, eyes gently closed "
     "(eyelids relaxed, eyebrows visible), head resting on his front paws, side three-quarter view. Warm golden light from the round entrance. "
     "Stylized 3D animated feature-film look, cinematic 16:9, shallow depth of field, no text, no sharp teeth.")
for s in (501, 502, 503, 504):
    out, dt = run(qwen_edit(P, ["hux.png", "env_burrow.png"], s, f"hux_uyku_{s}"))
    f = out["13"]["images"][0]["filename"]
    shutil.copy(rf"C:\ComfyUI\output\{f}", rf"C:\YoutubeVideo\YouTubeCalisma\uretim\b1\kareler\hux_uyku_{s}.png")
    print(s, round(dt), flush=True)
