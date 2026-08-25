import cv2
import numpy as np
import math
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8, maxHands=2)

scale = 100
angle_x, angle_y = 0, 0

# posisi cube di layar
cube_pos = np.array([0, 0], dtype=float)

cube_points = np.array([
    [-1, -1, -1],
    [1, -1, -1],
    [1,  1, -1],
    [-1, 1, -1],
    [-1, -1,  1],
    [1, -1,  1],
    [1,  1,  1],
    [-1, 1,  1]
])

edges = [
    (0,1),(1,2),(2,3),(3,0),
    (4,5),(5,6),(6,7),(7,4),
    (0,4),(1,5),(2,6),(3,7)
]

def project(points, scale, angle_x, angle_y, center, offset):
    projected = []
    cx, cy = center

    for p in points:
        x, y, z = p * scale

        # rotate X
        cosx = math.cos(angle_x)
        sinx = math.sin(angle_x)
        y, z = y * cosx - z * sinx, y * sinx + z * cosx

        # rotate Y
        cosy = math.cos(angle_y)
        siny = math.sin(angle_y)
        x, z = x * cosy + z * siny, -x * siny + z * cosy

        f = 500 / (z + 500)

        x2 = int(x * f + cx + offset[0])
        y2 = int(y * f + cy + offset[1])

        projected.append((x2, y2))

    return projected

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    h, w, _ = img.shape

    hands, img = detector.findHands(img)

    left = None
    right = None

    if hands:
        for hand in hands:
            if hand["type"] == "Left":
                left = hand
            else:
                right = hand

    # ================= MOVE (LEFT HAND) =================
    if left:
        lm = left["lmList"]
        cx, cy = lm[0][0], lm[0][1]

        # offset dari tengah layar → supaya cube ikut geser
        cube_pos[0] = cx - w // 2
        cube_pos[1] = cy - h // 2

    # ================= ROTATE + SCALE (RIGHT HAND) =================
    if right:
        lm = right["lmList"]

        ix, iy = lm[8][0], lm[8][1]
        tx, ty = lm[4][0], lm[4][1]

        # SCALE dari pinch
        distance = math.hypot(ix - tx, iy - ty)
        scale = int(distance * 2)
        scale = max(50, min(scale, 200))

        # ROTATE dari posisi tangan
        cx = lm[0][0]
        cy = lm[0][1]

        angle_y = (cx - w / 2) / 200
        angle_x = (cy - h / 2) / 200

    # ================= RENDER =================
    pts = project(
        cube_points,
        scale,
        angle_x,
        angle_y,
        (w // 2, h // 2),
        cube_pos
    )

    # edges
    for edge in edges:
        cv2.line(img, pts[edge[0]], pts[edge[1]], (0, 255, 0), 2)

    # vertex points
    for pt in pts:
        cv2.circle(img, pt, 5, (0, 0, 255), cv2.FILLED)

    cv2.imshow("Fixed 3D Cube", img)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()