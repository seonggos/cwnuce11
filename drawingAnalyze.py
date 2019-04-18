#!/usr/bin/python3
import cv2
import sys
import numpy as np
import os
import tensorflow as tf
from random import shuffle
from keras.models import Sequential
from keras.layers import *
from keras.optimizers import * 

test_data = "./uploads"

def test_data_with_label():
	test_images = []
	
	for i in os.listdir(test_data):
		path = os.path.join(test_data, i)
		img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
		img = cv2.resize(img, (32, 32))
		test_images.append([np.array(img), i])
	return test_images

testing_images = test_data_with_label() 
model = Sequential()
model.add(InputLayer(input_shape = [32, 32, 1]))
model.add(Conv2D(filters=32, kernel_size=5, strides=1, padding='same', activation='relu'))
model.add(MaxPool2D(pool_size=5, padding='same'))
model.add(Conv2D(filters=50, kernel_size=5, strides=1, padding='same', activation='relu'))
model.add(MaxPool2D(pool_size=5, padding='same'))
model.add(Conv2D(filters=80, kernel_size=5, strides=1, padding='same', activation='relu')) 
model.add(MaxPool2D(pool_size=5, padding='same'))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(512, activation='relu')) 
model.add(Dropout(rate=0.5))
model.add(Dense(2, activation='softmax')) 
optimizer = Adam(lr=1e-3)
model.load_weights("model.h5")
model.compile(optimizer=optimizer, loss='categorical_crossentropy', metrics=['accuracy'])

result = {
    "P-p" : 0,
    "P-n" : 0,
    "N-p" : 0,
    "N-n" : 0
}

for data in testing_images:
    img = data[0]
    title = data[1]
    data = img.reshape(1, 32, 32, 1)
    model_out = model.predict([data])
    
    if np.argmax(model_out) == 1:
        str_label = "Negative"
    else:
        str_label = "Positive"
    
    if str_label == "Positive" and title.split("_")[0] == "positive":
        result["P-p"] += 1;
    elif str_label == "Positive" and title.split("_")[0] == "negative":
        result["P-n"] += 1;
    elif str_label == "Negative" and title.split("_")[0] == "positive":
        result["N-p"] += 1;
    elif str_label == "Negative" and title.split("_")[0] == "negative":
        result["N-n"] += 1;

result_message = "There are " + str(result["N-p"] + result["N-n"]) + " negative pictures of " + str(len(testing_images))

print(result_message)
