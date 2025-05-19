# Component-Labeling-Thesis
This repository contains the implementation of a component labeling algorithm as part of my undergraduate/graduate thesis. The script uses Python along with OpenCV, NumPy, and skimage to identify and label connected components in binary images.

# 🧩 Component Labeling for Image Processing

This repository contains a Python script that performs **connected component labeling** on a binary image. It is part of a thesis project focused on image segmentation and analysis using classical image processing techniques.

The script reads an input image, applies thresholding, labels each connected region using 8-connectivity, visualizes the labeled regions with distinct colors, and saves the label matrix as a CSV file.

---

## 📁 Files

- `Component_Labeling.py` – Main Python script for component labeling and visualization.
- `sanity.png` – Input image (you must provide this image in the same directory).
- `binary_output.csv` – Output CSV containing the label matrix (generated after running the script).

---

## 🚀 Getting Started

### ✅ Prerequisites

Ensure you have **Python 3.7+** installed. Then install the required libraries:

```bash
pip install opencv-python numpy matplotlib scikit-image pandas

```
---

## 📷 Output Preview

The script displays a visual plot like the output.png:

- Each connected region is colored uniquely.
- The center of each component is annotated with its label number.

---

## 📚 Libraries Used

- `OpenCV` – Image reading and preprocessing
- `NumPy` – Matrix operations
- `Matplotlib` – Visualization
- `scikit-image` – Labeling and region analysis
- `Pandas` – Exporting label matrix to CSV

---

## 👤 Author

**Lymperis Lymperidis**
**Supervisor Xenophon Zabulis**
*Thesis Project – [University of Crete]*

---

## 📷 Rendered Images

The output is being displayed in a rendering Tool as well so you can see that the component labeling worked 
See the Rendered_1 to 4 for examples

---

