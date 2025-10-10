<h1 align="center"> 🎨 KMeans App</h1>

---

## 🧭 Những Gì Dự Án Này Mang Lại

| Mô-đun                             | Mô tả                                                                     |
|------------------------------------|---------------------------------------------------------------------------|
| 📊 Trực Quan Hóa Kmeans            | Mô phỏng KMeans 2D tương tác (tùy chỉnh & dựa trên sklearn, qua Pygame)   |
| 🖼️ Giảm Số Lượng Màu Trong Ảnh     | Giảm số lượng màu trong ảnh bằng KMeans (giao diện Tkinter)               |

---

## 🧠 Cách Hoạt Động

📈 **1. Trực quan hóa phân cụm KMeans (Pygame)**

- Thêm điểm 2D tương tác, đặt số cụm (k) và các tâm cụm ngẫu nhiên
- Bao gồm cả:
  - **Thuật toán KMeans tự xây dựng** (cài đặt từ đầu) (*Nút Run*)
  - **KMeans tích hợp sẵn của Scikit-learn** (*Nút Algorithm*)
- Trực quan hóa cách các cụm được hình thành, tâm cụm được cập nhật và sai số giảm dần
- Giúp người dùng so sánh giữa quá trình học từng bước và cách thư viện trừu tượng hóa

🖼️ **2. Giảm số lượng màu trong ảnh bằng KMeans (Giao diện Tkinter)**

- Tải lên các tệp `.jpg`, `.png`, `.jpeg`, `.bmp`, `.gif`, `.tiff`, v.v.
- Thiết lập số lượng **cụm (k)** để giảm số màu trong ảnh
- Hiển thị cả ảnh **gốc** và ảnh **đã xử lý**
- Lưu ảnh đã xử lý với định dạng phù hợp trong thư mục `assets/`

---

## 📸 Demo

| 📊 Ứng Dụng Trực Quan Hóa Kmeans                                                                            | 🖼️ Ứng Dụng Giảm Màu Ảnh |
|-------------------------------------------------------------------------------------------------------------|--------------------------|
| ![img](https://github.com/PhungDinhQuangAnh/Kmeans_App/blob/main/assets/kmeans_visualization_app_demo.png)  | ![img](https://github.com/PhungDinhQuangAnh/Kmeans_App/blob/main/assets/kmeans_image_app_demo.png)  |

| Ảnh Gốc                                                                                | Ảnh Đã Xử Lí Còn 10 Màu             |
|----------------------------------------------------------------------------------------|-------------------------------------|
| ![Original](https://github.com/PhungDinhQuangAnh/Kmeans_App/blob/main/assets/test.jpg) | ![Processed](https://github.com/PhungDinhQuangAnh/Kmeans_App/blob/main/assets/test_processed.jpg) |
|*size: 1080 x 1350 - 374.5KB*                                                           |*size: 1080 x 1350 - 316.1 KB*       |

---

## 📁 Cấu Trúc Dự Án

```
Kmeans_App/
│
├── assets/                     # Ảnh đầu ra & bản demo
├── kmeans_image_processing.py  # Giao diện Tkinter cho việc nén màu ảnh
├── kmeans_visualization.py     # Ứng dụng Pygame để trực quan hóa phân cụm KMeans
├── requirements.txt
└── README.md
```

---

## 🔧 Công Nghệ Sử Dụng

- **Python**
- **Scikit-learn** – dùng cho thuật toán phân cụm (KMeans)
- **Pygame** – dùng để trực quan hóa phân cụm tương tác
- **Tkinter** – dùng cho giao diện xử lý ảnh
- **NumPy** – dùng cho các phép toán số học
- **Pillow (PIL)** – dùng để tải và lưu hình ảnh

---


---

## ▶️ Cài Đặt Và Chạy Ứng Dụng

```bash
# Cài đặt các yêu cầu (thư viện phụ thuộc)
pip install -r requirements.txt

# Chạy ứng dụng trực quan hóa KMeans
python kmeans_visualization.py

# Chạy ứng dụng giảm số lượng màu trong ảnh
python kmeans_image_processing.py
```

---

## 🛠 Ứng dụng

📈 **Trực quan hóa phân cụm KMeans**

- ✅ **Công cụ học tập** minh họa học không giám sát
- ✅ **Thuật toán KMeans tự xây dựng** kèm so sánh song song với **KMeans của Scikit-learn**
- ✅ **Quá trình phân cụm từng bước** với hoạt ảnh gán điểm trực quan
- ✅ Phù hợp cho giảng dạy, thuyết trình hoặc hội thảo

🖼 **Giảm số lượng màu trong ảnh bằng KMeans**

- ✅ **Giảm kích thước ảnh** bằng cách tối thiểu hóa số lượng màu
- ✅ **Tiền xử lý dữ liệu ảnh** cho các mô hình học máy
- ✅ **Tạo hiệu ứng nghệ thuật tối giản** từ ảnh thực tế
- ✅ **Trích xuất màu chủ đạo** phục vụ gợi ý sản phẩm (thời trang, nội thất, v.v.)

