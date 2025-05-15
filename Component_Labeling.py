import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.measure import label, regionprops
import pandas as pd

#Step 1: Read Image
image = cv2.imread(r'nw_03.png')  # Load image (BGR format)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#Step 2: Apply manual threshold
_, bw = cv2.threshold(gray, 160, 255, cv2.THRESH_BINARY)

#Step 3: Label connected component
binary = bw > 0
labeled = label(binary, connectivity=2)  # 8-connected components

print(labeled)

#Step 4: Save label matrix to CSV ---
pd.DataFrame(labeled).to_csv('binary_output.csv', index=False, header=False)

#Step 5: Display result with labels on top ---
# Create RGB image for visualization
colored_label = np.zeros((*labeled.shape, 3), dtype=np.uint8)
num_labels = labeled.max()
colors = plt.cm.jet(np.linspace(0, 1, num_labels + 1))[:, :3] * 255

for y in range(labeled.shape[0]):
    for x in range(labeled.shape[1]):
        if labeled[y, x] > 0:
            colored_label[y, x] = colors[labeled[y, x]].astype(np.uint8)

#Step 6: Annotate labels with centroids ---
props = regionprops(labeled)

plt.figure(figsize=(8, 8))
plt.imshow(colored_label)
plt.title('Connected Components with Labels')

for i, region in enumerate(props):
    y, x = region.centroid
    plt.text(x, y, str(region.label), color='white',
             fontsize=10, weight='bold', ha='center')

plt.axis('off')
plt.show()
