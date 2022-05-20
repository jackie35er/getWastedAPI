
import numpy as np
import os
import tensorflow as tf

import random
from keras import layers
from keras.models import Sequential
import cv2
import pathlib

from definitions import ROOT_DIR

dataset_dir = os.path.join(ROOT_DIR, "resources/testdata")
sub_directories = ["trash", "valid"]
model_location = os.path.join(ROOT_DIR, 'resources/trashClassificationModel')

img_size = 80

training_ds = []


def create_training_ds():
    for category in sub_directories:
        path = os.path.join(dataset_dir, category)
        class_num = sub_directories.index(category)
        for img in os.listdir(path):
            try:
                img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_COLOR)
                resized_array = cv2.resize(img_array, (img_size, img_size))
                training_ds.append([resized_array, class_num])
            except Exception as e:
                pass


create_training_ds()

random.shuffle(training_ds)

features = []
label_ds = []

for feature, label in training_ds:
    features.append(feature)
    label_ds.append(label)

label_ds = np.array(label_ds)
feature_ds = np.array(features).reshape(-1, img_size, img_size, 3)
feature_ds = feature_ds / 255.0

model = Sequential([
    layers.Conv2D(16, 3, padding='same', input_shape=feature_ds.shape[1:], activation='relu'),
    layers.MaxPooling2D(),
    layers.Conv2D(32, 3, padding='same', activation='relu'),
    layers.MaxPooling2D(),
    layers.Conv2D(64, 3, padding='same', activation='relu'),
    layers.MaxPooling2D(),
    layers.Flatten(),
    layers.Dense(1, activation='sigmoid'),
])

model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

epochs = 10
history = model.fit(
    feature_ds,
    label_ds,
    validation_split=0.2,
    epochs=epochs
)

model.save(model_location)
