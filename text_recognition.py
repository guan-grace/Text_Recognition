import streamlit as st
import easyocr

reader = easyocr.Reader(['en'])

img_file_buffer = st.camera_input("Take a picture of some text")

if img_file_buffer is not None:
    bytes_data = img_file_buffer.getvalue()
    results = reader.readtext(bytes_data, detail=1, paragraph=False)
    for (bbox, text, confidence) in results:
        st.write(f'Text: {text}, Confidence: {confidence:.2f}')
