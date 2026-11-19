import json, time, urllib.request

API = "http://127.0.0.1:8188"


def post(wf):
    body = json.dumps({"prompt": wf, "client_id": "claude-hux"}).encode()
    req = urllib.request.Request(API + "/prompt", body, {"Content-Type": "application/json"})
    return json.load(urllib.request.urlopen(req))["prompt_id"]


def get(path):
    return json.load(urllib.request.urlopen(API + path))


def wait(pid, timeout=3600):
    t0 = time.time()
    while time.time() - t0 < timeout:
        h = get("/history/" + pid)
        if pid in h:
            return h[pid], time.time() - t0
        time.sleep(3)
    raise TimeoutError(pid)


def run(wf):
    pid = post(wf)
    h, dt = wait(pid)
    if h["status"]["status_str"] != "success":
        raise RuntimeError(json.dumps(h["status"]["messages"])[:1500])
    return h["outputs"], dt


STYLE = ("Stylized 3D animated feature-film look: cute caricatured animals with oversized heads, big friendly "
         "expressive eyes, short stubby limbs, no sharp teeth; realistic soft fur and feather texture, warm light, "
         "cheerful friendly mood, shallow depth of field, cinematic 16:9. No text, no subtitles.")


def qwen_t2i(prompt, seed, prefix, w=1344, h=768):
    return {
        "1": {"class_type": "UNETLoader", "inputs": {"unet_name": "qwen_image_2512_fp8_e4m3fn.safetensors", "weight_dtype": "default"}},
        "2": {"class_type": "LoraLoaderModelOnly", "inputs": {"model": ["1", 0], "lora_name": "Qwen-Image-Lightning-8steps-V2.0-bf16.safetensors", "strength_model": 1.0}},
        "3": {"class_type": "ModelSamplingAuraFlow", "inputs": {"model": ["2", 0], "shift": 3.0}},
        "5": {"class_type": "CLIPLoader", "inputs": {"clip_name": "qwen_2.5_vl_7b_fp8_scaled.safetensors", "type": "qwen_image", "device": "default"}},
        "6": {"class_type": "VAELoader", "inputs": {"vae_name": "qwen_image_vae.safetensors"}},
        "8": {"class_type": "CLIPTextEncode", "inputs": {"clip": ["5", 0], "text": prompt}},
        "9": {"class_type": "CLIPTextEncode", "inputs": {"clip": ["5", 0], "text": ""}},
        "10": {"class_type": "EmptySD3LatentImage", "inputs": {"width": w, "height": h, "batch_size": 1}},
        "11": {"class_type": "KSampler", "inputs": {"model": ["3", 0], "seed": seed, "steps": 8, "cfg": 1.0, "sampler_name": "euler", "scheduler": "simple", "positive": ["8", 0], "negative": ["9", 0], "latent_image": ["10", 0], "denoise": 1.0}},
        "12": {"class_type": "VAEDecode", "inputs": {"samples": ["11", 0], "vae": ["6", 0]}},
        "13": {"class_type": "SaveImage", "inputs": {"images": ["12", 0], "filename_prefix": prefix}},
    }


def qwen_edit(prompt, images, seed, prefix):
    """images: list of up to 3 filenames in ComfyUI input dir"""
    wf = {
        "1": {"class_type": "UNETLoader", "inputs": {"unet_name": "qwen_image_edit_2511_fp8mixed.safetensors", "weight_dtype": "default"}},
        "2": {"class_type": "LoraLoaderModelOnly", "inputs": {"model": ["1", 0], "lora_name": "Qwen-Image-Edit-2511-Lightning-8steps-V1.0-bf16.safetensors", "strength_model": 1.0}},
        "3": {"class_type": "ModelSamplingAuraFlow", "inputs": {"model": ["2", 0], "shift": 3.0}},
        "4": {"class_type": "CFGNorm", "inputs": {"model": ["3", 0], "strength": 1.0}},
        "5": {"class_type": "CLIPLoader", "inputs": {"clip_name": "qwen_2.5_vl_7b_fp8_scaled.safetensors", "type": "qwen_image", "device": "default"}},
        "6": {"class_type": "VAELoader", "inputs": {"vae_name": "qwen_image_vae.safetensors"}},
        "10": {"class_type": "EmptySD3LatentImage", "inputs": {"width": 1344, "height": 768, "batch_size": 1}},
        "11": {"class_type": "KSampler", "inputs": {"model": ["4", 0], "seed": seed, "steps": 8, "cfg": 1.0, "sampler_name": "euler", "scheduler": "simple", "positive": ["8", 0], "negative": ["9", 0], "latent_image": ["10", 0], "denoise": 1.0}},
        "12": {"class_type": "VAEDecode", "inputs": {"samples": ["11", 0], "vae": ["6", 0]}},
        "13": {"class_type": "SaveImage", "inputs": {"images": ["12", 0], "filename_prefix": prefix}},
    }
    pos = {"clip": ["5", 0], "vae": ["6", 0], "prompt": prompt}
    neg = {"clip": ["5", 0], "vae": ["6", 0], "prompt": ""}
    for i, name in enumerate(images, 1):
        wf[f"2{i}"] = {"class_type": "LoadImage", "inputs": {"image": name}}
        pos[f"image{i}"] = [f"2{i}", 0]
        neg[f"image{i}"] = [f"2{i}", 0]
    wf["8"] = {"class_type": "TextEncodeQwenImageEditPlus", "inputs": pos}
    wf["9"] = {"class_type": "TextEncodeQwenImageEditPlus", "inputs": neg}
    return wf


