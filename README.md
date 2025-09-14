# Object-Detection-with-YOLOv8
A Streamlit web application for real-time object detection powered by YOLOv8. Users can upload videos or use their webcam to detect objects instantly. The app annotates frames with bounding boxes, allows play and stop controls, and saves results as downloadable videos all in a modern, user-friendly interface.

## ✨ Features

- 🎥 **Video Upload & Webcam Support** – Upload video files (`.mp4`, `.avi`, `.mov`) or use your webcam for live detection.  
- ⚡ **Real-Time Object Detection** – Powered by YOLOv8 for fast and accurate results.  
- 🎨 **Neon-Styled Interface** – Clean, modern UI with custom styling for a better user experience.  
- ▶️ **Play & ⏹ Stop Controls** – Easily start or stop detection while viewing the video stream.  
- 💾 **Save & Download Output** – Processed video is saved as `output.avi` and can be downloaded directly from the app.  
- 📦 **Lightweight & Easy to Run** – Simple setup with `requirements.txt` and ready for deployment on Streamlit Cloud.

- ## 💻 Hardware & Model Compatibility

| Platform       | Recommended Model | GPU Support | Notes                           |
|----------------|-------------------|-------------|---------------------------------|
| CPU-only PC/Laptop | yolov8n.pt        | ❌          | Works fine (~10–15 FPS, lightweight) |
| Desktop w/ GPU | yolov8s.pt        | ✅ CUDA     | Best performance, smoother detection |
| Jetson Nano    | yolov8n.pt        | ✅ CUDA     | Can achieve near real-time performance |
| Raspberry Pi   | yolov8n (exported to NCNN) | ❌ CPU only  | Limited FPS, not ideal for heavy tasks |

> ⚡ Default model in this project: **`yolov8n.pt`** (fastest & most efficient for general use).  
Performance depends on hardware, model size, and video resolution.

## 👤 Author

Laiba Ahmed

🔗 Connect on LinkedIn
📅 Published Date: September 2025
