import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report


class EmotionModel:

    def __init__(self):
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.model = LogisticRegression()

    # Load dataset
    def load_data(self, path):

        data = pd.read_csv(path)

        X = data['text_message']
        y = data['emotion_label']

        return X, y

    # Train model
    def train(self, X, y):

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )

        X_train_vec = self.vectorizer.fit_transform(X_train)
        X_test_vec = self.vectorizer.transform(X_test)

        self.model.fit(X_train_vec, y_train)

        predictions = self.model.predict(X_test_vec)

        print("Model Performance:")
        print(classification_report(y_test, predictions))

    # Predict emotion
    def predict_emotion(self, text):

        text_vec = self.vectorizer.transform([text])
        prediction = self.model.predict(text_vec)

        return prediction[0]

    # Save model
    def save_model(self):

        pickle.dump(self.model, open("models/emotion_classifier.pkl", "wb"))
        pickle.dump(self.vectorizer, open("models/vectorizer.pkl", "wb"))

        print("Model saved successfully!")

    # Load model
    def load_model(self):

        self.model = pickle.load(open("models/emotion_classifier.pkl", "rb"))
        self.vectorizer = pickle.load(open("models/vectorizer.pkl", "rb"))

        print("Model loaded successfully!")
