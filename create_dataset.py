import mediapipe as mp 
import cv2 
import os

# for mitch and evan at this point we have 3 folders(which we can change later in script)
# that have 100 photos of one specific hand symbol
import matplotlib.pyplot as plt

DATA_DIR = './data'


#show first image of each, load as img plot. just to check that it works plt.imshow
for dir_ in os.listdir(DATA_DIR):
    for img_path in os.listdir(os.path.join(DATA_DIR, dir_))[:1]:
        img = cv2.imread(os.path.join(DATA_DIR, dir_, img_path))
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        plt.figure()
        plt.imshow(img_rgb)

plt.show()