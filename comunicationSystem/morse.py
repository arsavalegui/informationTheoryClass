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

    '_': '..--.-' 
}

pygame.mixer.init()

dot_sound = pygame.mixer.Sound("morseSounds/dot.wav")
dash_sound = pygame.mixer.Sound("morseSounds/dash.wav")

def text_to_morse(text):
    morse = ''
    for char in text:
        if char.upper() in MORSE_CODE_DICT:  #caracter en diccionario ?
            morse += MORSE_CODE_DICT[char.upper()] + '_'
    return morse[:-1]  # quitar separador


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

# datagram = {'id': '7802dc9c-2c6e-4f2f-83de-940fb4346876', 'Player_skin': 'Mogul Master (GER)', 'Using_emote': 'Daydream', 'Player_glider': 'Touchdown'}

# encoded_str = '_|_'.join([text_to_morse(key) + '|' + text_to_morse(value) for key, value in datagram.items()])
# print("Codificado:", encoded_str)

# play_morse_sound(encoded_str)

# decoded_datagram = {}
# for item in encoded_str.split('_|_'):
#     key, value = item.split('|')
#     decoded_datagram[morse_to_text(key)] = morse_to_text(value)

# print("Decodificado:", decoded_datagram)
