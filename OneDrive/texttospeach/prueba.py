import pyttsx3

# Inicializar el motor de texto a voz
engine = pyttsx3.init()

# Configurar propiedades de la voz (opcional)
engine.setProperty('rate', 150)  # Velocidad del habla
engine.setProperty('volume', 1.0)  # Volumen máximo

# Texto a traducir a voz (ejemplo de un gesto interpretado como "Hola")
texto_traducido = "Hola, ¿cómo estás?"

# Reproducir la traducción en audio
engine.say(texto_traducido)
engine.runAndWait()