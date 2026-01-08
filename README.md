<h1 align="center">KMeans App</h1>

---

## Mô tả dự án

| Mô-đun                             | Mô tả                                                                     |
|------------------------------------|---------------------------------------------------------------------------|
| Trực Quan Hóa Kmeans            | Code vẽ giao diện bằng pygame (có phần tự xây dựng thuật toán Kmeans và sử dụng thuật toán có sẵn)   |
| Giảm Số Lượng Màu Trong Ảnh     | Giảm số lượng màu trong ảnh bằng thuật toán KMeans (giao diện Tkinter) (Sử dụng AI để xây dựng)      |

---

## Cách Hoạt Động

**1. Trực quan hóa KMeans (Pygame)**

- Nháy chuột tạo các điểm dữ liệu ngẫu nhiên trên khung bảng
- Xác định số **k** là số cụm để dữ liệu phân chia
- Bấm nút **RANDOM** để tạo ngẫu nhiên **k** điểm nhãn có màu sắc riêng biệt
- Chạy thuật toán quan sát kết quả:
  - **Thuật toán KMeans tự xây dựng** (code xây dựng từ đầu) (*Nút Run*)
  - **KMeans tích hợp sẵn của Scikit-learn** (*Nút Algorithm*)
- Mục đích:
  - Minh họa thuật toán **học không giám sát** - Trực quan hóa cách các cụm được hình thành, tâm cụm được cập nhật và sai số giảm dần
  - Giúp người dùng so sánh giữa quá trình học từng bước và cách thư viện trừu tượng hóa

**2. Giảm số lượng màu trong ảnh bằng KMeans (Giao diện Tkinter)**

- Thiết lập số lượng **cụm (k)** là số lượng màu trong ảnh
- Tải lên các tệp `.jpg`, `.png`, `.jpeg`, `.bmp`, `.gif`, `.tiff`, ...
- Kết quả:
  - Hiển thị cả ảnh **gốc** và ảnh **đã xử lý** còn k màu
  - Lưu ảnh đã xử lý với định dạng phù hợp trong thư mục `assets/`
- Ứng dụng:
  - **Giảm kích thước ảnh** bằng cách tối thiểu hóa số lượng màu
  - **Tiền xử lý dữ liệu ảnh** cho các mô hình học máy
  - **Tạo hiệu ứng nghệ thuật tối giản** từ ảnh thực tế
  - **Trích xuất màu chủ đạo** phục vụ gợi ý sản phẩm (thời trang, nội thất, ...)

---

## Demo

|    Giao diện Trực Quan Hóa Kmeans                                                                            |    Ứng Dụng Giảm Màu Ảnh |
|-------------------------------------------------------------------------------------------------------------|--------------------------|
| ![img](https://github.com/PhungDinhQuangAnh/Kmeans_App/blob/main/assets/kmeans_visualization_app_demo.png)  | ![img](https://github.com/PhungDinhQuangAnh/Kmeans_App/blob/main/assets/kmeans_image_app_demo.png)  |

| Ảnh Gốc                                                                                | Ảnh Đã Xử Lí Còn 10 Màu             |
|----------------------------------------------------------------------------------------|-------------------------------------|
| ![Original](https://github.com/PhungDinhQuangAnh/Kmeans_App/blob/main/assets/test.jpg) | ![Processed](https://github.com/PhungDinhQuangAnh/Kmeans_App/blob/main/assets/test_processed.jpg) |
|*size: 1080 x 1350 - 374.5KB*                                                           |*size: 1080 x 1350 - 316.1 KB*       |

---

## Cấu Trúc Dự Án

```
Kmeans_App/
│
├── assets/                     # Ảnh đầu ra & bản demo
├── kmeans_image_processing.py  # Giao diện Tkinter giúp nén màu ảnh (xây dựng bởi AI)
├── kmeans_visualization.py     # Ứng dụng Pygame để trực quan hóa phân cụm KMeans
├── requirements.txt            # Các thư viện cần thiết
└── README.md
```

---

## Thư viện Sử Dụng

- **Scikit-learn** – dùng cho thuật toán phân cụm (KMeans)
- **Pygame** – dùng để tạo giao diện trực quan hóa phân cụm Kmeans
- **Tkinter** – dùng cho giao diện xử lý ảnh
- **NumPy** – dùng cho các phép toán số học
- **Pillow (PIL)** – dùng để tải và lưu hình ảnh