def wan_i2v(prompt, image, seed, prefix, w=832, h=480, length=129, fps=16.0, rife=False):
    wf = {
        "1": {"class_type": "UNETLoader", "inputs": {"unet_name": "wan2.2_i2v_high_noise_14B_fp8_scaled.safetensors", "weight_dtype": "default"}},
        "2": {"class_type": "UNETLoader", "inputs": {"unet_name": "wan2.2_i2v_low_noise_14B_fp8_scaled.safetensors", "weight_dtype": "default"}},
        "3": {"class_type": "LoraLoaderModelOnly", "inputs": {"model": ["1", 0], "lora_name": "wan2.2_i2v_lightx2v_4steps_lora_v1_high_noise.safetensors", "strength_model": 1.0}},
        "4": {"class_type": "LoraLoaderModelOnly", "inputs": {"model": ["2", 0], "lora_name": "wan2.2_i2v_lightx2v_4steps_lora_v1_low_noise.safetensors", "strength_model": 1.0}},
        "5": {"class_type": "ModelSamplingSD3", "inputs": {"model": ["3", 0], "shift": 5.0}},
        "6": {"class_type": "ModelSamplingSD3", "inputs": {"model": ["4", 0], "shift": 5.0}},
        "7": {"class_type": "CLIPLoader", "inputs": {"clip_name": "umt5_xxl_fp8_e4m3fn_scaled.safetensors", "type": "wan", "device": "default"}},
        "8": {"class_type": "VAELoader", "inputs": {"vae_name": "wan_2.1_vae.safetensors"}},
        "9": {"class_type": "LoadImage", "inputs": {"image": image}},
        "10": {"class_type": "CLIPTextEncode", "inputs": {"clip": ["7", 0], "text": prompt}},
        "11": {"class_type": "CLIPTextEncode", "inputs": {"clip": ["7", 0], "text": "text, subtitles, watermark, logo, sharp teeth, fangs, aggressive, scary, extra limbs, extra legs, deformed, melting face, flickering, blurry, low quality, static, overexposed, worst quality, jpeg artifacts, 色调艳丽，过曝，静态，细节模糊不清，字幕，画得不好的手部，画得不好的脸部，畸形的，毁容的，形态畸形的肢体，三条腿"}},
        "12": {"class_type": "WanImageToVideo", "inputs": {"positive": ["10", 0], "negative": ["11", 0], "vae": ["8", 0], "width": w, "height": h, "length": length, "batch_size": 1, "start_image": ["9", 0]}},
        "13": {"class_type": "KSamplerAdvanced", "inputs": {"model": ["5", 0], "add_noise": "enable", "noise_seed": seed, "steps": 4, "cfg": 1.0, "sampler_name": "euler", "scheduler": "simple", "positive": ["12", 0], "negative": ["12", 1], "latent_image": ["12", 2], "start_at_step": 0, "end_at_step": 2, "return_with_leftover_noise": "enable"}},
        "14": {"class_type": "KSamplerAdvanced", "inputs": {"model": ["6", 0], "add_noise": "disable", "noise_seed": 0, "steps": 4, "cfg": 1.0, "sampler_name": "euler", "scheduler": "simple", "positive": ["12", 0], "negative": ["12", 1], "latent_image": ["13", 0], "start_at_step": 2, "end_at_step": 10000, "return_with_leftover_noise": "disable"}},
        "15": {"class_type": "VAEDecode", "inputs": {"samples": ["14", 0], "vae": ["8", 0]}},
        "16": {"class_type": "CreateVideo", "inputs": {"images": ["15", 0], "fps": fps}},
        "17": {"class_type": "SaveVideo", "inputs": {"video": ["16", 0], "filename_prefix": "video/" + prefix, "format": "mp4", "codec": "h264"}},
    }
    return wf
