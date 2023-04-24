import streamlit as st
import numpy as np
import cv2 as cv
import os
from io import BytesIO
import tensorflow as tf
from PIL import Image
from tensorflow.keras.layers import *
from tensorflow.keras.models import *

# import streamlit.components.v1 as com

page_bg_img = """
<style>
# [data-testid="stAppViewContainer"]{
#   background: linear-gradient(to bottom right, #deaaff, #c0fdff);
# }

[data-testid="stHeader"]{
  background-color: #F97728;
}

[data-testid="stSidebar"]{
  background-color: #FFCEA5;
}

# [data-testid="stHorizontalBlock"]{
#   background-color: #fff;
# }
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)
st.markdown("<h5 style='font-family:sans-serif; text-align:center; margin-bottom:0;'>INDONESIA TRADITIONAL CAKES</h5>", unsafe_allow_html=True)
st.markdown("<h2 style='font-family:sans-serif; text-align:center; margin:0; padding-top:0;'>Upload Your Picture</h2>", unsafe_allow_html=True)
  
from tensorflow.keras.applications import ResNet50

###Input Image
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    #st.write("nama file yang diupload = ", uploaded_file.name)
    #ini untuk nampilin gambar, outputnya bytes
    bytes_image = uploaded_file.read() #baca image

    #nampilin gambar
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write(" ")
    with col2:
        image = Image.open(BytesIO(bytes_image))
        st.image(image.resize((300,300)))
    with col3:
        st.write(" ")

    image_np = np.asarray(image)
    #Assuming your model expects Input shape (None, 64, 64, 1), biar input sesuai sama inputan awal. Kalo ndak sesuai nanti error
    resized_image = cv.resize(image_np, (200,200))
    resized_image = np.expand_dims(resized_image, axis=-1) #add a new dimension
    resized_image = np.expand_dims(resized_image, axis=0)

    # Loading ResNet50 model
    base_resnet_model = ResNet50(include_top=False,
                    input_shape=(200,200,3),
                    pooling='max',classes=8,
                    weights='imagenet')

    base_resnet_model.trainable = False

    # Transfer learning ResNet50
    resnet_model = tf.keras.models.Sequential([
        base_resnet_model,
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(64, activation="relu"),
        tf.keras.layers.Dense(64, activation="relu"),
        tf.keras.layers.Dense(8, activation="softmax")
    ])
    resnet_model.load_weights("ResNet50.h5")

    #Proses
    result = resnet_model.predict(resized_image)
    # output = np.rint(result)

    hasil = np.argmax(result)
    # st.text(hasil)

    if hasil==0:
        st.markdown("<h5 style='font-family:sans-serif; text-align:center; margin-bottom:0;'>Kue Dadar Gulung</h5>", unsafe_allow_html=True)
    elif hasil==1:
        st.markdown("<h5 style='font-family:sans-serif; text-align:center; margin-bottom:0;'>Kue Kastengel</h5>", unsafe_allow_html=True)
    elif hasil==2:
        st.markdown("<h5 style='font-family:sans-serif; text-align:center; margin-bottom:0;'>Kue Klepon</h5>", unsafe_allow_html=True)
    elif hasil==3:
        st.markdown("<h5 style='font-family:sans-serif; text-align:center; margin-bottom:0;'>Kue Lapis</h5>", unsafe_allow_html=True)
    elif hasil==4:
        st.markdown("<h5 style='font-family:sans-serif; text-align:center; margin-bottom:0;'>Kue Lumpur</h5>", unsafe_allow_html=True)
    elif hasil==5:
        st.markdown("<h5 style='font-family:sans-serif; text-align:center; margin-bottom:0;'>Kue Putri Salju</h5>", unsafe_allow_html=True)
    elif hasil==6:
        st.markdown("<h5 style='font-family:sans-serif; text-align:center; margin-bottom:0;'>Kue Risoles</h5>", unsafe_allow_html=True)
    else:
        st.markdown("<h5 style='font-family:sans-serif; text-align:center; margin-bottom:0;'>Kue Serabi</h5>", unsafe_allow_html=True)