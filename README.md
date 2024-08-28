# Image Compression using K-Means Clustering

This project demonstrates how to compress images using the K-means clustering algorithm in Python.

## Overview

By reducing the number of colors in an image, we can achieve compression while maintaining visual similarity to the original image. This technique is useful for reducing file sizes and is often applied in image processing.

## Features

- **Efficient Compression**: Uses MiniBatchKMeans from scikit-learn for efficient clustering on large images.
- **Visual Comparison**: Displays the compressed image alongside the original for visual comparison.
- **Centroid Colors Display**: Shows the colors of the centroids used in the compressed image.

## Getting Started

### Prerequisites

- Python 3.x
- `numpy`
- `Pillow`
- `scikit-learn`
- `matplotlib`

You can install these dependencies using pip:

```bash
pip install numpy Pillow scikit-learn matplotlib
```

## Getting Started

**1. Clone the repository:**    
  
  git clone https://github.com/missochan/image_compression.git  
  cd image_compression

**2. Run the main.py script to see the compression in action with sample images:**  
  
  python main.py

**3. To use your own images, replace the image paths in main.py with the path to your image files.**

## Example
The repository includes example images (ikeashark.JPG, pancake_burger.JPG) for demonstration. (which is my favourite plusie and food!) You can replace these with your own images to test the compression.

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contact
For inquiries or feedback, please feel free to reach out to me (mailto:mschanolivia@gmail.com)


