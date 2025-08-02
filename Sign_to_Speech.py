import cv2
import mediapipe as mp
import numpy as np
import pyttsx3
from collections import deque

# Initialize webcam
cap = cv2.VideoCapture(0)
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7)
mp_draw = mp.solutions.drawing_utils
engine = pyttsx3.init()

COOLDOWN_FRAMES = 20
cooldown_counter = 0

def gesture_to_text(landmarks):
    if landmarks is None:
        return None
    # Landmarks for tips of thumb, index, middle, ring, pinky fingers
    tips = [landmarks[i] for i in [4, 8, 12, 16, 20]]
    thumb_tip, index_tip, middle_tip, ring_tip, pinky_tip = tips

    # Calculate some distances between finger tips (heuristic)
    dist_thumb_index = np.sqrt((thumb_tip.x - index_tip.x)**2 + (thumb_tip.y - index_tip.y)**2)
    dist_thumb_middle = np.sqrt((thumb_tip.x - middle_tip.x)**2 + (thumb_tip.y - middle_tip.y)**2)
    dist_index_middle = np.sqrt((index_tip.x - middle_tip.x)**2 + (index_tip.y - middle_tip.y)**2)

    # Example gesture rules (customize as you collect more data!):
    if dist_thumb_index < 0.05 and dist_thumb_middle > 0.1:
        return "Hello"
    elif dist_thumb_index < 0.05 and dist_thumb_middle < 0.05:
        return "How are you"
    elif dist_index_middle < 0.04 and dist_thumb_index > 0.10:
        return "Nice to meet you"
    else:
        return None

recent_text = ""

while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)
    hand_landmarks = None
    if result.multi_hand_landmarks:
        for hand_lm in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_lm, mp_hands.HAND_CONNECTIONS)
            hand_landmarks = hand_lm.landmark

    text = gesture_to_text(hand_landmarks)

    if cooldown_counter > 0:
        cooldown_counter -= 1

    if text and (text != recent_text) and cooldown_counter == 0:
        engine.say(text)
        engine.runAndWait()
        print(f"Recognized and speaking: {text}")
        recent_text = text
        cooldown_counter = COOLDOWN_FRAMES

    # Reset recent_text when no gesture is detected
    if text is None and cooldown_counter == 0:
        recent_text = ""

    # Overlay the recognized gesture on the frame
    if text:
        cv2.putText(frame, text, (10, 50), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0, 255, 0), 2, cv2.LINE_AA)

    cv2.imshow('Hand Gesture Recognition', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
