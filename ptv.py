#Este codigo solo hace el texto plano en la terminal y debes colocar manualmente la ruta del archivo
# Instalación de las bibliotecas necesarias (ejecutar en una celda)
# !pip install SpeechRecognition pydub

import speech_recognition as sr
from pydub import AudioSegment
import os

def convertir_audio_a_texto(ruta_audio):
    """
    Convierte un archivo de audio de WhatsApp a texto
    
    Args:
        ruta_audio (str): Ruta al archivo de audio de WhatsApp (.opus o .ogg)
        
    Returns:
        str: Texto transcrito del audio
    """
    # Nombre del archivo temporal
    temp_wav = "temp_audio.wav"
    
    # Convertir de formato OGG/OPUS (WhatsApp) a WAV para mejor compatibilidad
    try:
        # WhatsApp normalmente usa .opus o .ogg
        audio = AudioSegment.from_file(ruta_audio, format=ruta_audio.split('.')[-1])
        audio.export(temp_wav, format="wav")
        print(f"Audio convertido temporalmente a WAV para procesamiento")
    except Exception as e:
        return f"Error al convertir el archivo: {str(e)}"
    
    # Inicializar el reconocedor
    reconocedor = sr.Recognizer()
    
    # Transcribir el audio
    try:
        with sr.AudioFile(temp_wav) as fuente_audio:
            # Ajustar para ruido ambiente (opcional)
            #reconocedor.adjust_for_ambient_noise(fuente_audio)
            
            # Capturar el audio
            datos_audio = reconocedor.record(fuente_audio)
            
            # Usar Google Speech Recognition (no requiere clave API para uso básico)
            texto = reconocedor.recognize_google(datos_audio, language="es-ES")
            
            print("Transcripción completada!")
            return texto
    except sr.UnknownValueError:
        return "No se pudo entender el audio"
    except sr.RequestError as e:
        return f"Error en el servicio de reconocimiento: {str(e)}"
    finally:
        # Eliminar archivo temporal
        if os.path.exists(temp_wav):
            os.remove(temp_wav)

# Ejemplo de uso
# Reemplaza 'ruta/al/audio_whatsapp.opus' con la ruta de tu archivo
ruta_archivo = 'xxxxxxxxxxxxx'
texto_transcrito = convertir_audio_a_texto(ruta_archivo)
print("Texto transcrito:")
print(texto_transcrito)