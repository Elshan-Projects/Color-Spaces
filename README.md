_The captured images are stored in the "Original Images" folder (image_1.jpg, image_2.jpg, image_3.jpg)._

# 1. Grey Scale Conversion
+ The resulting conversion images are located in the "Grey Scale Images" folder which contains a separate subfolder for each test image.
### Qualitative Analysis
+ The NTSC greyscale conversion showed better outcomes in capturing shadows and semi-shadows for Images 1 and 2, whereas the 1/3 weights conversion method was better at distinguishing between darker color hues under the belly of the dog in Image 1 and around the ears in Image 2.
+ For Image 3, the nearly identical resulting images for both conversion methods are due to the image's uniform lighting and contrasting colors of the carpet.
### Quantitative Analysis
When comparing the greyscale conversions of three images using both the NTSC and 1/3 weight methods, the Peak Signal-to-Noise Ratio (PSNR) and Structural Similarity Index (SSIM) were used as metrics.
+ **Image 1**: The NTSC method yields a significantly higher PSNR of 77.99 compared to 27.05 for the 1/3 weights method, suggesting that the NTSC conversion retains a much closer match to the original image in terms of signal accuracy. Similarly, the SSIM is perfect (1.0000) for NTSC, indicating an exact match, while the 1/3 weights method scores slightly lower at 0.9872, implying a very high but not perfect structural similarity.
+ **Image 2**: Similar to Image 1, the NTSC method outperforms the 1/3 weights method with a higher PSNR (79.99 vs. 36.17) and a perfect SSIM score (1.0000) compared to a slightly lower SSIM (0.9902) for the 1/3 weights. This suggests that, as with Image 1, the NTSC conversion maintains a closer fidelity to the original image's detail and structure.
+ **Image 3**: The NTSC method shows a higher PSNR (85.40) than the 1/3 weights method (40.69), with both methods achieving very high to perfect SSIM scores (1.0000 for NTSC and 0.9985 for 1/3 weights). The quantitative metrics suggest excellent performance by both methods, with NTSC having a slight edge in signal accuracy.
### Instructions
+ The script name _Grey_Scale_Elshan_Naghizade.py_
+ Dependencies: Pillow, matplotlib, numpy, scikit-image (Use __pip install _package name___ to install)
+ Driver Function: grey_scale_driver("IMAGE_PATH")
+ Run the script and then call the driver function with the image path as its parameter
+ The driver function will display the original image along with the NTSC and 1/3 conversion results and then save the resulting images in the same folder that contains the script.
### Code Overview
+ **convert_to_ntsc_greyscale(image)**: Converts an RGB image to greyscale using NTSC coefficients (0.2989 for Red, 0.5870 for Green, and 0.1140 for Blue), which are intended to reflect the human eye's sensitivity to these colors.
+ **convert_to_one_third_greyscale(image)**: Converts an RGB image to greyscale by averaging the three color channels (Red, Green, Blue) equally, giving each one-third weight.
+ **calculate_metrics(original_image, converted_image)**: Calculates and returns the Peak Signal-to-Noise Ratio (PSNR) and the Structural Similarity Index (SSIM) between the original image and a converted greyscale image. These metrics assess the quality of the conversion in terms of signal accuracy and perceived visual similarity, respectively.
+ **save_and_show_images(original_image, ntsc_grey_image, one_third_grey_image, original_path)**: Saves the greyscale images (converted through both methods) with specific filenames indicating the conversion method. Then, it displays the original image alongside the two greyscale versions in a single figure for visual comparison.
+ **grey_scale_driver(image_path)**: Acts as the driver function for the entire script. It opens the specified image file, performs both greyscale conversions, calculates PSNR and SSIM for each conversion method, prints these metrics, and invokes save_and_show_images to save and display the results.

# 2. Color Quantization
+ The quantizations of the images are located in the "Color Quantization Images" folder with a separate subfolder for each test image. Consequently every test image's subfolder contains 2 subfolders (Uniform and K-means Quantization). Those subfolders contain the quantizations with the following numbers of buckets (2,4,8,12,16,32,64,128) for their respective quantization algorithm
### Instructions
+ The script name _Color_Quantization_Elshan_Naghizade.py_
+ Dependencies: numpy pillow matplotlib scikit-learn (Use __pip install _package name___ to install)
+ Driver Function: _quantization_driver('image path', n_buckets_list)_
+ Run the script and then call the driver function with the image path and n_buckets_list as its parameters
+ _n_bucket_list_ is a list containing integer values denoting the buckets for which the Uniform and K-Means quantization will be performed
+ The driver function will display the original image along with the resulting images for every bucket number for both algorithms and then save them under the following naming convention: __name of the file + the algorithm + bucket size__
### Code Overview
+ **uniform_quantization(image, n_buckets)**: Reduces the number of colors in the image to n_buckets by uniformly quantizing the RGB space. It calculates quantization levels based on the number of buckets, then applies this quantization to the image. The function returns the quantized image.
+ **k_means_quantization(image, n_clusters)**: Applies K-means clustering to reduce the number of colors in the image to n_clusters. It reshapes the image into a 2D array where each row represents a pixel, then uses K-means clustering to find n_clusters number of clusters in the color space. Each pixel's color is replaced with the closest cluster center's color. The function returns the image reconstructed with the new quantized colors.
+ **quantization_driver(image_path, n_buckets_list)**: The main driver function for performing and displaying color quantization. It loads an original image from image_path, applies both uniform quantization and K-means quantization with the number of buckets specified in n_buckets_list, displays the original and quantized images, and saves the quantized images using the aforementioned naming convention. The function does not return a value but shows the results and saves the quantized images.

