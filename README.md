# flower-ai-app
🌸 AI Flower Classifier Using Deep Learning

This project is an AI-based Flower Classification App built using Deep Learning and Transfer Learning.

It can identify the type of flower from an uploaded image using a trained neural network model.

🚀 What this project does

The app can classify flower images into the following categories:

🌼 Daisy

🌻 Dandelion

🌹 Roses

🌻 Sunflowers

🌷 Tulips

You upload a photo, and the model predicts:
✅ Flower name
✅ Confidence score

🧠 How it works (Simple Explanation)

A pretrained AI model (MobileNetV2) is used (Transfer Learning).

The model is retrained using a flower dataset from TensorFlow.

The AI learns patterns like:

color

shape

petals

edges

texture

A web app (Streamlit) is used to show predictions on a user interface.

🏗️ Technologies Used

Python 🐍

TensorFlow / Keras

Transfer Learning

CNN (Convolutional Neural Network)

Streamlit (Web UI)

GitHub (Version Control)

📂 Project Files
File	Purpose
app.py	Runs the web interface
flower_train.py	Trains the AI model
flower_classifier.h5	The trained AI model
requirements.txt	Required libraries
▶️ How to Run
1. Install dependencies
pip install -r requirements.txt

2. Run the app
streamlit run app.py

🎯 Purpose of this project

This project is built for:

Learning AI and Deep Learning

Understanding Transfer Learning

Prakticing Deployment with Streamlit

Building real-world ML experience

It is not a production-level app but a learning project for growth.
