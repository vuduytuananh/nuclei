import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib
matplotlib.rcParams['backend'] = 'GTK'
train_images_dir = os.getcwd() + "/input/train_images/"
image_dir_name = "images"
mask_dir_name = "masks"
count = 0
def show_time(pic_data):
    plt.imshow(pic_data)
    plt.show()

def process_images(image_path):
    print("Processing image...")

def process_mask(mask_path):
    print("Processing mask...")
def _4x_4x_image(data):
    for i in range(data.shape[1]):
        for _ in range(3):
            data = np.insert(data, i * 4, data[:, i*4], axis = 1)
    for i in range(data.shape[0]):
        for _ in range(3):
            data = np.insert(data, i*4, data[i*4,:], axis = 0)
    return data
for sub_dir in os.listdir(train_images_dir):
    pic_data = np.array([])
    for sd in os.listdir(train_images_dir + sub_dir):
        dir_path = train_images_dir + sub_dir + "/" + sd + "/"
        file_path = dir_path + os.listdir(dir_path)[0]
        # image
        if sd == image_dir_name:
            pic_data = mpimg.imread(file_path)[:,:,1]
            print(pic_data.shape)
            # print(pic_data[0])
        # mask
        else:
            mask_data = mpimg.imread(file_path)
            pic_data += mask_data
            pic_data = np.hstack((pic_data, np.ones((pic_data.shape[0], 50)), pic_data - mask_data))
            # print(mask_data.shape)
            show_time(pic_data)
