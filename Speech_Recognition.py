#pip install SpeechRecognition
#pip install pyttsx3
#pip install pyaudio
#pip install setuptools

import speech_recognition as sr

r = sr.Recognizer()

def grabacion_texto():
    with sr.Microphone() as mic:
        print("Háblale al micrófono...")
        r.adjust_for_ambient_noise(mic)
        audio = r.listen(mic)

        try:
            texto = r.recognize_google(audio, language='es-ES')
            if texto == "140":
                raise SystemExit
            return texto
        except sr.UnknownValueError:
            print("No se pudo entender el audio.")
        except sr.RequestError as e:
            print(f"Error en la solicitud: {e}")

def guardar_texto(texto):
    with open("Audio_a_Texto.txt", "a") as f:
        f.write(texto + "\n")

while True:
    texto = grabacion_texto()
    if texto:
        print(f"Texto reconocido: {texto}")
        guardar_texto(texto)
    else:
        print("Inténtalo de nuevo.")
