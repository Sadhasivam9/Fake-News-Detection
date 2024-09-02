from flask import Flask, request, render_template
import joblib
import os
from sklearn.feature_extraction.text import TfidfVectorizer

# Initialize the Flask app
app = Flask(__name__)

# Load the trained model and vectorizer
model = joblib.load('fake_news_model.pkl')
vectorizer = joblib.load('tfidf_vectorizer.pkl')  # Save and load the vectorizer the same way

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        title = request.form['title']
        text = request.form['text']

        # Combine title and text for prediction (as done during training)
        combined_input = title + " " + text
        input_features = vectorizer.transform([combined_input])

        prediction = model.predict(input_features)
        result = 'REAL' if prediction[0] == 'REAL' else 'FAKE'

        return render_template('index.html', prediction_text=f'This news is {result}')
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)

