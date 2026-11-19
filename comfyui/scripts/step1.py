import sys, shutil
sys.path.insert(0, r"C:\Users\yusuf\AppData\Local\Temp\claude\ddc4959a59b64e86\170759c1-6726-4ee9-a655-d6a9b9f30954\scratchpad")
from hux_lib import *

PIP = ("Pip, a tiny cute caricatured honeyguide bird: round brown body, pale chest, oversized head, huge shiny eyes, "
       "short pink beak, one feather sticking up on his head like a cowlick.")
jobs = []
for s in (11, 22, 33):
    jobs.append((f"pip_seed{s}", qwen_t2i(f"Character reference, single full-body front three-quarter view, centered, plain light grey background. {PIP} Friendly restless energetic posture. {STYLE}", s, f"pip_seed{s}")))
VALLEY = ("Wide establishing shot of a quiet valley at dawn where a pine forest meets a wildflower meadow, mist over a small pond, "
          "a big pine tree with a small round burrow entrance glowing softly between its roots. Golden morning light. " + STYLE)
BURROW = ("Inside a cosy underground burrow under the roots of a pine tree, roots hanging from the earthen ceiling, a bed of dry grass and leaves, "
          "warm golden light falling through the round entrance. No characters. " + STYLE)
jobs.append(("valley", qwen_t2i(VALLEY, 5, "env_valley")))
jobs.append(("burrow", qwen_t2i(BURROW, 5, "env_burrow")))
for name, wf in jobs:
    out, dt = run(wf)
    f = out["13"]["images"][0]["filename"]
    print(name, f, round(dt), "sn", flush=True)
