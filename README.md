# flower-ai-app

# 🌸 AI Flower Classifier (Deep Learning Project)

This project is an **AI-based Flower Classification App** built using Deep Learning and Transfer Learning.

The application identifies the type of flower from an uploaded image using a trained neural network model.

---

## 🚀 Features

The model can classify flowers into the following categories:

- Daisy  
- Dandelion  
- Roses  
- Sunflowers  
- Tulips  

For each image, the app returns:
- Flower name
- Confidence score

---

## 🧠 How It Works

1. A pre-trained model (**MobileNetV2**) is used (Transfer Learning).
2. The model is retrained on a flower dataset.
3. The network learns:
   - colors
   - shapes
   - edges
   - textures
4. Streamlit provides a simple web interface for predictions.

---

## 🏗️ Tech Stack

- Python  
- TensorFlow / Keras  
- CNN (Convolutional Neural Network)  
- Transfer Learning  
- Streamlit  
- GitHub  

---

## 📂 Project Structure

| File | Purpose |
|------|--------|
| `app.py` | Frontend / UI |
| `flower_train.py` | Model training script |
| `requirements.txt` | Required libraries |

---
