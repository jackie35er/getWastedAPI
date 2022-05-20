import tensorflow as tf
import cv2
import numpy as np
from ai.trashClassification.definitions import IMG_SIZE, MODEL_LOCATION
import base64


def convert_base64_to_np(img_base64):
    decoded_data = base64.b64decode(img_base64)
    np_data = np.frombuffer(decoded_data, np.uint8)
    img_array = cv2.imdecode(np_data, cv2.IMREAD_COLOR)
    resized_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
    img_np_array = np.array(resized_array).reshape(-1, IMG_SIZE, IMG_SIZE, 3)
    img_np_array = img_np_array/255.0
    return img_np_array


def predict(img_base64):
    img_np_array = convert_base64_to_np(img_base64)
    model = tf.keras.models.load_model(MODEL_LOCATION)
    predictions = model.predict(img_np_array)
    return predictions[0][0]



