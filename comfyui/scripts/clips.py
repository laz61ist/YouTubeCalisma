import sys, shutil, shutil, os
sys.path.insert(0, r"C:\Users\yusuf\AppData\Local\Temp\claude\ddc4959a59b64e86\170759c1-6726-4ee9-a655-d6a9b9f30954\scratchpad")
from hux_lib import *

S = "Stylized 3D animated feature-film look, warm golden light, smooth cinematic camera, cute friendly mood. No music, no subtitles, no on-screen text."
CLIPS = {
    1: ("anahtar_s01.png", f"Slow aerial push-in toward the roots of the big pine tree and the glowing round burrow entrance. Mist drifts slowly over the pond, wildflowers and grass sway in the breeze, tiny birds cross the dawn sky, the entrance glows softly. {S}"),
    2: ("anahtar_s02.png", f"Pip the little brown bird lands with a bounce on the grass in front of the burrow entrance, folds his wings, then hops up and down excitedly several times and leans forward to peek inside the burrow, his head bobbing, wings flapping with excitement. {S}"),
    3: ("hux_s03_key.png", f"Hux the honey badger sleeps peacefully curled up on dry grass, eyes closed. Clearly visible slow breathing: his body rises and falls, his small ear twitches, a soft snore puffs from his nose, dust motes drift in the warm light. Very slow gentle camera push-in. {S}"),
    4: ("anahtar_s04.png", f"Pip the little bird, standing on top of sleeping Hux's head, gently tugs Hux's ear with his beak, then flaps his wings and talks excitedly with his beak moving. Hux stays asleep with eyes closed, his ear stretches and flicks, he grumbles sleepily and scrunches his face. {S}"),
    5: ("anahtar_s05.png", f"Pip the little bird hops up and down on sleeping Hux's round belly like a trampoline, wings flapping for balance. Hux sleepily rolls over onto his other side, and Pip slides softly off into the soft grass bed and pops back up with his feathers comically ruffled, shaking himself off. Gentle and harmless. {S}"),
    6: ("anahtar_s06.png", f"Close-up. Pip the little bird tiptoes slowly right up to sleeping Hux's ear, cups one wing beside his beak like telling a secret, and whispers, his beak moving slowly. Hux stays asleep, his ear gives a tiny twitch. Slow gentle push-in. {S}"),
    7: ("anahtar_s07.png", f"Extreme close-up of sleeping Hux's face. Total stillness for the first few seconds, only faint breathing. Then suddenly one eye pops wide open, perfectly alert and bright, while the rest of the face stays still. Slow push-in on the open eye. {S}"),
    8: ("anahtar_s08.png", f"Hux the honey badger marches out of the burrow fully awake and determined, with confident steps, past the camera side. Pip bursts into the air with joy, flaps his wings and flies off across the meadow, and Hux trots after him. {S}"),
}
only = [int(a) for a in sys.argv[1:]] or list(CLIPS)
for n in only:
    img, prompt = CLIPS[n]
    if img.startswith("anahtar"):
        shutil.copy(rf"C:\YoutubeVideo\YouTubeCalisma\uretim\b1\kareler\{img}", rf"C:\ComfyUI\input\{img}")
    out, dt = run(wan_i2v(prompt, img, 20261119 + n, f"taslak_s0{n}", length=129))
    f = out["17"]["images"][0]["filename"]
    shutil.copy(rf"C:\ComfyUI\output\video\{f}", rf"C:\YoutubeVideo\YouTubeCalisma\uretim\b1\klipler\taslak_s0{n}.mp4")
    print(f"s0{n} ok {round(dt)} sn", flush=True)
