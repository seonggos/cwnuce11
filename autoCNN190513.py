import cv2
import numpy as np
import os
from random import shuffle
from tqdm import tqdm
import tensorflow as tf
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import *
from keras.optimizers import *
%matplotlib inline

class_weight = {0:1., 1:3.}
train_data = "./data/train"
test_data = "./data/test"


size = 224

# [레이어 수, filters x레이어수 , kernelsize x레이어수] - 레이어 수만큼 파라미터 입력
tries = 3 # 총 시도할 횟수, 이 수만큼 리스트에 튜플을 넣어줘야함
list_layerNums = [4, 4, 5] #레이어 수
list_filters = [(32, 50, 80, 80),
               (32, 64, 80, 80),
               (32, 50, 64, 80, 80)]
list_kernelsize = [(5, 4, 3, 2),
                  (5, 4, 3, 2),
                  (5, 4, 3, 2, 1)]

list_records = [] #기록이 담길 리스트

            
def one_hot_label(img):
    label = img.split("_")[0]
    if label == "positive":
        ohl = np.array([1,0])
    elif label == "negative":
        ohl = np.array([0,1])
    return ohl

def train_data_with_label(size):
    train_images = []
    for i in tqdm(os.listdir(train_data)):
        path = os.path.join(train_data, i)
        img = cv2.imread(path, cv2.IMREAD_COLOR)
        img = cv2.resize(img, (size, size))
        train_images.append([np.array(img), one_hot_label(i)])
    shuffle(train_images)
    return train_images

def test_data_with_label(size):
    test_images = []
    for i in tqdm(os.listdir(test_data)):
        path = os.path.join(test_data, i)
        img = cv2.imread(path, cv2.IMREAD_COLOR)
        img = cv2.resize(img, (size, size))
        test_images.append([np.array(img), i])
    return test_images




for i in range(0, tries):
    layerNum = list_layerNums[i]
    
    training_images = train_data_with_label(size)
    testing_images = test_data_with_label(size)

    tr_img_data = np.array([i[0] for i in training_images])
    tr_lbl_data = np.array([i[1] for i in training_images])


    model = Sequential()
    model.add(InputLayer(input_shape = [size, size, 3]))
    
    for j in range(0, layerNum):
        model.add(Conv2D(filters=list_filters[i][j], kernel_size=list_kernelsize[i][j], strides=1, padding='same', activation='relu'))
        model.add(MaxPool2D(pool_size=2, padding='same'))
        
# model.add(Dropout(0.25)) # 살리는지 버리는지 확인
    model.add(Flatten())
    model.add(Dense(512, activation='relu')) 
    model.add(Dropout(0.5))
    model.add(Dense(2, activation='softmax')) 
    optimizer = Adam(lr=1e-3)
    model.compile(optimizer=optimizer, loss='binary_crossentropy', metrics=['accuracy'])
    model.fit(x=tr_img_data, y=tr_lbl_data, epochs=50, batch_size=32, class_weight=class_weight)
    model.summary()

    fig = plt.figure(figsize=(14, 14))
    result = {
        "P-p" : 0,
        "P-n" : 0,
        "N-p" : 0,
        "N-n" : 0
    }


    for cnt, data in enumerate(testing_images):
        y = fig.add_subplot(20, 5, cnt+1)
        img = data[0]
        title = data[1]
        data = img.reshape(1, size, size, 3)
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

        
    accuracy = (result["P-p"]+result["N-n"])/(result["P-p"]+result["P-n"]+result["N-p"]+result["N-n"])
    # Accuracy = Pp+Np/Pp+Pn+Np+Nn 정확도(n을 N이라고, p를 P라고 예상한 총확률. 0.8 이상이 좋다.

    if(result["N-n"]+result["N-p"])==0:
        precision = 0 #0으로 나눌 경우 처리
    else:
        precision = result["N-n"]/(result["N-n"]+result["N-p"])
    # Precision = Nn/Nn+Pp Negative라고 예상한 데이터 중에서 실제로 Negative였던 게 어느 정도인지. 0.7 이상이 좋다.

    if(result["N-n"]+result["P-n"])==0:
        recall = 0 #0으로 나눌 경우 처리
    else:
        recall = result["N-n"]/(result["N-n"]+result["P-n"])
    # Recall(Sensitivity) = Nn/Nn+Pn 실제로 Negative인 데이터를 얼마나 찾아냈는지. 0.5 이상이 좋다.

    if(recall+precision)==0:
        f1 = 0
    else:
        f1 = 2*(recall*precision)/(recall+precision)
    # F1 Score = 2*(Recall*Precision)/(Recall*Precision) , recall과 precision의 가중평균,
    # N, P 비율이 다르면 F1이 acc보다 참고할만 하다.

    list_records.append("size: "+ str(size) + ", filter: " + str(list_filters[i]) + ", kernel size: " + str(list_kernelsize[i]) 
                        + " accuracy: " + str("%0.4f" % accuracy) + ", precision: " + str("%0.4f" % precision) + ", recall: " + str("%0.4f" % recall) + ", f1: " + str("%0.4f" % f1))
    print(result)
    print(list_records)
