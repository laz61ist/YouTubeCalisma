import sys, shutil
sys.path.insert(0, r"C:\Users\yusuf\AppData\Local\Temp\claude\ddc4959a59b64e86\170759c1-6726-4ee9-a655-d6a9b9f30954\scratchpad")
from hux_lib import *
T = " Stylized 3D animated feature-film look, warm golden light, cinematic 16:9, shallow depth of field, no text, no sharp teeth."
H = "Image 1 shows Hux the honey badger asleep in his burrow: keep him, his body, his curled pose and the whole burrow EXACTLY unchanged (black face, silver cap, long narrow snout, small flat ears, eyes closed)."
J = {
 "s04": f"{H} Add exactly ONE small brown bird, Pip (image 2), standing on top of Hux's head, gently tugging Hux's ear with his beak. Only one bird in the picture.{T}",
 "s05": f"{H} Add exactly ONE small brown bird, Pip (image 2), standing on Hux's furry back, wings raised, ready to bounce. Hux's body stays black and furry. Only one bird in the picture.{T}",
}
for name, p in J.items():
    for s in (61, 62):
        out, dt = run(qwen_edit(p, ["hux_uyku.png", "pip.png"], s, f"anahtar3_{name}_{s}"))
        f = out["13"]["images"][0]["filename"]
        shutil.copy(rf"C:\ComfyUI\output\{f}", rf"C:\YoutubeVideo\YouTubeCalisma\uretim\b1\kareler\anahtar3_{name}_{s}.png")
        print(name, s, round(dt), flush=True)
