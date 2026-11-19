import sys, shutil
sys.path.insert(0, r"C:\Users\yusuf\AppData\Local\Temp\claude\ddc4959a59b64e86\170759c1-6726-4ee9-a655-d6a9b9f30954\scratchpad")
from hux_lib import *
HUX = ("Hux the honey badger exactly as in the reference, NOT a panda: long narrow snout, small flat ears close to the head, silver-white cap from the forehead over the head and down the back, "
       "face and cheeks black, thick expressive eyebrows")
PIP = "Pip the tiny brown honeyguide bird exactly as in the reference: round brown body, pale chest, huge shiny eyes, short pink beak, one cowlick feather on his head"
TAIL = " Stylized 3D animated feature-film look, warm golden light, cinematic 16:9, shallow depth of field, no text, no sharp teeth."
J = {
 "anahtar2_s04": (["hux_uyku.png", "pip.png"], f"Keep the sleeping Hux scene of image 1 ({HUX}), still fast asleep, eyes closed, same pose and burrow. Add {PIP} (image 2) standing on top of Hux's head, gently tugging his ear with his beak.{TAIL}", 44),
 "anahtar2_s05": (["hux_uyku.png", "pip.png"], f"Keep the burrow scene of image 1 with the sleeping Hux ({HUX}), curled up, eyes closed. Add {PIP} (image 2) hopping on Hux's round belly with wings raised, bouncing playfully.{TAIL}", 45),
 "anahtar2_s06": (["hux_uyku.png", "pip.png"], f"Close-up inside the burrow. Keep the sleeping Hux of image 1 ({HUX}), eyes closed. Add {PIP} (image 2) tiptoeing right next to Hux's ear, one wing cupped beside his beak like telling a secret.{TAIL}", 46),
 "anahtar2_s07a": (["hux_uyku.png"], f"Extreme close-up of the face of the sleeping Hux from image 1 ({HUX}), eyes closed and relaxed, the face fills most of the frame, burrow glow blurred behind.{TAIL}", 47),
}
for name, (imgs, p, s) in J.items():
    out, dt = run(qwen_edit(p, imgs, s, name))
    f = out["13"]["images"][0]["filename"]
    shutil.copy(rf"C:\ComfyUI\output\{f}", rf"C:\YoutubeVideo\YouTubeCalisma\uretim\b1\kareler\{name}.png")
    shutil.copy(rf"C:\ComfyUI\output\{f}", rf"C:\ComfyUI\input\{name}.png")
    print(name, round(dt), flush=True)
# s07 bitis: ayni kare, yalniz bir goz acik
p = ("Same image, same close-up framing, same character and lighting. Change only the eyes: only one eye (the eye nearest the camera) pops wide open, "
     "big, bright, alert and wide awake with a round iris; the other eye stays gently closed. Everything else identical." + TAIL)
out, dt = run(qwen_edit(p, ["anahtar2_s07a.png"], 48, "anahtar2_s07b"))
f = out["13"]["images"][0]["filename"]
shutil.copy(rf"C:\ComfyUI\output\{f}", r"C:\YoutubeVideo\YouTubeCalisma\uretim\b1\kareler\anahtar2_s07b.png")
shutil.copy(rf"C:\ComfyUI\output\{f}", r"C:\ComfyUI\input\anahtar2_s07b.png")
print("s07b", round(dt), flush=True)
