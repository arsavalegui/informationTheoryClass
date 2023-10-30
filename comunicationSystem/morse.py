import time
import pygame

MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',

    '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.',

    ' ': '/', '.': '.-.-.-', ',': '--..--', '-': '-....-',

    '_': '..--.-' #separador
}

pygame.mixer.init()

dot_sound = pygame.mixer.Sound("morseSounds/dot.wav")
dash_sound = pygame.mixer.Sound("morseSounds/dash.wav")

def text_to_morse(text):
    morse = ''
    for char in text:
        morse += MORSE_CODE_DICT[char.upper()] + '_'
    return morse[:-1] #quitar separador

def morse_to_text(morse):
    text = ''
    for code in morse.split('_'):
        text += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(code)]
    return text

def play_morse_sound(morse):
    for char in morse:
        if char == '.':
            dot_sound.play()
            time.sleep(0.3)
        elif char == '-':
            dash_sound.play()
            time.sleep(0.7)
        elif char == '_':
            time.sleep(1) #pausa de letras

