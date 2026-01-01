import speech_recognition as sr
from gtts import gTTS
import os

def speak(text):
    print("Bot: " + text)
    tts = gTTS(text=text, lang='ur')
    tts.save("reply.mp3")
    os.system("mpv reply.mp3")

def start_bot():
    speak("Salam Zidan, main taiyar hoon. Hukam dein")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Sun raha hoon...")
        audio = r.listen(source)
        try:
            cmd = r.recognize_google(audio, language='ur-PK')
            print("Aapne kaha: " + cmd)
            if "Facebook" in cmd or "فیس بک" in cmd:
                speak("Theek hai, Facebook automation shuru kar raha hoon")
            else:
                speak("Main ne suna: " + cmd)
        except:
            speak("Maaf karna, samajh nahi aaya")

if __name__ == "__main__":
    start_bot()
