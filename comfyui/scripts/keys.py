import sys, shutil
sys.path.insert(0, r"C:\Users\yusuf\AppData\Local\Temp\claude\ddc4959a59b64e86\170759c1-6726-4ee9-a655-d6a9b9f30954\scratchpad")
from hux_lib import *

HUX = ("Hux the honey badger exactly as in the reference: entire face, muzzle and cheeks solid BLACK fur, thick silver-white stripe only on top of the head and down the back, "
       "black legs, belly and tail, small round ears with a small notch in the left ear")
PIP = "Pip the tiny brown honeyguide bird exactly as in the reference: round brown body, pale chest, huge shiny eyes, short pink beak, one cowlick feather on his head"
TAIL = " Stylized 3D animated feature-film look, warm golden light, cinematic 16:9, shallow depth of field, no text, no sharp teeth."

SCENES = {
    2: (["pip.png", "env_valley.png"], f"Place {PIP} (image 1) into the valley scene (image 2): Pip is landing with a bounce on the grass right in front of the small round burrow entrance between the pine roots, wings spread, excited. Keep the scene of image 2.{TAIL}"),
    4: (["hux_s03_key.png", "pip.png"], f"Keep the sleeping Hux scene of image 1 ({HUX}), still fast asleep with eyes closed. Add {PIP} (image 2) standing on top of Hux's head, gently tugging his ear with his beak.{TAIL}"),
    5: (["hux_s03_key.png", "pip.png"], f"Keep the burrow scene of image 1 with the sleeping Hux ({HUX}), curled up on his side, eyes closed. Add {PIP} (image 2) hopping on Hux's round belly with wings raised, bouncing playfully.{TAIL}"),
    6: (["hux_s03_key.png", "pip.png"], f"Close-up inside the burrow. Keep the sleeping Hux of image 1 ({HUX}), eyes closed. Add {PIP} (image 2) tiptoeing right next to Hux's ear, one wing cupped beside his beak like telling a secret.{TAIL}"),
    7: (["hux_s03_key.png"], f"Extreme close-up of the face of the sleeping Hux from image 1 ({HUX}), eyes closed, peaceful, the face fills most of the frame, burrow glow blurred in the background.{TAIL}"),
    8: (["hux.png", "pip.png", "env_valley.png"], f"Place {HUX} (image 1) walking out of the round burrow entrance between the pine roots of the valley scene (image 3), fully awake and determined, with his lopsided grin. Next to him {PIP} (image 2) is flying up into the air with joy, wings wide. Keep the scene of image 3.{TAIL}"),
}
for n, (imgs, prompt) in SCENES.items():
    out, dt = run(qwen_edit(prompt, imgs, 40 + n, f"key_s0{n}"))
    f = out["13"]["images"][0]["filename"]
    shutil.copy(r"C:\ComfyUI\output\\" + f, rf"C:\YoutubeVideo\YouTubeCalisma\uretim\b1\kareler\anahtar_s0{n}.png")
    print(n, f, round(dt), flush=True)
