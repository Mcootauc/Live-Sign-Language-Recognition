import os
import pickle
import cv2
import mediapipe as mp

# use mediapipe 
mp_hands = mp.solutions.hands
hands_processor = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3)

DATA_DIR = './data'

processed_data = []
class_labels = []
#iterating over the class
for class_dir in os.listdir(DATA_DIR):
    class_path = os.path.join(DATA_DIR, class_dir)
    for image_file in os.listdir(class_path):
        landmark_data = []
        landmark_x = []
        landmark_y = []

        # Loading the ddata
        image = cv2.imread(os.path.join(class_path, image_file))
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        detection_results = hands_processor.process(image_rgb)

        # getting handmarks 
        if detection_results.multi_hand_landmarks:
            for landmarks in detection_results.multi_hand_landmarks:
                for landmark in landmarks.landmark:
                    landmark_x.append(landmark.x)
                    landmark_y.append(landmark.y)

                min_x, min_y = min(landmark_x), min(landmark_y)
                for landmark in landmarks.landmark:
                    normalized_x = landmark.x - min_x
                    normalized_y = landmark.y - min_y
                    landmark_data.extend([normalized_x, normalized_y])

            processed_data.append(landmark_data)
            class_labels.append(class_dir)

# saving data and labels
with open('data.pickle', 'wb') as data_file:
    pickle.dump({'data': processed_data, 'labels': class_labels}, data_file)
