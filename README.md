# Sign Language Recognition
This project harnesses the power of machine learning (ML) and image processing to create an innovative solution for real-time sign language recognition. Using a webcam, the system can recognize and interpret sign language gestures, making communication more accessible for those who rely on sign language.

## 🔗 Developers
- [@Mitchell Cootauco](https://github.com/Mcootauc)
- [@Owen Hunger](https://github.com/ohunger)
- [@Evan Yu](https://github.com/yuevan10284)

## Tech Stack
![Python](https://img.shields.io/badge/-Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

## 🛠️  Setup Instructions
#Prerequisites
- Python 3.8.10
- Webcam for capturing sign language gestures
#Installation
1. Clone the repository to your local machine
   'git clone [repository URL]'
2. Change directory (cd) into the project folder
   'cd [project folder name]'
3. Install the required packages using pip:
   'pip install numpy opencv-python==4.7.0.68 mediapipe==0.9.0.1 scikit-learn==1.2.0'

## Collecting Sign Language Data
Set the 'cap = cv2.VideoCapture(0)' code to whichever camera you want to use. 
Then run the following command into your terminal to collect data and follow the instructions. 

`python collect_imgs.py` 

## Sign Language Detection
Once you've correctly collected all the data, run the following command into the terminal to practice!

`python inference_classifier.py` 
