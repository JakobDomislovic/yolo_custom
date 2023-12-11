import os
import cv2
import numpy as np

if __name__ == '__main__':
    ORGAN = 'KidneyR'
    DATASET = 'abd_corr_view'

    src_path = f'./dataset/{DATASET}/Masks{ORGAN}/'
    dst_path = f'./dataset/{DATASET}/Masks{ORGAN}_yolo_segmentation/'

    os.makedirs(dst_path, exist_ok=True)

    for mask in os.listdir(src_path):
        
        img = cv2.imread(src_path + mask)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray, 0.5, 255, cv2.THRESH_BINARY)
        
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        H, W = gray.shape

        # convert the contours to polygons
        polygons = []
        for cnt in contours:
            if cv2.contourArea(cnt) > 200:
                polygon = []
                for point in cnt:
                    x, y = point[0]
                    polygon.append(x / W)
                    polygon.append(y / H)
                polygons.append(polygon)
        # print the polygons
        with open(dst_path+mask[:-4]+'.txt', 'w') as f:
            for polygon in polygons:
                for p_, p in enumerate(polygon):
                    if p_ == len(polygon) - 1:
                        f.write('{}\n'.format(p))
                    elif p_ == 0:
                        f.write('0 {} '.format(p))
                    else:
                        f.write('{} '.format(p))