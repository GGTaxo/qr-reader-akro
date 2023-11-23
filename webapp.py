import cv2
import numpy as np
import streamlit as st

image = st.camera_input("Scan QR code")

def cross_check_name(qr_value):
    fixed_value = "Akrolithos_Gala_2023"
    if qr_value == fixed_value:
        return True



if image is not None:
    bytes_data = image.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)

    detector = cv2.QRCodeDetector()

    data, bbox, straight_qrcode = detector.detectAndDecode(cv2_img)

    # st.write(data)

    if (cross_check_name(data)):
        st.info("PASS")
    else:
        st.info("FAIL")



