import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input

# Load trained model
model = tf.keras.models.load_model("flower_classifier.h5")

# Class names (MUST match training)
class_names = ['daisy', 'dandelion', 'roses', 'sunflowers', 'tulips']

# App title
st.title("🌼 AI Flower Classifier")
st.write("Upload a flower image and I will tell you its type!")

# Image uploader
uploaded = st.file_uploader("Upload a flower image", type=["jpg", "jpeg", "png"])

if uploaded:
    img = Image.open(uploaded).convert("RGB")
    st.image(img, caption="Uploaded Image", use_container_width=True)

    # Resize
    img = img.resize((224,224))
    img_array = np.array(img)

    # Preprocess
    img_array = preprocess_input(img_array)
    img_array = np.expand_dims(img_array, axis=0)

    # Predict
    prediction = model.predict(img_array)
    index = np.argmax(prediction)
    confidence = prediction[0][index] * 100

    # Show result
    st.subheader("🌸 Prediction")
    st.write("Flower Type:", class_names[index])
    st.write("Confidence:", f"{confidence:.2f}%")
