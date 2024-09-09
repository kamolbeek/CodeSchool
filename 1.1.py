import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import os

def speak(text):
    tts = gTTS(text=text, lang='ru')
    tts.save("response.mp3")
    playsound("response.mp3")
    os.remove("response.mp3")

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Gapiring...")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language="uz-UZ")
            print(f"Siz aytdingiz: {text}")
            return text.lower()
        except sr.UnknownValueError:
            print("Kechirasiz, ovozingizni tanib bo'lmadi.")
            return ""
        except sr.RequestError:
            print("Xatolik yuz berdi!")
            return ""

def chatbot_response(user_input):
    if 'qalay' in user_input or 'qandaysan' in user_input:
        return "Yaxshi, siz qalaysiz?"
    elif 'isming nima' in user_input:
        return "Men Kamoliddinning botiman"
    elif 'rahmat' in user_input:
        return "Arzimaydi!"
    elif 'andijondan' in user_input:
        return 'Andijon va Qoraqalpogʻiston o‘rtasidagi masofa taxminan 900-950 kilometrni tashkil qiladi.'
    elif 'xayr' in user_input or 'exit' in user_input:
        return "Xayr, keyingi safar ko'rishguncha!"
    else:
        return "Afsus, bu savolga javobim yo'q."

if __name__ == "__main__":
    speak("Salom! Men bilan gaplashishingiz mumkin.")
    while True:
        user_input = listen()
        if user_input:
            response = chatbot_response(user_input)
            speak(response)
        if 'xayr' in user_input or 'exit' in user_input:
            break