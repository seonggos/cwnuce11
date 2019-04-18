import cv2
import numpy as np
import os
from random import shuffle
from tqdm import tqdm
import tensorflow as tf
from keras.models import Sequential
from keras.layers import *
from keras.optimizers import * 
train_data = "./train_sample"
test_data = "./test"
record = {}
img_size = 32
            
def one_hot_label(img):
    label = img.split("_")[0]
    if label == "positive":
        ohl = np.array([1,0])
    elif label == "negative":
        ohl = np.array([0,1])
    return ohl

def train_data_with_label(img_size):
    train_images = []
    for i in tqdm(os.listdir(train_data)):
        path = os.path.join(train_data, i)
        img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        img = cv2.resize(img, (img_size, img_size))
        train_images.append([np.array(img), one_hot_label(i)])
    shuffle(train_images)
    return train_images

def test_data_with_label(img_size):
    test_images = []
    for i in tqdm(os.listdir(test_data)):
        path = os.path.join(test_data, i)
        img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        img = cv2.resize(img, (img_size, img_size))
        test_images.append([np.array(img), i])
    return test_images

	
while(True):
	training_images = train_data_with_label(img_size)
	testing_images = test_data_with_label(img_size)

	tr_img_data = np.array([i[0] for i in training_images]).reshape(-1, img_size, img_size, 1)
	tr_lbl_data = np.array([i[1] for i in training_images])

	model = Sequential()
	model.add(InputLayer(input_shape = [img_size, img_size, 1]))
	model.add(Conv2D(filters=32, kernel_size=5, strides=1, padding='same', activation='relu'))
	model.add(MaxPool2D(pool_size=5, padding='same'))
	model.add(Conv2D(filters=64, kernel_size=5, strides=1, padding='same', activation='relu'))
	model.add(MaxPool2D(pool_size=5, padding='same'))
	#model.add(Conv2D(filters=80, kernel_size=5, strides=1, padding='same', activation='relu'))
	#model.add(MaxPool2D(pool_size=5, padding='same'))

	model.add(Dropout(0.25))
	model.add(Flatten())
	model.add(Dense(512, activation='relu')) 
	model.add(Dropout(rate=0.5))
	model.add(Dense(2, activation='softmax')) 
	optimizer = Adam(lr=1e-3)
	model.compile(optimizer=optimizer, loss='categorical_crossentropy', metrics=['accuracy'])
	model.fit(x=tr_img_data, y=tr_lbl_data, epochs=50, batch_size=50)
	model.summary()

	result = {
	"P-p" : 0,
	"P-n" : 0,
	"N-p" : 0,
	"N-n" : 0
	}

	for data in testing_images:
		img = data[0]
		title = data[1]
		data = img.reshape(1, img_size, img_size, 1)
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

	record[img_size] = result
	img_size += 16
	print(record)

	if(img_size == 256):
		break
#32: {'P-p': 0, 'P-n': 0, 'N-p': 10, 'N-n': 10}
#48: {'P-p': 0, 'P-n': 0, 'N-p': 10, 'N-n': 10}
#64: {'P-p': 0, 'P-n': 0, 'N-p': 10, 'N-n': 10}
#80: {'P-p': 10, 'P-n': 10, 'N-p': 0, 'N-n': 0}
#96: {'P-p': 10, 'P-n': 10, 'N-p': 0, 'N-n': 0}
