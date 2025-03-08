# Este codigo te pide el audio luego de ejecutarse y tambien te da la opcion de guardarlo en un archivo comun de texto o en word, para lo cual es necesario bajar las biblioteca python-doc
# Instalación de las bibliotecas necesarias (ejecutar primero si no están instaladas)
# !pip install SpeechRecognition pydub python-doc

import speech_recognition as sr
from pydub import AudioSegment
import os
from datetime import datetime

def convertir_audio_a_texto(ruta_audio):
    """
    Convierte un archivo de audio de WhatsApp a texto
    
    Args:
        ruta_audio (str): Ruta al archivo de audio de WhatsApp (.opus o .ogg)
        
    Returns:
        str: Texto transcrito del audio
    """
    if not os.path.exists(ruta_audio):
        return f"Error: El archivo {ruta_audio} no existe"
    
    print(f"Procesando archivo: {ruta_audio}")
    
    # Nombre del archivo temporal
    temp_wav = "temp_audio.wav"
    
    # Convertir de formato OGG/OPUS (WhatsApp) a WAV para mejor compatibilidad
    try:
        # Intentar detectar el formato por extensión
        formato = ruta_audio.split('.')[-1].lower()
        audio = AudioSegment.from_file(ruta_audio, format=formato)
        audio.export(temp_wav, format="wav")
        print(f"Audio convertido temporalmente a WAV para procesamiento")
    except Exception as e:
        return f"Error al convertir el archivo: {str(e)}"
    
    # Inicializar el reconocedor
    reconocedor = sr.Recognizer()
    
    # Transcribir el audio
    try:
        with sr.AudioFile(temp_wav) as fuente_audio:
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

def guardar_transcripcion(texto, ruta_archivo, formato="txt"):
    """
    Guarda la transcripción en un archivo de texto
    
    Args:
        texto (str): Texto a guardar
        ruta_archivo (str): Ruta donde guardar el archivo
        formato (str): Formato del archivo ('txt' o 'docx')
    """
    try:
        if formato == "docx":
            # Para guardar como Word necesitamos la biblioteca python-docx
            try:
                from docx import Document
                doc = Document()
                doc.add_paragraph(texto)
                doc.save(ruta_archivo)
                print(f"Transcripción guardada como documento Word en: {ruta_archivo}")
            except ImportError:
                nueva_ruta = ruta_archivo.replace(".docx", ".txt")
                print("La biblioteca 'python-docx' no está instalada. Guardando como texto plano...")
                with open(nueva_ruta, "w", encoding="utf-8") as archivo:
                    archivo.write(texto)
                print(f"Transcripción guardada como texto en: {nueva_ruta}")
        else:
            with open(ruta_archivo, "w", encoding="utf-8") as archivo:
                archivo.write(texto)
            print(f"Transcripción guardada como texto en: {ruta_archivo}")
        
        return True
    except Exception as e:
        print(f"Error al guardar el archivo: {str(e)}")
        return False

def main():
    """Función principal que ejecuta todo el proceso"""
    print("=== CONVERSOR DE AUDIO DE WHATSAPP A TEXTO ===")
    
    # Solicitar ruta del archivo
    ruta_archivo = input("Ingresa la ruta completa del archivo de audio (puedes arrastrar el archivo aquí): ").strip()
    # Eliminar comillas si el usuario arrastró el archivo
    ruta_archivo = ruta_archivo.strip("'\"")
    
    if not ruta_archivo:
        print("No se proporcionó ninguna ruta. Programa terminado.")
        return
    
    # Convertir audio a texto
    print(f"Convirtiendo el archivo: {ruta_archivo}")
    texto_transcrito = convertir_audio_a_texto(ruta_archivo)
    
    # Mostrar resultado
    print("\n=== TRANSCRIPCIÓN ===")
    print(texto_transcrito)
    print("=====================")
    
    # Preguntar si desea guardar
    guardar = input("\n¿Deseas guardar la transcripción? (s/n): ").lower().strip()
    
    if guardar == 's' or guardar == 'si' or guardar == 'sí':
        # Preguntar formato para guardar
        print("\n¿En qué formato deseas guardar la transcripción?")
        print("1. Texto plano (.txt)")
        print("2. Documento Word (.docx) - Requiere 'python-docx'")
        
        try:
            opcion = int(input("Ingresa el número de opción (1-2): "))
            if opcion < 1 or opcion > 2:
                opcion = 1  # Por defecto, texto plano
        except:
            opcion = 1  # Por defecto, texto plano
        
        formato_elegido = "txt" if opcion == 1 else "docx"
        
        # Si el usuario elige Word, verificar si tiene python-docx
        if formato_elegido == "docx":
            try:
                import docx
            except ImportError:
                print("\nLa biblioteca 'python-docx' no está instalada.")
                print("Para instalarla, ejecuta: pip install python-docx")
                print("Guardando como texto plano en su lugar.")
                formato_elegido = "txt"
        
        # Generar un nombre de archivo predeterminado
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        nombre_archivo = f"transcripcion_{timestamp}.{formato_elegido}"
        
        # Solicitar ruta de guardado
        ruta_guardar = input(f"Ingresa la ruta donde guardar el archivo (deja en blanco para usar '{nombre_archivo}' en el directorio actual): ").strip()
        
        # Si no se proporciona ruta, usar el directorio actual
        if not ruta_guardar:
            ruta_guardar = os.path.join(os.getcwd(), nombre_archivo)
        else:
            # Eliminar comillas si el usuario arrastró una carpeta
            ruta_guardar = ruta_guardar.strip("'\"")
            # Si la ruta es un directorio, agregar el nombre del archivo
            if os.path.isdir(ruta_guardar):
                ruta_guardar = os.path.join(ruta_guardar, nombre_archivo)
            # Si la ruta no tiene extensión, agregar la extensión correcta
            if not os.path.splitext(ruta_guardar)[1]:
                ruta_guardar = f"{ruta_guardar}.{formato_elegido}"
        
        guardar_transcripcion(texto_transcrito, ruta_guardar, formato_elegido)
    
    print("\nProceso completado. ¡Gracias por usar el conversor!")

# Ejecutar el programa
if __name__ == "__main__":
    main()