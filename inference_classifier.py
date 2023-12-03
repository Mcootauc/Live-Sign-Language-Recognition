import pickle
import cv2
import mediapipe as mp
import numpy as np


model_dict = pickle.load(open('model.pkl', 'rb'))
model = model_dict['model']
label_encoder = model_dict.get('label_encoder', None)  

cap = cv2.VideoCapture(0)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3)

while True:
    ret, frame = cap.read()
    if not ret:
        break  

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
          
            data_aux = [landmark.x - min(landmark.x for landmark in hand_landmarks.landmark) for landmark in hand_landmarks.landmark] + \
                       [landmark.y - min(landmark.y for landmark in hand_landmarks.landmark) for landmark in hand_landmarks.landmark]

           
            prediction = model.predict([np.asarray(data_aux)])
            predicted_character = label_encoder.inverse_transform(prediction)[0] if label_encoder else str(prediction[0])

          
            cv2.putText(frame, predicted_character, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):  
        break

cap.release()
cv2.destroyAllWindows()
