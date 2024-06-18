import cv2
import numpy as np
from django.conf import settings

def process_image(image_path):
    image_full_path = settings.MEDIA_ROOT / image_path
    image = cv2.imread(str(image_full_path))
    if image is None:
        return {'error': 'Image not found or unreadable'}

    # Assuming the strip is vertical and we need to detect 10 horizontal segments
    strip_height, strip_width, _ = image.shape
    segment_height = strip_height // 10
    colors = []

    for i in range(10):
        segment = image[i * segment_height:(i + 1) * segment_height, :]
        avg_color_per_row = np.average(segment, axis=0)
        avg_color = np.average(avg_color_per_row, axis=0)
        colors.append({
            'R': int(avg_color[2]),
            'G': int(avg_color[1]),
            'B': int(avg_color[0]),
        })

    return colors
