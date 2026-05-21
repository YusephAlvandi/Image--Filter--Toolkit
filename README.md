Image Filter Toolkit

A real-time image processing desktop application for edge detection, applying grayscale, invert, sharpen, and blur filters instantly with live preview and saving the results.

Built with Python, OpenCV, and CustomTkinter. Appropriate for complete offline operation.


WHAT IT DOES

This toolkit applies professional image filters in real time. Open an image, click a filter, and see the result immediately in live preview; no uploads, no waste of time.

Filters included: Edge Detection (Canny), Gaussian Blur, Sharpen, Invert Colors, and Grayscale.

Adjust the parameters to desired amount with simple sliders. Save the processed images with one click.


HOW IT WORKS (THE SCIENCE)

The Canny algorithm (a foundational technique in machine vision which identifies boundaries by monitoring intensity gradients in the image) is used in edge detection. Gaussian Blur applies a kernel based on the Gaussian distribution in optics to model light diffusion. Sharpen uses a convolution kernel for enhancing fine details.

The above mentioned features are not only filters, but also the building blocks of computer vision and image-based AI systems.


COMPETITIVE ADVANTAGE

Majority of online filter tools need uploading your images to a remote server (a privacy risk). This application works totally offline. Your images never leave your local storage.

- Live preview (see changes as you manipulate the parameters)
- No internet required
- No privacy concerns
- Simple, clean desktop interface
- Built by a physicist who understands the optics behind the operations


HOW TO RUN

pip install opencv-python customtkinter pillow numpy
python image_filters.py


AUTHOR

Yuseph Alvandi
PhD in Optics and Laser Physics
Python Developer and Image Processing Specialist

GitHub: https://github.com/YusephAlvandi


LICENSE

MIT License