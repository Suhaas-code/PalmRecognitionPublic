# An original by Suhaas-code (github) .
# please install OpenCv-Python , Time and Mediapipe.
# update pip if getting install errors, I got them as well.

print("Author : Suhaas")
print("REG - 2193xxxxx")
print("preserving privacy")

import cv2
import mediapipe as mp
import time
pTime = 0

mpHands = mp.solutions.hands
# Edit the maximum no of hands here, I would suggest to keep it at 1 (default) for better fps.
hands = mpHands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mpDraw = mp.solutions.drawing_utils
cap = cv2.VideoCapture(0)
while True:

    _, frame = cap.read()

    x, y, c = frame.shape

    frame = cv2.flip(frame, 1)
    framergb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    result = hands.process(framergb)


    className = ''

    if result.multi_hand_landmarks:
        landmarks = []
        for handslms in result.multi_hand_landmarks:
            for lm in handslms.landmark:
                print(id, lm)
                lmx = int(lm.x * x)
                lmy = int(lm.y * y)

                landmarks.append([lmx, lmy])

            mpDraw.draw_landmarks(frame, handslms, mpHands.HAND_CONNECTIONS)

    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime


    cv2.putText(frame, f'FPS:{int(fps)}', (20, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.imshow("Output", frame)




    if cv2.waitKey(1) == ord('q'):
        break

cap.release()

cv2.destroyAllWindows()
