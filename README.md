# hangmanproject
import random

# Lista de palabras para el juego
palabras = ["python", "computadora", "codigo", "juego", "programa"]
palabra_secreta = random.choice(palabras)

# Guardamos las letras adivinadas y los intentos
letras_adivinadas = []
intentos_restantes = 6

print("¡Bienvenido al juego del Ahorcado!")
