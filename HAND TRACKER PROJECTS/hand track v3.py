import cv2
import math
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8, maxHands=1)

block_x, block_y = 300, 200
block_size = 80

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)

    hands, img = detector.findHands(img)

    if hands:
        hand = hands[0]
        lmList = hand["lmList"]

        # koordinat jari telunjuk & jempol
        ix, iy = lmList[8][0], lmList[8][1]
        tx, ty = lmList[4][0], lmList[4][1]

        # jarak pinch (buat resize)
        distance = math.hypot(ix - tx, iy - ty)

        # mapping jarak ke ukuran block
        block_size = int(distance * 2)

        # batas ukuran biar gak ngawur
        if block_size < 30:
            block_size = 30
        if block_size > 200:
            block_size = 200

        # drag pakai telunjuk
        if block_x < ix < block_x + block_size and block_y < iy < block_y + block_size:
            block_x = ix - block_size // 2
            block_y = iy - block_size // 2

    # gambar block
    cv2.rectangle(img,
                  (block_x, block_y),
                  (block_x + block_size, block_y + block_size),
                  (255, 0, 255),
                  cv2.FILLED)

    cv2.imshow("Hand Tracking Block Resize", img)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
