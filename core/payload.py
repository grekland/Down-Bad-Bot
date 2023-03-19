from csv import DictReader
from requests import get
from json import loads
from os import chdir

chdir("core")

with open("../resources/style_default.csv") as f:
    reader = DictReader(f)
    row = next(reader)
    prompt = row["prompt"]
    negative_prompt = row["negative_prompt"]
 
response = get("http://127.0.0.1:7860/sdapi/v1/sd-models")

models = loads(response.content) 

model_index = 2

payload = {
    "prompt": prompt, 
    "negative_prompt": negative_prompt,
    "batch_size": 2,
    "steps": 30,
    "width": 512,
    "height": 768,
    "sampler_index": "DPM++ 2S a Karras",
    "enable_hr": True,
    "denoising_strength": 0.5,
    "hr_scale": 1.5,
    "hr_upscaler": "ESRGAN_4x",
    'override_settings': {'sd_model_checkpoint': 'Deliberate.safetensors [9aba26abdf]'}
}