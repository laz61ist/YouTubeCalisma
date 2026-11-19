import sys, shutil
sys.path.insert(0, r"C:\Users\yusuf\AppData\Local\Temp\claude\ddc4959a59b64e86\170759c1-6726-4ee9-a655-d6a9b9f30954\scratchpad")
from hux_lib import *
K = r"C:\YoutubeVideo\YouTubeCalisma\uretim\b1\kareler\\"
for a, b in (("anahtar3_s04_62", "k_s04"), ("anahtar3_s05_61", "k_s05"), ("anahtar2_s06", "k_s06"), ("anahtar_s01", "k_s01"), ("anahtar_s02", "k_s02")):
    shutil.copy(K + a + ".png", rf"C:\ComfyUI\input\{b}.png")
S = "Stylized 3D animated feature-film look, warm golden light, smooth cinematic camera, cute friendly mood. No music, no subtitles, no on-screen text."
HUXN = "Hux the honey badger (black face, silver-white cap, long narrow snout, small flat ears)"
C = {
 1: ("k_s01.png", None, f"Slow aerial push-in toward the roots of the big pine tree and the round burrow entrance, which glows softly and stays empty. Mist drifts slowly over the pond, wildflowers and grass sway in the breeze, tiny birds cross the dawn sky. {S}", 20261201),
 2: ("k_s02.png", None, f"Pip the little brown bird lands softly on the grass in front of the burrow entrance, folds his wings neatly, hops twice excitedly, then leans forward and peeks into the burrow, head tilting. Calm, smooth, simple movement, Pip always upright. {S}", 20261202),
 3: ("hux_uyku.png", None, f"{HUXN} sleeps peacefully curled up on dry grass, eyes closed. Clearly visible slow breathing: his body rises and falls, his small ear twitches, a soft snore puffs from his nose, dust motes drift in the warm light. Very slow gentle camera push-in. {S}", 20261203),
 4: ("k_s04.png", None, f"Pip the little bird, standing on top of sleeping Hux's head, gently tugs Hux's ear with his beak, then flaps his wings and chirps excitedly. Hux stays asleep with eyes closed, his ear stretches and flicks, he grumbles sleepily and scrunches his face. Only one bird. {S}", 20261204),
 5: ("k_s05.png", None, f"Pip the little bird hops up and down on sleeping Hux's furry back like a trampoline, wings flapping for balance. Hux sleepily rolls slightly onto his side, and Pip slides softly off into the grass bed and pops back up with feathers comically ruffled, shaking himself off. Gentle and harmless. Only one bird. {S}", 20261205),
 6: ("k_s06.png", None, f"Pip the little bird tiptoes slowly right up to sleeping Hux's ear, cups one wing beside his beak like telling a secret, and whispers, his beak moving slowly. Hux stays asleep, his ear gives a tiny twitch. Slow gentle push-in. Only one bird. {S}", 20261206),
 7: ("anahtar2_s07a.png", "anahtar2_s07b.png", f"Extreme close-up of sleeping Hux's face. Total stillness for the first three seconds, only faint breathing, eyes closed. Then suddenly one eye pops wide open, bright and perfectly alert, and stays open, while the other eye stays closed. Slow push-in on the open eye. {S}", 20261207),
}
for n, (a, b, p, seed) in C.items():
    wf = wan_flf(p, a, b, seed, f"taslak2_s0{n}") if b else wan_i2v(p, a, seed, f"taslak2_s0{n}", length=129)
    out, dt = run(wf)
    f = out["17"]["images"][0]["filename"]
    shutil.copy(rf"C:\ComfyUI\output\video\{f}", rf"C:\YoutubeVideo\YouTubeCalisma\uretim\b1\klipler\taslak2_s0{n}.mp4")
    print(f"s0{n} ok {round(dt)} sn", flush=True)
