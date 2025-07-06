<h1 align="center"> 🎨 KMeans App</h1>

---

## 🧭 What This Project Offers

| Module                        | Description                                                                 |
|------------------------------|-----------------------------------------------------------------------------|
| 📊 Clustering Visualization   | Interactive 2D KMeans simulation (custom & sklearn-based, via Pygame)      |
| 🖼️ Image Color Reduction     | Reduce image colors using KMeans (Tkinter GUI)                             |

---

## 🧠 How It Works

📈 **1. KMeans Clustering Visualization (Pygame)**
- Interactively add 2D points and random centroids
- Includes both:
  - A **custom-built KMeans algorithm** (implemented from scratch) (Run Button)
  - The **built-in Scikit-learn KMeans** (Algorithm Button)
- Visualize how clusters are formed, centroids are updated, and errors decrease
- Lets users compare step-by-step learning vs. library abstraction

🖼️ **2. KMeans Image Color Reduction (Tkinter GUI)**
- Upload `.jpg`, `.png`, `.jpeg`, `.bmp`, `.gif`, `.tiff`, etc.
- Set number of clusters (k) to reduce the number of colors
- Displays both the **original** and **processed** image
- Saves the processed image with appropriate format in `assets/`

---

## 📸 Demo

| 📊 KMeans Visualization App | 🖼️ Image Color Reduction App |
|--------------------------|--------------------------|
| ![img](https://github.com/PhungDinhQuangAnh/kmeans-app/blob/main/assets/kmeans_visualization_app_demo.png)  | ![img](https://github.com/PhungDinhQuangAnh/kmeans-app/blob/main/assets/kmeans_visualization_app_demo.png)  |

| Original Image             | Processed Image with 10 colors     |
|----------------------------------------|-------------------------------------|
| ![Original](https://github.com/PhungDinhQuangAnh/kmeans-app/blob/main/assets/test.jpg) | ![Processed](https://github.com/PhungDinhQuangAnh/kmeans-app/blob/main/assets/test_processed.jpg) |
|*size: 1080 x 1350 - 374.5KB*|*size: 1080 x 1350 - 316.1 KB*|

---

## 📁 Project Structure

```
kmeans-app/
│
├── assets/                    # Output images & demo
├── kmeans_image_processing.py  # Tkinter GUI for image color compression
├── kmeans_visualization.py     # Pygame app for visualizing KMeans clustering
├── requirements.txt
└── README.md
```

---

## 🔧 Technologies Used

- Python 
- Scikit-learn – for clustering (KMeans)
- Pygame – for interactive clustering visualization
- Tkinter – for image processing GUI
- NumPy – for numerical operations
- Pillow (PIL) – for image loading and saving

---

## ▶️ Setup & Run Application

```bash
# Install Requirements
pip install -r requirements.txt

# Run kmeans visualization app
python kmeans_visualization.py

# Run image color reduction app
python kmeans_image_processing.py
```

---

## 🛠 Applications

📈 **KMeans Clustering Visualization**
- ✅ **Educational tool** to demonstrate unsupervised learning
- ✅ **Custom-built KMeans algorithm** with side-by-side comparison to **Scikit-learn's KMeans**
- ✅ **Step-by-step clustering process** with point assignment animations
- ✅ Great for teaching, presentations, or workshops

🖼 **KMeans Image Color Reduction**
- ✅ **Reduce image size** by minimizing the number of colors
- ✅ **Preprocess image data** for machine learning models
- ✅ **Create minimalistic artistic effects** from real-world photos
- ✅ **Extract dominant colors** for product suggestions (fashion, interior, etc.)
