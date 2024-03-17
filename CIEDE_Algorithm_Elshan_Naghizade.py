import cv2
import numpy as np

def click_event(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        src, lab_image, threshold, image_path = params
        clicked_color_lab = cv2.cvtColor(src[y:y+1, x:x+1, :], cv2.COLOR_BGR2Lab)
        delta_e = np.sqrt(np.sum(np.square(lab_image - clicked_color_lab), axis=2))

        mask = delta_e < threshold
        highlighted_img = src.copy()
        highlighted_img[mask] = [0, 255, 0] 

        cv2.circle(highlighted_img, (x, y), radius=5, color=(0, 0, 255), thickness=-1)
        base_name = image_path.rsplit('.', 1)[0]  
        result_path = f"{base_name} x-{x} y-{y} threshold-{threshold}.jpg"
        cv2.imwrite(result_path, highlighted_img)

        # Display the result
        cv2.imshow('Highlighted Image', highlighted_img)

def closeness_driver(image_path, threshold=10):
    src = cv2.imread(image_path)
    lab_image = cv2.cvtColor(src, cv2.COLOR_BGR2Lab)
    cv2.imshow('Original Image', src)
    params = [src, lab_image, threshold, image_path]
    cv2.setMouseCallback('Original Image', click_event, params)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Provide an image path to the driver function (setting a threshold is optional)
image_path = 'image_1.jpg'
closeness_driver(image_path)
