"""
Image Filter Toolkit - Edge Detection & Artistic Filters
Author: Yuseph Alvandi
Description: Apply edge detection and artistic filters with live preview.
"""

import customtkinter as ctk
from tkinter import filedialog, messagebox
import cv2
import numpy as np
from PIL import Image, ImageTk
import os

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class ImageFilterApp:
    def __init__(self):
        self.window = ctk.CTk()
        self.window.title("Image Filter Toolkit")
        self.window.geometry("1200x800")
        self.window.configure(fg_color="#0a0a0a")
        
        self.image_path = None
        self.original_img = None
        self.current_img = None
        
        self.edge_sensitivity = ctk.IntVar(value=50)
        self.blur_amount = ctk.IntVar(value=5)
        self.filter_mode = ctk.StringVar(value="original")
        
        self.setup_ui()
    
    def setup_ui(self):
        # ===== HEADER =====
        header = ctk.CTkFrame(self.window, fg_color="transparent")
        header.pack(fill="x", pady=(20, 10), padx=30)
        ctk.CTkLabel(header, text="Image Filter Toolkit", font=ctk.CTkFont(size=32, weight="bold"), text_color="#1E90FF").pack()
        ctk.CTkLabel(header, text="Edge Detection, Blur, Sharpen, Invert, Grayscale — live preview", font=ctk.CTkFont(size=14), text_color="#AAAAAA").pack()
        
        # ===== TOOLBAR =====
        toolbar = ctk.CTkFrame(self.window, fg_color="#1a1a1a", corner_radius=12, height=60)
        toolbar.pack(fill="x", padx=30, pady=(5, 10))
        toolbar.pack_propagate(False)
        
        ctk.CTkButton(toolbar, text="Open Image", command=self.open_image, width=150, height=40, font=ctk.CTkFont(size=14)).pack(side="left", padx=(20, 10), pady=10)
        ctk.CTkButton(toolbar, text="Save Result", command=self.save_result, width=150, height=40, fg_color="#2ECC71", font=ctk.CTkFont(size=14)).pack(side="left", padx=10, pady=10)
        
        self.file_label = ctk.CTkLabel(toolbar, text="No file selected", text_color="#888888", font=ctk.CTkFont(size=12))
        self.file_label.pack(side="left", padx=20, pady=10)
        
        # ===== MAIN CONTENT =====
        content = ctk.CTkFrame(self.window, fg_color="transparent")
        content.pack(fill="both", expand=True, padx=30, pady=10)
        
        # Left panel
        left = ctk.CTkFrame(content, fg_color="#1a1a1a", corner_radius=12, width=380)
        left.pack(side="left", fill="y", padx=(0, 10))
        left.pack_propagate(False)
        
        ctk.CTkLabel(left, text="Quick Filters", font=ctk.CTkFont(size=16, weight="bold"), text_color="#1E90FF").pack(pady=(20, 10))
        
        filters = [
            ("Original", "original"),
            ("Grayscale", "grayscale"),
            ("Invert Colors", "invert"),
            ("Sharpen", "sharpen"),
            ("Edge Detection", "edge"),
            ("Blur", "blur"),
        ]
        
        for text, mode in filters:
            ctk.CTkButton(left, text=text, width=250, height=38, command=lambda m=mode: self.set_filter(m), font=ctk.CTkFont(size=13)).pack(pady=4, padx=30)
        
        # Edge Sensitivity
        ctk.CTkLabel(left, text="Edge Sensitivity", font=ctk.CTkFont(size=14, weight="bold"), text_color="#CCCCCC").pack(pady=(20, 5))
        ctk.CTkLabel(left, text="Higher = more edges detected", font=ctk.CTkFont(size=10), text_color="#888888").pack()
        ctk.CTkSlider(left, from_=1, to=100, variable=self.edge_sensitivity, width=250, command=self.on_slider_change).pack()
        self.edge_label = ctk.CTkLabel(left, text="50", font=ctk.CTkFont(size=11), text_color="#1E90FF")
        self.edge_label.pack()
        
        # Blur Amount
        ctk.CTkLabel(left, text="Blur Amount", font=ctk.CTkFont(size=14, weight="bold"), text_color="#CCCCCC").pack(pady=(15, 5))
        ctk.CTkLabel(left, text="Higher = more blur", font=ctk.CTkFont(size=10), text_color="#888888").pack()
        ctk.CTkSlider(left, from_=1, to=25, variable=self.blur_amount, width=250, command=self.on_slider_change).pack()
        self.blur_label = ctk.CTkLabel(left, text="5", font=ctk.CTkFont(size=11), text_color="#1E90FF")
        self.blur_label.pack()
        
        self.status_label = ctk.CTkLabel(left, text="Ready", text_color="#4CAF50", font=ctk.CTkFont(size=11))
        self.status_label.pack(pady=15)
        
        # Right panel (Preview)
        right = ctk.CTkFrame(content, fg_color="#1a1a1a", corner_radius=12)
        right.pack(side="right", fill="both", expand=True)
        
        self.preview_label = ctk.CTkLabel(right, text="No Image Loaded", font=ctk.CTkFont(size=16), text_color="#555555")
        self.preview_label.pack(expand=True)
    
    def open_image(self):
        path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp")])
        if not path:
            return
        
        self.image_path = path
        self.original_img = cv2.imread(path)
        self.file_label.configure(text=os.path.basename(path))
        self.status_label.configure(text="Image loaded. Select a filter or adjust sliders.", text_color="#4CAF50")
        self.filter_mode.set("original")
        self.apply_filter()
    
    def set_filter(self, mode):
        self.filter_mode.set(mode)
        if self.original_img is not None:
            self.apply_filter()
    
    def on_slider_change(self, value):
        self.edge_label.configure(text=str(self.edge_sensitivity.get()))
        self.blur_label.configure(text=str(self.blur_amount.get()))
        if self.original_img is not None:
            self.apply_filter()
    
    def apply_filter(self):
        if self.original_img is None:
            return
        
        img = self.original_img.copy()
        mode = self.filter_mode.get()
        
        if mode == "grayscale":
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
        elif mode == "invert":
            img = cv2.bitwise_not(img)
        elif mode == "sharpen":
            kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
            img = cv2.filter2D(img, -1, kernel)
        elif mode == "edge":
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            # Convert single sensitivity (1-100) to Canny thresholds
            s = self.edge_sensitivity.get()
            low = max(10, s * 2)
            high = low * 3
            edges = cv2.Canny(gray, low, high)
            img = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
        elif mode == "blur":
            k = self.blur_amount.get()
            if k % 2 == 0:
                k += 1
            img = cv2.GaussianBlur(img, (k, k), 0)
        
        self.current_img = img
        
        rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        pil_img = Image.fromarray(rgb)
        preview_w = 650
        ratio = preview_w / pil_img.width
        preview_h = int(pil_img.height * ratio)
        pil_img = pil_img.resize((preview_w, preview_h))
        tk_img = ImageTk.PhotoImage(pil_img)
        self.preview_label.configure(image=tk_img, text="")
        self.preview_label.image = tk_img
    
    def save_result(self):
        if self.current_img is None:
            messagebox.showerror("Error", "No processed image to save!")
            return
        
        path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG", "*.jpg"), ("PNG", "*.png")])
        if path:
            cv2.imwrite(path, self.current_img)
            self.status_label.configure(text=f"Saved: {os.path.basename(path)}", text_color="#4CAF50")
    
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = ImageFilterApp()
    app.run()
