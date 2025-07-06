<h1 align="center"> 🎨 KMeans App – Clustering Visualization & Image Color Reduction </h1>

A complete Python GUI application to:
- 📊 Visualize and compare **KMeans algorithms** interactively with 2D point clustering
- 📂 Upload and compress images by reducing colors using **KMeans clustering**
- 🖼️ Built with **Tkinter**, **Pygame**, and **Scikit-learn**

---

## 🧭 What This Project Offers

| Module                        | Description                                                                 |
|------------------------------|-----------------------------------------------------------------------------|
| 📊 Clustering Visualization   | Interactive 2D KMeans simulation (custom & sklearn-based, via Pygame)      |
| 🎨 Image Color Reduction     | Reduce image colors using KMeans (Tkinter GUI)                             |


---

## 📸 Demo

| 🎨 Image Color Reduction | 📊 KMeans Visualization |
|--------------------------|--------------------------|
| ![img](assets/img1.png)  | ![img](assets/img2.png)  |


---

## 🚀 Features

### 📈 Clustering Visualization (Pygame)
- ✅ Interactively add 2D points and observe clustering
- ✅ Switch between **custom KMeans implementation** and **Scikit-learn KMeans**
- ✅ Visual feedback of centroid updates and error reduction
- ✅ Explore and understand unsupervised learning concepts step-by-step

### 🎨 Image Color Reduction (Tkinter GUI)
- ✅ Upload and compress images with reduced colors
- ✅ Choose number of clusters (k) interactively
- ✅ Auto-save processed images to *"assets"* folder
- ✅ Supports most common image formats
  
---

## 🧠 How It Works

### 🖼️ 1. KMeans Image Color Reduction (Tkinter GUI)
- Upload `.jpg`, `.png`, `.jpeg`, `.bmp`, `.gif`, `.tiff`, etc.
- Set number of clusters (k) to reduce the number of colors
- Displays both the **original** and **processed** image
- Saves the processed image with appropriate format in `assets/`

### 📈 2. KMeans Clustering Visualization (Pygame)
- Interactively add 2D points and random centroids
- Includes both:
  - A **custom-built KMeans algorithm** (implemented from scratch)
  - The **built-in Scikit-learn KMeans**
- Visualize how clusters are formed, centroids are updated, and errors decrease
- Lets users compare step-by-step learning vs. library abstraction
- Great for learning and teaching **unsupervised learning** intuitively

---

## 🧪 Requirements

Install dependencies using:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
# Run image color reduction app
python kmeans_image_processing.py

# Run visualization tool
python kmeans_visualization.py
```

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

## ✨ Screenshots

| Original vs Processed Image             | KMeans Clustering Visualization     |
|----------------------------------------|-------------------------------------|
| ![Processed](assets/sample_result.jpg) | ![Visualization](assets/visual.png) |

---

## 💡 Why This Project?

This project demonstrates your ability to:

🖼️ **Image Color Reduction**
- Apply unsupervised learning for practical image compression
- Build intuitive GUI using Tkinter
- Work with image formats and color spaces

📊 **KMeans Clustering Visualization**
- Implement clustering algorithm manually from scratch
- Compare and benchmark with built-in KMeans
- Visualize clustering dynamics step-by-step
- Teach or learn clustering with visual intuition