# 3. Hue, Saturation, Brightness, Lightness
+ The resulting images with both positive and negative alterations are located in the "Hue, Saturation, Brightness, Lightness" folder. The name of each file reflects the changed paramter and the value of that change.
### Instructions
+ The script name _Hue_Saturation_Brightness_Lightness__Elshan Naghizade.py_
+ Dependencies: pillow matplotlib numpy (Use __pip install _package name___ to install)
+ Driver Function: ***HSBL_driver("image_1.jpg", adjustments)***
+ To use the HSBL_driver function, you should pass two parameters: the path to your image file and a list of adjustments you want to apply. The structure of the adjustments list consists of tuples, where each tuple contains three elements: the parameter name (as a string) to be adjusted ("hue", "saturation", "brightness", or "lightness"), the value of the adjustment (as a number), and the direction of the adjustment (either "increase" or "decrease" as a string). This list allows you to specify multiple adjustments in sequence, enabling complex color transformations on the image. Since Pillow automatically crops the ranges, the user doesn't have to consider the out-of-range problem.
+ It will display the original image and the resulting images, consequently saving them in the same folder that contains the script under the following naming convention:
***name of the file + the changed parameter (for instance, hue) + the change value + increase/decrease***
### Code Overview
+ **adjust_hsv(image, parameter, change, direction)**: This function adjusts the hue, saturation, or brightness (value) of an image based on the specified parameter (either 'hue', 'saturation', or 'brightness'), the change in the parameter's value, and the direction of the change ('increase' or 'decrease'). It modifies the image in the HSV color space and returns the adjusted image in RGB format.
+ **adjust_lightness(image, change, direction)**: Adjusts the lightness of an image by manipulating its HSL values. The change specifies how much to adjust the lightness, and direction determines whether to increase or decrease it. This function works by converting RGB to HSL, adjusting the lightness, then converting back to RGB, and returning the adjusted image.
+ **HSBL_driver(image_path, adjustments)**: The driver function for applying adjustments to an image based on a list of adjustments. Each adjustment in the list is a tuple containing the parameter to adjust (hue, saturation, brightness, or lightness), the amount of change, and the direction ('increase' or 'decrease'). The function opens the image from image_path, applies all specified adjustments, displays the original and adjusted images side by side, and saves the adjusted images using the aforementioned naming convention that includes the adjustment details.
# 4. CIEDE Closeness
+ The resulting images are located in the "CIEDE Closeness Images" folder which has separate subfolders for each test image. Those subfolders contain sample runs of the program, where the clicked pixel is marked with a red dot and the similarly colored areas are highlighted as green. The names of those files reflect the x/y position of the clicked pixel and the threshold value for the CIEDE algorithm.
### Instructions
+ The script name: _CIEDE_Algorithm_Elshan_Naghizade.py_
+ Dependencies: opencv-python numpy (Use __pip install _package name___ to install)
+ Driver Function: ***closeness_driver(image_path)***
+ Set the ***image_path*** variable in the script. (setting a threshold is optional)
+ Run the script. (The "threshold=10" default parameter is optional but can be set as the second parameter of the driver function.)
+ Once application starts the original image will be displayed. Use the crosshair to select a pixel position. Another window will pop up marking the chosen pixel positiion with a red dot and highlighting the areas with close (similar) colors with green on the image. The resulting image will be saved under the following naming convention:
<br>***name of the file + x/y position of the chosen pixel + threshold value*** in the same folder that contains the script.
+ To exit the app close both windows (the original image and the resulting image)
### Code Overview
+ **click_event(event, x, y, flags, params)**: This function acts as an event handler for mouse clicks within an OpenCV window. On a left button click (cv2.EVENT_LBUTTONDOWN), it computes the color difference (Delta E) between the clicked pixel and all other pixels in the image, highlights similar colors based on the threshold, marks the clicked position with a circle, saves the highlighted image with the aforementioned naming convention, and then displays this result. The params include the source image, its LAB color space representation, the similarity threshold, and the image path.
+ **closeness_driver(image_path, threshold=10)**: This is the driver function for the color similarity demonstration. It loads an image from image_path, converts it to the LAB color space for more accurate color difference computation, displays the original image in an OpenCV window, and sets up a mouse click callback to click_event with the necessary parameters (src, lab_image, threshold, image_path). It then waits for a user interaction and closes all OpenCV windows upon completion.


