import cv2
import numpy as np
import streamlit as st

logo_img  = cv2.imread("logo.png")
# st.header("AKROLITHOS SA")
st.image(logo_img, use_column_width='auto')
image = st.camera_input("Scan QR code")


def cross_check_name(qr_value):
    fixed_value = "Akrolithos_Gala_2023"
    if qr_value == fixed_value:
        return True


if image is not None:
    bytes_data = image.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
    gray_img = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray_img, 228, 255, 0)
    inv_bw_img = cv2.bitwise_not(thresh)
    inv_gray_img = cv2.bitwise_not(gray_img)

    detector = cv2.QRCodeDetector()
    # decoded_info, points, straight_qrcode = detector.detectAndDecodeMulti(cv2_img)

    data, bbox, straight_qrcode = detector.detectAndDecode(inv_gray_img)

    # st.write(data)

    if (cross_check_name(data)):
        st.success("PASS", )
    else:
        st.error("FAIL")

