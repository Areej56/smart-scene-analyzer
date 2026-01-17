from ultralytics import YOLO
import cv2
from utils import ensure_dir

ensure_dir("../outputs/images")

model = YOLO("../models/yolov8n-seg.pt")
img = cv2.imread("../data/images/sample.jpg")

results = model(img)

for r in results:
    if r.masks is not None:
        for mask in r.masks.xy:
            pts = mask.astype(int)
            cv2.polylines(img, [pts], True, (255,0,0), 2)

cv2.imwrite("../outputs/images/segmented.jpg", img)
cv2.imshow("Segmentation", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

