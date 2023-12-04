import cv2
import numpy as np
import requests
from io import BytesIO


def process_defaults(src):
    result = {}
    image_A = get_image(src)
    for defaut in ('impact', 'griffure', 'rayure', 'marque'):
        image_B = cv2.imread("materials/images/" + defaut + '.png')
        n_defauts = count_default(image_A, image_B)
        result[defaut] = n_defauts
    return result


def get_image(src):
    response = requests.get(src)
    if response.status_code == 200:
        # Read the image data and convert it into a NumPy array
        image_data = BytesIO(response.content)
        image_data = np.asarray(bytearray(image_data.read()), dtype="uint8")

        # Decode the image data
        image = cv2.imdecode(image_data, cv2.IMREAD_COLOR)
        return image
    else:
        print("Failed to fetch the image")


def count_default(image_A, image_B):
    result = cv2.matchTemplate(image_A, image_B, cv2.TM_CCOEFF_NORMED)
    threshold = 0.95
    locations = np.where(result >= threshold)

    unique_locations = set(zip(*locations[::-1]))
    count_B = len(unique_locations)

    return count_B