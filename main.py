from PIL import Image
from utils import compress_image_kmeans, show_images_side_by_side, show_centroid_colors
from IPython.display import display

# Function to run the compression
def run_image_compression(image_path, k):
    image = Image.open(image_path)
    compressed_image, kmeans = compress_image_kmeans(image, k=k)

    # Display the compressed image
    display(compressed_image)

    # Display the centroid colors
    show_centroid_colors(kmeans)

    # Compare the original image and the compressed image side by side
    show_images_side_by_side(image, compressed_image)

if __name__ == "__main__":
    # Example usage
    run_image_compression('images/ikeashark.JPG', 16)
    run_image_compression('images/pancake_burger.JPG', 16)
