from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
from skimage.metrics import peak_signal_noise_ratio as psnr
from skimage.metrics import structural_similarity as ssim

def convert_to_ntsc_greyscale(image):
    return image.convert("L", (0.2989, 0.5870, 0.1140, 0))

def convert_to_one_third_greyscale(image):
    return image.convert("L", (1/3, 1/3, 1/3, 0))

def calculate_metrics(original_image, converted_image):
    original_array = np.array(original_image)
    converted_array = np.array(converted_image)
    
    if len(original_array.shape) > 2:
        original_array = original_array[:,:,0]
    
    psnr_value = psnr(original_array, converted_array)
    ssim_value = ssim(original_array, converted_array)
    
    return psnr_value, ssim_value

def save_and_show_images(original_image, ntsc_grey_image, one_third_grey_image, original_path):
    base_name = original_path.rsplit('.', 1)[0]  # Remove file extension
    
    ntsc_file_name = f"{base_name} - NTSC grey scale.jpg"
    one_third_file_name = f"{base_name} - 1over3 grey scale.jpg"
    
    ntsc_grey_image.save(ntsc_file_name)
    one_third_grey_image.save(one_third_file_name)
    
    plt.figure(figsize=(15, 5))
    
    plt.subplot(1, 3, 1)
    plt.imshow(original_image, cmap='gray')
    plt.title('Original Image')
    plt.axis('off')
    
    plt.subplot(1, 3, 2)
    plt.imshow(ntsc_grey_image, cmap='gray')
    plt.title('NTSC Greyscale')
    plt.axis('off')
    
    plt.subplot(1, 3, 3)
    plt.imshow(one_third_grey_image, cmap='gray')
    plt.title('1/3 Weights Greyscale')
    plt.axis('off')
    
    plt.show()

def grey_scale_driver(image_path):
    original_image = Image.open(image_path)
    original_grey = original_image.convert("L")  # Convert original to grayscale for comparison
    
    ntsc_grey_image = convert_to_ntsc_greyscale(original_image)
    one_third_grey_image = convert_to_one_third_greyscale(original_image)

    psnr_ntsc, ssim_ntsc = calculate_metrics(original_grey, ntsc_grey_image)
    psnr_one_third, ssim_one_third = calculate_metrics(original_grey, one_third_grey_image)
    
    print(f"NTSC Greyscale - PSNR: {psnr_ntsc:.2f}, SSIM: {ssim_ntsc:.4f}")
    print(f"1/3 Weights Greyscale - PSNR: {psnr_one_third:.2f}, SSIM: {ssim_one_third:.4f}")
    
    save_and_show_images(original_image, ntsc_grey_image, one_third_grey_image, image_path)


# Provide an image path to the driver function
#grey_scale_driver("image_1.jpg")