#pip install SpeechRecognition
#pip install pyttsx3
#pip install pyaudio
#pip install setuptools

import speech_recognition as sr

r = sr.Recognizer()

def grabacion_texto():
    with sr.Microphone() as mic: 
        print("Hablale al microfono...")
        r.adjust_for_ambient_noise(mic)
        audio = r.listen(mic) #el sonido de mic que escucha lo guarda en audio

        try:
            texto = r.recognize_google(audio, language='es-ES') #Se utiliza Google para reconocer el audio hacia texto
            if texto == "140": #si se dice el numero 140 el programa se detiene
                raise SystemExit
            return texto
        except sr.UnknownValueError: #En caso de no entender el audio el programa lanzara un error 
            print("No se pudo entender el audio.")
        except sr.RequestError as e: #en caso de tener problema 
            print(f"Error en la solicitud: {e}")

def guardar_texto(texto): #definicion que permite guardar el texto en un archivo .txt
    with open("Audio_a_Texto.txt", "a") as f: 
        f.write(texto + "\n")

while True: #mientra se grabe, se procedera a pedir que el usuario hable, si no se escucha o entiende nada, se procedera a imprimir "Intentalo de nuevo"
    texto = grabacion_texto()
    if texto:
        print(f"Texto reconocido: {texto}")
        guardar_texto(texto)
    else:
        print("Intentalo de nuevo.")
