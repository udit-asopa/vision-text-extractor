import numpy as np
import tempfile
import os
import cv2

from langchain_core.tools import tool


@tool
def preprocess_image(
        img_path: str,
        op: str = "threshold",
        target_width: int = 1600) -> str:
    img = cv2.imread(img_path)
    if img is None:
        raise ValueError(f"Could not read image at {img_path}")

    # Upscale small images to help OCR
    if target_width is not None and img.shape[1] < target_width:
        scale = target_width / img.shape[1]
        img = cv2.resize(img, None, fx = scale, fy = scale, interpolation = cv2.INTER_CUBIC)

    if op == "threshold":
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Gentle denoise and local binarisation to sharpen text
        gray = cv2.bilateralFilter(gray, 7, 50, 50)
        out = cv2.adaptiveThreshold(gray,
                                    255,
                                    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                    cv2.THRESH_BINARY,
                                    31,
                                    10)

    elif op == "deskew":
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = cv2.bitwise_not(gray)
        # Otsu to find text pixels
        _, bw = cv2.threshold(gray,
                              0,
                              255,
                              cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        coords = np.column_stack(np.where(bw > 0))
        angle = 0.0
        if coords.size > 0:
            rect = cv2.minAreaRect(coords)
            angle = rect[-1]
            # Convert OpenCV's angle convention to a proper rotation
            if angle < -45:
                angle = -(90 + angle)
            else:
                angle = -angle
        # Rotate around centre
        (h, w) = img.shape[:2]
        M = cv2.getRotationMatrix2D((w // 2, h // 2), angle, 1.0)
        out = cv2.warpAffine(img, M, (w, h), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)

    # Ensure 3-channel PNG for the vision model (it accepts grayscale too, but PNG-3 is universal)
    if out.ndim == 2:
        out = cv2.cvtColor(out, cv2.COLOR_GRAY2BGR)

    # Write to a temporary PNG and return its path
    tmpdir = tempfile.gettempdir()
    base = os.path.splitext(os.path.basename(img_path))[0]
    out_path = os.path.join(tmpdir, f"{base}_proc_{op}.png")
    cv2.imwrite(out_path, out)
    return out_path