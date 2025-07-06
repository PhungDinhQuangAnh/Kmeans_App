<h1 align="center"> 🎨 KMeans App</h1>

---

## 🧭 What This Project Offers

| Module                        | Description                                                                 |
|------------------------------|-----------------------------------------------------------------------------|
| 📊 Clustering Visualization   | Interactive 2D KMeans simulation (custom & sklearn-based, via Pygame)      |
| 🖼️ Image Color Reduction     | Reduce image colors using KMeans (Tkinter GUI)                             |

---

## 🧠 How It Works

### 📈 1. KMeans Clustering Visualization (Pygame)
- Interactively add 2D points and random centroids
- Includes both:
  - A **custom-built KMeans algorithm** (implemented from scratch) (Run Button)
  - The **built-in Scikit-learn KMeans** (Algorithm Button)
- Visualize how clusters are formed, centroids are updated, and errors decrease
- Lets users compare step-by-step learning vs. library abstraction
- Great for learning and teaching **unsupervised learning** intuitively
  
### 🖼️ 2. KMeans Image Color Reduction (Tkinter GUI)
- Upload `.jpg`, `.png`, `.jpeg`, `.bmp`, `.gif`, `.tiff`, etc.
- Set number of clusters (k) to reduce the number of colors
- Displays both the **original** and **processed** image
- Saves the processed image with appropriate format in `assets/`

---

## 📸 Demo

| 📊 KMeans Visualization App | 🖼️ Image Color Reduction App |
|--------------------------|--------------------------|
| ![img](https://github.com/PhungDinhQuangAnh/kmeans-app/blob/main/assets/kmeans_visualization_app_demo.png)  | ![img](https://github.com/PhungDinhQuangAnh/kmeans-app/blob/main/assets/kmeans_image_app_demo.png)  |

| Original Image             | Processed Image with 10 colors     |
|----------------------------------------|-------------------------------------|
| ![Original](https://github.com/PhungDinhQuangAnh/kmeans-app/blob/main/assets/test.jpg) | ![Processed](https://github.com/PhungDinhQuangAnh/kmeans-app/blob/main/assets/test_processed.jpg) |

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

## 💡 Why This Project?

This project demonstrates my ability to:

🖼️ **Image Color Reduction**
- Apply unsupervised learning for practical image compression
- Build intuitive GUI using Tkinter
- Work with image formats and color spaces

📊 **KMeans Clustering Visualization**
- Implement clustering algorithm manually from scratch
- Compare and benchmark with built-in KMeans
- Visualize clustering dynamics step-by-step
- Teach or learn clustering with visual intuition
