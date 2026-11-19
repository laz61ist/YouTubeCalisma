import sys
sys.path.insert(0, r"C:\Users\yusuf\AppData\Local\Temp\claude\ddc4959a59b64e86\170759c1-6726-4ee9-a655-d6a9b9f30954\scratchpad")
from hux_lib import *
ENV = "Stylized 3D animated feature-film environment concept, warm light, cheerful mood, cinematic 16:9. Completely empty scenery, uninhabited: absolutely no animals, no creatures, no characters, no people. No text. "
V = ENV + "Wide establishing shot of a quiet valley at dawn where a pine forest meets a wildflower meadow, mist over a small pond, a big pine tree whose roots hold a small round burrow entrance glowing softly. Golden morning light."
B = ENV + "Interior of a cosy underground burrow under pine roots: earthen walls, roots hanging from the ceiling, an empty bed of dry grass and leaves in the middle of the floor, a small pile of honeycomb in the corner, warm golden light falling through the round entrance."
for name, p, seeds in (("valley", V, (6, 7)), ("burrow", B, (6, 7))):
    for s in seeds:
        out, dt = run(qwen_t2i(p, s, f"env2_{name}_{s}"))
        print(out["13"]["images"][0]["filename"], round(dt), flush=True)
