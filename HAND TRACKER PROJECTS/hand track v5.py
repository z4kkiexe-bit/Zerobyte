import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8, maxHands=2)

def count_fingers(hand):
    fingers = detector.fingersUp(hand)
    return sum(fingers)

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)

    hands, img = detector.findHands(img)

    total = 0
    left_count = 0
    right_count = 0

    if hands:
        for hand in hands:
            count = count_fingers(hand)

            if hand["type"] == "Left":
                left_count = count
            else:
                right_count = count

        total = left_count + right_count

    # tampilkan angka
    cv2.putText(img, f"Left: {left_count}", (50, 100),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

    cv2.putText(img, f"Right: {right_count}", (50, 150),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

    cv2.putText(img, f"Total: {total}", (50, 220),
                cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0,0,255), 3)

    cv2.imshow("Finger Counter", img)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()