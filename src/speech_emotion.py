import speech_recognition as sr

def detect_speech_emotion():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Speak something")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)

        if "tired" in text or "stress" in text:
            return "Stressed"
        else:
            return "Neutral"

    except:
        return "Speech not recognized"
