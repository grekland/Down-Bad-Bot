from PIL import Image
from requests import post
from io import BytesIO
from base64 import b64decode
from payload import payload

URL = "http://127.0.0.1:7860/sdapi/v1/txt2img"

async def txt2img():
    response = post(URL, json=payload)

    r = response.json()

    for count, image_data in enumerate(r['images']):
        image = Image.open(BytesIO(b64decode(image_data.split(",",1)[0])))
        image.save(fr"../outputs/output_{count}.jpg")