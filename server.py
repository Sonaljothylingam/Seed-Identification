from flask import Flask, request, jsonify
import pickle
import numpy as np
from PIL import Image
import io
from flask_cors import CORS
from tensorflow.keras.models import load_model

model = load_model('model.h5')
print("Model loaded successfully")

app = Flask(__name__)
CORS(app)


def preprocess_image(image):
    img = Image.open(io.BytesIO(image))
    img = img.resize((160, 160))  # Resize the image to match the input size of your model
    img = np.array(img) / 255.0  # Normalize the pixel values
    return img

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'})

    image = request.files['image'].read()
    processed_image = preprocess_image(image)
    prediction = model.predict(np.expand_dims(processed_image, axis=0))
    print("heheheheh")
    print(prediction)
    class_name = ['Almond', 'Amla', 'Apple', 'Avocado', 'Betel_Nut', 'Black_Plum', 'Cashew', 'Chinese_Date', 'Date', 'Guava', 'Hog_Plum', 'Jackfruit', 'Litchi', 'Mango', 'Olive', 'Orange', 'Palm', 'Pumpkin', 'Sapodilla', 'Tamarind']  # Replace with your actual class names
    predicted_class_index = np.argmax(prediction)  # Get the index of the maximum probability
    predicted_class = class_name[predicted_class_index]
    return jsonify({'class': predicted_class})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)





