import sys, shutil, json, time
sys.path.insert(0, r"C:\Users\yusuf\AppData\Local\Temp\claude\ddc4959a59b64e86\170759c1-6726-4ee9-a655-d6a9b9f30954\scratchpad")
from hux_lib import *

shutil.copy(r"C:\YoutubeVideo\YouTubeCalisma\uretim\b1\klipler\s03_v2.mp4", r"C:\ComfyUI\input\s03_v2.mp4")
wf = {
    "1": {"class_type": "LoadVideo", "inputs": {"file": "s03_v2.mp4"}},
    "2": {"class_type": "GetVideoComponents", "inputs": {"video": ["1", 0]}},
    "3": {"class_type": "ImageScale", "inputs": {"image": ["2", 0], "upscale_method": "lanczos", "width": 1280, "height": 720, "crop": "center"}},
    "4": {"class_type": "SeedVR2Preprocess", "inputs": {"resized_images": ["3", 0]}},
    "5": {"class_type": "VAELoader", "inputs": {"vae_name": "ema_vae_fp16.safetensors"}},
    "6": {"class_type": "UNETLoader", "inputs": {"unet_name": "seedvr2_7b_fp8_e4m3fn.safetensors", "weight_dtype": "default"}},
    "7": {"class_type": "VAEEncodeTiled", "inputs": {"pixels": ["4", 0], "vae": ["5", 0], "tile_size": 512, "overlap": 64, "temporal_size": 8, "temporal_overlap": 4}},
    "8": {"class_type": "SeedVR2Conditioning", "inputs": {"model": ["6", 0], "vae_conditioning": ["7", 0]}},
    "9": {"class_type": "KSampler", "inputs": {"model": ["6", 0], "seed": 1, "steps": 1, "cfg": 1.0, "sampler_name": "euler", "scheduler": "simple", "positive": ["8", 0], "negative": ["8", 1], "latent_image": ["7", 0], "denoise": 1.0}},
    "10": {"class_type": "VAEDecodeTiled", "inputs": {"samples": ["9", 0], "vae": ["5", 0], "tile_size": 512, "overlap": 64, "temporal_size": 8, "temporal_overlap": 4}},
    "11": {"class_type": "SeedVR2PostProcessing", "inputs": {"images": ["10", 0], "original_resized_images": ["3", 0], "color_correction_method": "lab"}},
    "12": {"class_type": "RIFE VFI", "inputs": {"ckpt_name": "rife49.pth", "frames": ["11", 0], "clear_cache_after_n_frames": 10, "multiplier": 2, "fast_mode": True, "ensemble": True, "scale_factor": 1.0, "dtype": "float32", "torch_compile": False, "batch_size": 1}},
    "13": {"class_type": "CreateVideo", "inputs": {"images": ["12", 0], "fps": 32.0}},
    "14": {"class_type": "SaveVideo", "inputs": {"video": ["13", 0], "filename_prefix": "video/s03_v2_seedvr2_720p_32fps", "format": "mp4", "codec": "h264"}},
}
json.dump(wf, open(r"C:\YoutubeVideo\YouTubeCalisma\comfyui\workflows\hux_upscale_seedvr2_7b_rife32.json", "w"), indent=1)
t0 = time.time()
out, dt = run(wf)
f = out["14"]["images"][0]["filename"]
shutil.copy(rf"C:\ComfyUI\output\video\{f}", r"C:\YoutubeVideo\YouTubeCalisma\uretim\b1\klipler\s03_v2_seedvr2_720p_32fps.mp4")
print("seedvr2+rife ok", round(dt), "sn", out["14"]["images"][0]["metadata"], flush=True)


