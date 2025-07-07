import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import numpy as np
from sklearn.cluster import KMeans
import os

def reduce_colors(image_path, n_colors=10):
    img = Image.open(image_path).convert("RGB")
    img_np = np.array(img)
    h, w = img_np.shape[:2]
    img_flat = img_np.reshape(-1, 3)

    kmeans = KMeans(n_clusters=n_colors, random_state=42).fit(img_flat)
    new_colors = kmeans.cluster_centers_.astype('uint8')
    labels = kmeans.predict(img_flat)
    img_recolored = new_colors[labels].reshape(h, w, 3)

    # Image for GUI display
    display_img = Image.fromarray(img_recolored)
    return img, display_img, img_recolored

def upload_image():
    file_path = filedialog.askopenfilename(
        filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif *.tiff *.tif *.webp *.ico *.ppm *.pgm")])
    if file_path:
        try:
            k = int(entry_k.get())
            if k <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number of colors (> 0)")
            return

        original_img, processed_img, processed_np = reduce_colors(file_path, n_colors=k)
        base_name, ext = os.path.splitext(os.path.basename(file_path))
        ext = ext.lower()
        save_path = f"assets/{base_name}_processed{ext}"

        try:
            if ext in ['.jpg', '.jpeg']:
                Image.fromarray(processed_np).save(save_path, format="JPEG", quality=70, optimize=True)
            elif ext in ['.png']:
                Image.fromarray(processed_np).convert("P", palette=Image.ADAPTIVE).save(save_path, format="PNG", optimize=True)
            else:
                Image.fromarray(processed_np).save(save_path)
        except Exception as e:
            messagebox.showwarning("Warning", f"Image saved but not optimized. Reason: {str(e)}")
            Image.fromarray(processed_np).save(save_path)

        show_images(original_img, processed_img)
        messagebox.showinfo("Done", f"Processed image saved at:\n{save_path}")
        label_path.config(text=f"💾 Saved to: {save_path}")

def show_images(img1, img2):
    for widget in display_frame.winfo_children():
        widget.destroy()

    img_max_width = 400
    img_max_height = 400

    def prepare_image(img):
        w, h = img.size
        scale = min(img_max_width / w, img_max_height / h, 1)
        new_w = int(w * scale)
        new_h = int(h * scale)
        return img.resize((new_w, new_h)), new_w, new_h

    img1_resized, _, _ = prepare_image(img1)
    img2_resized, _, _ = prepare_image(img2)

    tk_img1 = ImageTk.PhotoImage(img1_resized)
    tk_img2 = ImageTk.PhotoImage(img2_resized)

    panel1 = tk.Label(display_frame, image=tk_img1, bg="#eee", bd=2, relief="solid")
    panel1.image = tk_img1
    panel1.grid(row=0, column=0, padx=40, pady=(10, 4))

    panel2 = tk.Label(display_frame, image=tk_img2, bg="#eee", bd=2, relief="solid")
    panel2.image = tk_img2
    panel2.grid(row=0, column=1, padx=40, pady=(10, 4))

    tk.Label(display_frame, text="🖼 Original Image", font=("Segoe UI", 12, "bold"), bg="#f5f5f5").grid(row=1, column=0)
    tk.Label(display_frame, text="🎨 Processed Image", font=("Segoe UI", 12, "bold"), bg="#f5f5f5").grid(row=1, column=1)

# ===== GUI SETUP =====
root = tk.Tk()
root.title("🎨 KMeans Image Color Reduction")
root.geometry("1100x750")
root.configure(bg="#f5f5f5")
root.resizable(False, False)

# Title
tk.Label(root, text="KMEANS COLOR REDUCTION", font=("Segoe UI", 24, "bold"), fg="#333", bg="#f5f5f5").pack(pady=(20, 6))
tk.Label(root, text="Upload an image and reduce its colors using KMeans clustering",
         font=("Segoe UI", 12), fg="#555", bg="#f5f5f5").pack()

# Controls
control_frame = tk.Frame(root, bg="#f5f5f5")
control_frame.pack(pady=14)

tk.Label(control_frame, text="🎯 Number of Colors (k):", font=("Segoe UI", 13), bg="#f5f5f5").grid(row=0, column=0, padx=5)

entry_k = tk.Entry(control_frame, font=("Segoe UI", 13), width=5)
entry_k.insert(0, "10")
entry_k.grid(row=0, column=1, padx=5)

tk.Button(control_frame, text="📂 Upload Image", font=("Segoe UI", 13, "bold"),
          bg="#007bff", fg="white", activebackground="#0056b3",
          relief="flat", padx=20, pady=7, command=upload_image).grid(row=0, column=2, padx=20)

# Display frame
display_frame = tk.Frame(root, bg="#f5f5f5")
display_frame.pack(pady=20)

# Initial placeholder
placeholder = tk.Label(display_frame, text="🖼️ Image Display Area", font=("Segoe UI", 13),
                       bg="#eee", width=90, height=20, relief="solid", bd=2)
placeholder.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Save path
label_path = tk.Label(root, text="", font=("Segoe UI", 10), fg="#444", bg="#f5f5f5")
label_path.pack(pady=8)

# Footer
tk.Label(root, text="Set number of colors, upload image, then click to process",
         font=("Segoe UI", 10), bg="#f5f5f5", fg="#777").pack(pady=8)

root.mainloop()
