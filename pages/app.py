import streamlit as st
import numpy as np
import cv2 as cv
import os
from io import BytesIO
import tensorflow as tf
from PIL import Image
from tensorflow.keras.layers import *
from tensorflow.keras.models import *

st.title("Klasifikasi Kue Tradisional")

from tensorflow.keras.applications import ResNet50

###Input Image
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    #st.write("nama file yang diupload = ", uploaded_file.name)
    #ini untuk nampilin gambar, outputnya bytes
    bytes_image = uploaded_file.read() #baca image

    #nampilin gambar
    image = Image.open(BytesIO(bytes_image))
    st.image(image, caption='Data Testing')

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

    # nama_kue = {
    #     0: 'Kue Dadar Gulung',
    #     1: 'Kastengel',
    #     2: 'Kue Klepon',
    #     3: 'Kue Lapis',
    #     4: 'Kue Lumpur',
    #     5: 'Kue Putri Salju',
    #     6: 'Kue Risoles',
    #     7: 'Kue Serabi'
    # }
    # st.write(nama_kue)
    # st.write(output)

    hasil = np.argmax(result)
    # st.text(hasil)

    if hasil==0:
        st.text("Kue Dadar Gulung")
    elif hasil==1:
        st.text("Kue Kastengel")
    elif hasil==2:
        st.text("Kue Klepon")
    elif hasil==3:
        st.text("Kue Lapis")
    elif hasil==4:
        st.text("Kue Lumpur")
    elif hasil==5:
        st.text("Kue Putri Salju")
    elif hasil==6:
        st.text("Kue Risoles")
    else:
        st.text("Kue Serabi")