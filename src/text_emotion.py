from textblob import TextBlob

def detect_text_emotion(text):

    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity

    if polarity > 0.3:
        emotion = "Happy"
    elif polarity < -0.3:
        emotion = "Stressed"
    else:
        emotion = "Neutral"

    return emotion
