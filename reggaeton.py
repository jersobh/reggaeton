# reggaeton.py

import cv2
import numpy as np

def compare_images(image_path1, image_path2, threshold=30):
    """
    Compare two images and find differences.

    Parameters:
    - image_path1: str, path to the first image.
    - image_path2: str, path to the second image.
    - threshold: int, threshold value for difference sensitivity.

    Returns:
    - image with differences highlighted (if any), or None if no significant differences are found.
    """
    image1 = cv2.imread(image_path1)
    image2 = cv2.imread(image_path2)

    gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    difference = cv2.absdiff(gray1, gray2)
    _, diff_thresh = cv2.threshold(difference, threshold, 255, cv2.THRESH_BINARY)

    contours, _ = cv2.findContours(diff_thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(image1, (x, y), (x + w, y + h), (0, 0, 255), 2)
        return image1
    else:
        return None
