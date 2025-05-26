import cv2
import numpy as np
from google.colab.patches import cv2_imshow

NO_CORNERS = 78

def first_correct_winsize(I):
    """find the smallest win_size for which all corners are detected"""
    window_sizes = [2, 4, 8, 16, 32, 64]
    G = cv2.cvtColor(I, cv2.COLOR_BGR2GRAY)
    G = np.float32(G)
    
    for win_size in window_sizes:
        alpha = 0.04
        corners = cv2.goodFeaturesToTrack(
            G, 
            maxCorners=1000,  # زيادة العدد
            qualityLevel=0.005,  # تقليل العتبة
            minDistance=3,  # تقليل المسافة
            blockSize=win_size,
            useHarrisDetector=True,
            k=alpha
        )
        
        nc = len(corners) if corners is not None else 0
        print(f"win_size: {win_size}, detected corners: {nc}")
        
        if nc == NO_CORNERS:
            return win_size
    
    return 64

# Main code
I1 = cv2.imread('/content/1.PNG')
I2 = cv2.imread('/content/3.PNG')

if I1 is None or I2 is None:
    print("Error: Could not load images. Check the file paths.")
else:
    h1, w1 = I1.shape[:2]
    h2, w2 = I2.shape[:2]
    target_height = min(h1, h2)
    I1_resized = cv2.resize(I1, (int(w1 * target_height / h1), target_height))
    I2_resized = cv2.resize(I2, (int(w2 * target_height / h2), target_height))

    s1 = first_correct_winsize(I1)
    s2 = first_correct_winsize(I2)
    J = np.concatenate((I1_resized, I2_resized), 1)

    if s1 < s2:
        txt = f'Logo 1 is {s2/s1:.2f} times larger than logo 2'  # عكست المنطق
    elif s1 > s2:
        txt = f'Logo 1 is {s1/s2:.2f} times smaller than logo 2'  # عكست المنطق
    else:
        txt = 'Logo 1 is about the same size as logo 2'

    cv2.putText(J, txt, (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2_imshow(J)
    print(f"Window sizes: Image 1 = {s1}, Image 2 = {s2}")
    print(txt)
