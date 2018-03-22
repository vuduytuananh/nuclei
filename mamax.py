import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

train_images_dir = os.getcwd() + "/input/train_images/"
image_dir_name = "images"
mask_dir_name = "masks"
count = 0
def show_time(file_path):
    pic = mpimg.imread(file_path)
    print(file_path)
    plt.imshow(pic)
    plt.show()
def process_images(image_path):
    print("Processing image...")
    show_time(image_path)
def process_mask(mask_path):
    print("Processing mask...")
    show_time(mask_path)

for sub_dir in os.listdir(train_images_dir):
    for sd in os.listdir(train_images_dir + sub_dir):
        dir_path = train_images_dir + sub_dir + "/" + sd + "/"
        file_path = dir_path + os.listdir(dir_path)[0]
        # image
        if sd == image_dir_name: process_images(file_path)
        # mask
        else: process_mask(file_path)
