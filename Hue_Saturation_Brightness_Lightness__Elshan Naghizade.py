from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import colorsys

def adjust_hsv(image, parameter, change, direction):
    """Adjust Hue, Saturation, Brightness of an image."""
    hsv_image = image.convert('HSV')
    h, s, v = hsv_image.split()
    h_data = np.array(h, dtype=np.float32)
    s_data = np.array(s, dtype=np.float32)
    v_data = np.array(v, dtype=np.float32)

    if parameter == 'hue':
        change = change if direction == "increase" else -change
        h_data = (h_data + change) % 256
    elif parameter == 'saturation':
        s_data = s_data / 255.0  # Normalize to 0-1
        factor = change if direction == "increase" else 1 / change
        s_data *= factor
        np.clip(s_data, 0, 1, out=s_data)
        s_data *= 255  # Denormalize to 0-255
    elif parameter == 'brightness':
        factor = change if direction == "increase" else 1 / change
        v_data *= factor
        np.clip(v_data, 0, 255, out=v_data)

    adjusted_hsv_image = Image.merge('HSV', (Image.fromarray(h_data.astype('uint8'), 'L'),
                                             Image.fromarray(s_data.astype('uint8'), 'L'),
                                             Image.fromarray(v_data.astype('uint8'), 'L')))
    return adjusted_hsv_image.convert('RGB')

def adjust_lightness(image, change, direction):
    """Adjust Lightness of an image using colorsys for more accurate HSL manipulation."""
    rgb_image = np.array(image)
    # Convert RGB to HSL
    hls_image = np.apply_along_axis(lambda rgb: colorsys.rgb_to_hls(rgb[0]/255.0, rgb[1]/255.0, rgb[2]/255.0), 2, rgb_image)
    
    if direction == "increase":
        hls_image[:,:,1] = np.clip(hls_image[:,:,1] + change/255.0, 0, 1)
    else:
        hls_image[:,:,1] = np.clip(hls_image[:,:,1] - change/255.0, 0, 1)

    # Convert HSL back to RGB
    adjusted_rgb_image = np.apply_along_axis(lambda hls: np.array(colorsys.hls_to_rgb(hls[0], hls[1], hls[2]))*255, 2, hls_image)
    return Image.fromarray(adjusted_rgb_image.astype('uint8'))


def HSBL_driver(image_path, adjustments):
    original_image = Image.open(image_path)
    
    plt.figure(figsize=(20, 10))
    num_adjustments = len(adjustments) + 1
    plt.subplot(1, num_adjustments, 1)
    plt.imshow(original_image)
    plt.title('Original')
    plt.axis('off')
    
    for i, (parameter, value, direction) in enumerate(adjustments, start=2):
        if parameter != 'lightness':
            adjusted_image = adjust_hsv(original_image, parameter, value, direction)
        else:
            adjusted_image = adjust_lightness(original_image, value, direction)
            
        plt.subplot(1, num_adjustments, i)
        plt.imshow(adjusted_image)
        title = f'{parameter.capitalize()} {direction.capitalize()}'
        plt.title(title)
        plt.axis('off')
        
        # Save adjusted image
        base_name = image_path.rsplit('.', 1)[0]  # Strip extension
        adjusted_image.save(f"{base_name} - {parameter} - {value} - {direction}.jpg")

    plt.show()

adjustments = [
    ('hue', 20, "increase"),
    ('hue', 20, "decrease"),
    ('saturation', 1.2, "increase"),
    ('saturation', 0.8, "decrease"),
    ('brightness', 1.2, "increase"),
    ('brightness', 0.8, "decrease"),
    ('lightness', 40, "increase"),
    ('lightness', 40, "decrease"),
]

# Provide an image path to the driver function
#HSBL_driver("image_1.jpg", adjustments)
