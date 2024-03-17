import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

def uniform_quantization(image, n_buckets):
    levels = 256 // n_buckets  
    quantized_image = (image // levels) * levels
    return quantized_image

def k_means_quantization(image, n_clusters):
    w, h, d = original_shape = tuple(image.shape)
    image_array = np.reshape(image, (w * h, d))
    kmeans = KMeans(n_clusters=n_clusters, random_state=0).fit(image_array)
    labels = kmeans.predict(image_array)
    quantized_image = kmeans.cluster_centers_.astype('uint8')[labels]
    return quantized_image.reshape(w, h, d)

def quantization_driver(image_path, n_buckets_list):
    original_image = Image.open(image_path)
    original_array = np.array(original_image)
    
    plt.figure(figsize=(10, len(n_buckets_list) * 5))
    plt.subplot(len(n_buckets_list) + 1, 2, 1)
    plt.imshow(original_image)
    plt.title('Original Image')
    plt.axis('off')
    
    for i, n_buckets in enumerate(n_buckets_list, start=2):
        uq_image = uniform_quantization(original_array, n_buckets)
        plt.subplot(len(n_buckets_list) + 1, 2, i * 2 - 1)
        plt.imshow(uq_image)
        plt.title(f'Uniform Quantization - {n_buckets} Buckets')
        plt.axis('off')
        Image.fromarray(uq_image).save(f"{image_path.split('.')[0]} - Uniform Quantization - {n_buckets} Buckets.jpg")
        
        km_image = k_means_quantization(original_array, n_buckets)
        plt.subplot(len(n_buckets_list) + 1, 2, i * 2)
        plt.imshow(km_image)
        plt.title(f'K-means - {n_buckets} Buckets')
        plt.axis('off')
        Image.fromarray(km_image).save(f"{image_path.split('.')[0]} - K-means - {n_buckets} Buckets.jpg")
    
    plt.tight_layout()
    plt.show()


n_buckets_list = [2, 4, 8, 12, 16, 32, 64, 128]
# Provide an image path to the driver function
#quantization_driver('image_1.jpg', n_buckets_list)