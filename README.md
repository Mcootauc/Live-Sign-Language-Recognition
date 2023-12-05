# Sign Language Recognition
This project seeks to leverage advancements in deep learning and image processing to create
an innovative solution for real-time sign language recognition. By addressing challenges such
as varying hand orientations and background noise, we aim to develop a system that enhances
communication accessibility for individuals with hearing impairments.

## 🔗 Developers
- [@Mitchell Cootauco](https://github.com/Mcootauc)
- [@Owen Hunger](https://github.com/ohunger)
- [@Evan Yu](https://github.com/yuevan10284)

## Tech Stack
![Python](https://img.shields.io/badge/-Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

# How to setup
Make sure you have Python 3.8.10 installed so you can install the following packages.
CD into the project folder, and run the following command in the terminal.

`pip install numpy`
`pip install opencv-python`
`pip install mediapipe`

## Collecting Sign Language Data
Set the 'cap = cv2.VideoCapture(0)' code to whichever camera you want to use. 
Then run the following command into your terminal to collect data and follow the instructions. 

`python collect_imgs.py` 

## Sign Language Detection
Once you've correctly collected all the data, run the following command into the terminal to practice!

`python inference_classifier.py` 
