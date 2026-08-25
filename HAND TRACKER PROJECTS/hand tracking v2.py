import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8, maxHands=1)

# posisi balok awal
block_x, block_y = 300, 200
block_size = 80

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)

    hands, img = detector.findHands(img)

    if hands:
        hand = hands[0]
        lmList = hand["lmList"]

        # ambil ujung jari telunjuk (landmark 8)
        index_finger = lmList[8][0:2]
        x, y = index_finger

        # cek kalau jari menyentuh balok
        if block_x < x < block_x + block_size and block_y < y < block_y + block_size:
            block_x = x - block_size // 2
            block_y = y - block_size // 2

    # gambar balok
    cv2.rectangle(img, (block_x, block_y),
                  (block_x + block_size, block_y + block_size),
                  (255, 0, 255), cv2.FILLED)

    cv2.imshow("Hand Tracking Block", img)

    if cv2.waitKey(1) & 0xFF == 27:  # ESC untuk keluar
        break

cap.release()
cv2.destroyAllWindows()