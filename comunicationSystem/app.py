import uuid
import time
import random
from collections import defaultdict, Counter
from morse import text_to_morse as tm, morse_to_text as mt, play_morse_sound as pms
from huffman import HuffmanCoding
from shanonfano import ShannonFanoCoding 
from api import requestRandomSkins, requestRandomEmote, requestRandomGlider


class WiFi:
    def __init__(self, password):
        self.password = password

    def transmitir(self, data):
        print(f"WiFi: Transmitiendo datagrama a través del router hacia el transmisor\n {data}")
        return data

    def recibir(self, data):
        print("WiFi: Recibiendo datagrama del servidor del juego...")
        return data

class Transmisor:
    def __init__(self, data):
        self.data = data

    def transmitir(self, binaryData):
        print("Transmisor: Enviando datagrama codificado al canal...")
        return binaryData

    def recibir(self, data):
        print(f"Transmisor: Recibiendo datagrama: {data}")
        return data

    def codificar(self, data, metodo):
        
        if metodo == "8bits":

            def string_a_binario(cadena):
                binario = ''.join(format(ord(char), '08b') for char in cadena)
                return binario

            binarios = [string_a_binario(data[key]) for key in data]
            datagrama_binario = ''.join(binarios)

            def agregar_longitud_prefijo(binario):
                longitud = len(binario) // 8
                return format(longitud, '016b') + binario

            binarios_con_prefijo = [agregar_longitud_prefijo(b) for b in binarios]
            datagrama_binario = ''.join(binarios_con_prefijo)

            print(f"Transmisor: Codificando datos... Datagrama en binario: {datagrama_binario}\n")
            return datagrama_binario, 0
        
        elif metodo == "huffman":
            huffman = HuffmanCoding()
            frequency = Counter(str(data))
            huffman.build_heap(frequency)
            huffman.merge_nodes()
            huffman.build_codes()
            
            encoded_data_dict = {}
            for key, value in data.items():
                encoded_data_dict[key] = huffman.encode(value)
            
            print(f"Transmisor: Codificando datos con Huffman... Datagrama codificado: {encoded_data_dict}\n")
            return encoded_data_dict, huffman
        
        elif metodo == "shannon_fano":
            sf = ShannonFanoCoding()
            data_string = str(data)

            encoded_data = sf.encode(data_string)
            
            print(f"Transmisor: Codificando datos con Shanon-fano... Datagrama codificado: {encoded_data}\n")

            return encoded_data, sf

        elif metodo == "morse":
            encoded_str = '_|_'.join([tm(key) + '|' + tm(value) for key, value in data.items()])
            print(f"Transmisor: Codificando datos con codigo morse... Datagrama codificado: {encoded_str}\n")

            pms(encoded_str)

            return encoded_str, 0
        
        else:
            print("No llegó la solicitud correctamente.")
            exit()
    
class Canal:
    def recibir(self, binaryData):
        print("Canal: Recibiendo datagrama codificado del transmisor...")
        return binaryData
    
    def enviar(self, binaryData):
        print("Canal: Enviando datagrama codificado a Nintendo Switch...")
        return binaryData

class ConsolaNintendoSwitchOLED:
    def __init__(self, nombre):
        self.nombre = nombre

    def recibir(self, binaryData):
        print(f"{self.nombre}: Recibiendo datagrama...")
        return binaryData

    def decodificar(self, binario, metodo, obj):

        if metodo == "8bits":
            data = {}
            keys = ['id', 'Player_skin', 'Using_emote', 'Player_glider']
            idx = 0

            def binario_a_string(binario):
                cadena = ''.join(chr(int(binario[i:i+8], 2)) for i in range(0, len(binario), 8))
                return cadena

            def extraer_con_prefijo(binario):
                longitud = int(binario[:16], 2) * 8
                return binario[16:16+longitud], binario[16+longitud:]

            while binario:
                segmento, binario = extraer_con_prefijo(binario)
                data[keys[idx]] = binario_a_string(segmento)
                idx += 1

            print(f"{self.nombre}: Decodificando datagrama... Datos: {data}\n")
            return data

        elif metodo == "huffman":
            huffman = obj
        
            decoded_data_dict = {}
            for key, value in binario.items():
                decoded_data_dict[key] = huffman.decode(value)
            
            print(f"{self.nombre}: Decodificando datos con Huffman... Datos: {decoded_data_dict}\n")
            return decoded_data_dict
        
        elif metodo == "shannon_fano":
            sf = obj

            decoded_data = sf.decode(binario)
            print(f"{self.nombre}: Decodificando datos con Shanon-Fano... Datos: {decoded_data}\n")

            return decoded_data
        
        elif metodo == "morse":
            decoded_data = {}
            for item in binario.split('_|_'):
                key, value = item.split('|')
                decoded_data[mt(key)] = mt(value)

            print(f"{self.nombre}: Decodificando datos con codigo morse... Datos: {decoded_data}\n")
            return decoded_data

def simulacion_transmision():

    def generar_datagrama():
        random_uuid = uuid.uuid4()
        uuid_str = str(random_uuid)

        return {
            "id": uuid_str,
            "Player_skin": requestRandomSkins(),
            "Using_emote": requestRandomEmote(),
            "Player_glider": requestRandomGlider() 
        }

    def simulacion_canales():
        PROBABILIDAD_RUIDO = 0.3
        canales = [i for i in range(1, 6)] #matriz de canales
        
        print("\n---------- Simulación de Canales ----------\n")
        canal_actual = 1
        
        while True:
            datagrama = generar_datagrama()

            if random.random() < PROBABILIDAD_RUIDO:
                print(f"Ruido detectado en el canal {canal_actual}.")
                canal_actual = random.choice([canal for canal in canales if canal != canal_actual])
                print(f"Reenviando datos al canal {canal_actual}.\n")

            print(f"Canal {canal_actual} transmitiendo datos: {datagrama}")
            time.sleep(2)

    print("Selecciona el método de codificación:")
    print("1. Codificación 8 bits")
    print("2. Codificación Huffman")
    print("3. Codificación Shannon-Fano")
    print("4. Codificación morse")
    print("5. Simulación de canales")
    opcion = input("Introduce el número de la opción deseada: ")

    if opcion == "1":
        metodo = "8bits"
    elif opcion == "2":
        metodo = "huffman"
    elif opcion == "3":
        metodo = "shannon_fano"
    elif opcion == "4":
        metodo = "morse"
    elif opcion == "5":
        simulacion_canales()
        return
    else:
        print("Opción no válida. Usando codificación normal (8 bits) por defecto.")
        metodo = "8bits"

    print("\n---------- Inicio de la Transmisión ----------\n")

    wifi = WiFi("mySecretPassword")
    data_wifi = wifi.transmitir(generar_datagrama())

    transmisor = Transmisor(data_wifi)
    data_codificada, obj = transmisor.codificar(data_wifi, metodo)
    datagram = transmisor.transmitir(data_codificada)

    canal = Canal()
    data_canal = canal.enviar(datagram)
    data_canal = canal.recibir(data_canal)

    consola = ConsolaNintendoSwitchOLED("Nintendo Switch OLED")
    data_nintendo = consola.recibir(data_canal)
    consola.decodificar(data_nintendo, metodo, obj)

    print("---------- Fin de la Transmisión ----------\n")

simulacion_transmision()