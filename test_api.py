from inference_sdk import InferenceHTTPClient
from PIL import Image
import os

CLIENT = InferenceHTTPClient(
    api_url="https://detect.roboflow.com",
    api_key="API_KEY"
)

filenames = os.listdir("shoes_color.v4i.yolov8/train/images")

for index, filename in enumerate(filenames):
    if (index == 2):
        break
    image = Image.open(f"shoes_color.v4i.yolov8/train/images/{filename}")
    result = CLIENT.infer(image, model_id="thai-ocr/2")
    print(result)