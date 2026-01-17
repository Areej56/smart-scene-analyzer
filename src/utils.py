import cv2
import os

def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def draw_label(img, text, x, y):
    cv2.putText(
        img, text, (x, y - 10),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6, (0, 255, 0), 2
    )

