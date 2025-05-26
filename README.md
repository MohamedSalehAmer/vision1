# Logo Corner Detection and Size Comparison

This project uses OpenCV to compare two logos based on the smallest window size that detects a specific number of corners (78). It uses the Harris corner detector through OpenCV's `goodFeaturesToTrack` function.

## 🧠 Purpose

The goal is to determine which of two input logos is more **"detailed"** or **"complex"** in structure by finding the smallest `blockSize` (window size) needed to detect exactly 78 corners using Harris corner detection.

## 📦 Requirements

Make sure you have the following libraries installed:

```bash
pip install opencv-python numpy
```

For Google Colab users, no additional installation is required beyond standard packages. If you're running this locally and using `cv2.imshow` instead of Colab, replace `cv2_imshow` with `cv2.imshow`.

## 🖼️ Input

Place your two logo images in the correct paths:

- `/content/1.PNG`
- `/content/3.PNG`

Update the paths as needed if you're not using Google Colab.

## 🛠️ How It Works

1. Each image is converted to grayscale and processed using `cv2.goodFeaturesToTrack` with the Harris detector enabled.
2. A range of window sizes `[2, 4, 8, 16, 32, 64]` is tested.
3. The first window size that detects exactly **78** corners is selected as the effective detection window size for that image.
4. The two images are resized to the same height and displayed side by side.
5. Based on the relative window sizes:
   - If Image 1 requires a **smaller** window size than Image 2 to detect the same number of corners, it is considered **more complex (larger in detail)**.
   - Conversely, if it needs a **larger** window size, it is considered **less complex (smaller in detail)**.

## 📊 Output

- A side-by-side image with a text overlay comparing the two logos.
- A printed summary indicating:
  - The window size used for each image.
  - A conclusion about their relative sizes.

## 📎 Example Output

```
win_size: 2, detected corners: 53  
win_size: 4, detected corners: 70  
win_size: 8, detected corners: 78  
Window sizes: Image 1 = 8, Image 2 = 16  
Logo 1 is 2.00 times smaller than logo 2
```

## 📄 Notes

- The comparison logic is based on the assumption that a **smaller window size** indicates **finer detail**.
- The number of target corners (`NO_CORNERS = 78`) is customizable.

## 🔗 References

- [OpenCV Documentation – goodFeaturesToTrack](https://docs.opencv.org/4.x/d4/d8c/tutorial_py_shi_tomasi.html)
- [Harris Corner Detection](https://docs.opencv.org/4.x/dc/d0d/tutorial_py_features_harris.html)

---

Feel free to fork and modify this project as needed.
