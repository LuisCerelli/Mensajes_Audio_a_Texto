
# Proyecto de Conversión de Audio de WhatsApp a Texto

Este proyecto consta de dos scripts en Python para convertir archivos de audio de WhatsApp (en formato `.opus` o `.ogg`) a texto. Utiliza el servicio de Google Speech Recognition para transcribir los audios. Además, el segundo script ofrece la opción de guardar la transcripción en un archivo de texto o en un documento Word.

## Requisitos

Antes de ejecutar los scripts, asegúrate de tener instaladas las siguientes bibliotecas:

```bash
pip install SpeechRecognition pydub python-docx
```

- **SpeechRecognition**: Para el reconocimiento de voz y la transcripción de audio a texto.
- **pydub**: Para convertir archivos de audio a formato compatible.
- **python-docx**: Para guardar la transcripción en un archivo Word (opcional).

## Scripts

### 1. `ptv.py`

Este script toma un archivo de audio de WhatsApp (en formato `.opus` o `.ogg`), lo convierte a `.wav` para un mejor procesamiento y luego utiliza Google Speech Recognition para transcribir el audio a texto. El script imprime el texto transcrito en la terminal.

#### Uso

1. Ejecuta el script.
2. Introduce la ruta completa del archivo de audio cuando se te pida (puedes arrastrar el archivo a la terminal).
3. El texto transcrito se mostrará en la terminal.

#### Ejemplo de uso:

```python
ruta_archivo = 'ruta/al/archivo/audio.ogg'
texto_transcrito = convertir_audio_a_texto(ruta_archivo)
print("Texto transcrito:")
print(texto_transcrito)
```

---

### 2. `ptv3.py`

Este script es similar al anterior, pero con la opción de guardar la transcripción en un archivo de texto plano o en un documento Word. También solicita la ruta del archivo de audio y te permite elegir en qué formato guardar la transcripción.

#### Uso

1. Ejecuta el script.
2. Introduce la ruta completa del archivo de audio.
3. El texto transcrito se mostrará en la terminal.
4. Se te preguntará si deseas guardar la transcripción. Si la respuesta es sí, te permitirá elegir entre guardar el archivo en formato `.txt` o `.docx`.
5. La transcripción se guardará en el formato elegido en la ubicación que elijas.

#### Ejemplo de uso:

```python
# El script pedirá la ruta del archivo de audio y luego la opción para guardar la transcripción.
```

---

## Funciones principales

### `convertir_audio_a_texto(ruta_audio)`

Convierte el audio de WhatsApp a texto utilizando Google Speech Recognition.

**Argumentos**:
- `ruta_audio`: Ruta al archivo de audio (debe ser `.opus` o `.ogg`).

**Retorna**:
- Texto transcrito o un mensaje de error.

### `guardar_transcripcion(texto, ruta_archivo, formato="txt")`

Guarda la transcripción en un archivo de texto.

**Argumentos**:
- `texto`: Texto que se va a guardar.
- `ruta_archivo`: Ruta donde se guardará el archivo.
- `formato`: El formato en el que se guardará el archivo (`txt` o `docx`).

---

## Notas

- **Guardar en Word**: Para guardar como un archivo Word, debes tener instalada la biblioteca `python-docx`. Si no está instalada, el script guardará el archivo como texto plano.
  
- **Recomendación de uso**: Este proyecto está diseñado para convertir audios de WhatsApp, que comúnmente están en formato `.ogg` o `.opus`. Si el audio tiene otro formato, podría no funcionar correctamente.

---

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.
