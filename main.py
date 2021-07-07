import streamlit as st
from PIL import Image
import os
import numpy as np

st.title("Online Yolov5 Object Detection")

uploaded_file = st.file_uploader("Choose an image...", type="jpg")
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    st.write("Classifying...")
    image.save("image.jpg", format='JPEG', quality=75)
    result = os.system(f"python yolov5/detect.py --source image.jpg --save-txt")

    os.system("del image.jpg")
    num_detection = len(os.listdir("runs/detect"))

    if num_detection > 1:
        image = Image.open(f"runs/detect/exp{num_detection}/image.jpg")
        with open (f"runs/detect/exp{num_detection}/labels/image.txt", 'r') as f:
            line = f.readlines()
            class_num = []
            for i in range(len(line)):
                print(line[i])
                class_num.append(int(line[i].split(" ")[0]))
    else:
        image = Image.open("runs/detect/exp/image.jpg")
        with open ("runs/detect/exp/labels/image.txt", 'r') as f:
            class_num = f.read(2)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    st.write("Yolov5 Detection")

    
    for item in class_num:
        with open ("label.txt", 'r') as f:
            label = f.read().split(",")[item].replace("'", "")
            st.write(label)

