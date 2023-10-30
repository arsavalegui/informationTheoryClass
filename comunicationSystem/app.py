import heapq
import struct
import uuid
from api import requestRandomSkins, requestRandomEmote, requestRandomGlider

#-----------------------------
#---------- HUFFMAN ----------
#-----------------------------

class NodoHuffman:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def construir_arbol_huffman(cadena):
    if not cadena:
        return None

    frecuencias = {}
    for char in cadena:
        if char not in frecuencias:
            frecuencias[char] = 0
        frecuencias[char] += 1

    heap = [NodoHuffman(char, freq) for char, freq in frecuencias.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        nodo_combinado = NodoHuffman(None, left.freq + right.freq)
        nodo_combinado.left = left
        nodo_combinado.right = right

        heapq.heappush(heap, nodo_combinado)

    return heap[0]

def huffman_codificar(nodo, prefijo_binario="", codigo={}):
    if not nodo:
        return codigo

    if nodo.char:
        codigo[nodo.char] = prefijo_binario
        return codigo

    huffman_codificar(nodo.left, prefijo_binario + "0", codigo)
    huffman_codificar(nodo.right, prefijo_binario + "1", codigo)

    return codigo

def huffman_decodificar(nodo, codigo_binario):
    result = []
    current_nodo = nodo
    for bit in codigo_binario:
        if bit == "0":
            current_nodo = current_nodo.left
        else:
            current_nodo = current_nodo.right

        if current_nodo.char:
            result.append(current_nodo.char)
            current_nodo = nodo

    return "".join(result)

#-----------------------------
#------- Shannon-Fano --------
#-----------------------------

def construir_shannon_fano(cadena):
    frecuencias = {}
    for char in cadena:
        if char not in frecuencias:
            frecuencias[char] = 0
        frecuencias[char] += 1

    # Ordena los símbolos basados en frecuencia
    ordenados = sorted(frecuencias.items(), key=lambda x: x[1], reverse=True)

    def recursive_shannon_fano(symbols, codebook={}):
        n = len(symbols)
        if n == 1:
            symbol, _ = symbols[0]
            return {symbol: '0'}

        total = sum([freq for _, freq in symbols])
        half = total / 2
        split_idx = 0
        current_sum = 0

        for idx, (_, freq) in enumerate(symbols):
            if current_sum > half:
                break
            current_sum += freq
            split_idx = idx

        for idx in range(split_idx + 1):
            symbol, _ = symbols[idx]
            codebook[symbol] = '0' + codebook.get(symbol, '')

        for idx in range(split_idx + 1, n):
            symbol, _ = symbols[idx]
            codebook[symbol] = '1' + codebook.get(symbol, '')

        # Llamada recursiva
        recursive_shannon_fano(symbols[:split_idx+1], codebook)
        recursive_shannon_fano(symbols[split_idx+1:], codebook)

        return codebook

    return recursive_shannon_fano(ordenados)

def shannon_fano_codificar(cadena, codebook):
    return ''.join([codebook[char] for char in cadena])

def shannon_fano_decodificar(cadena_binaria, codebook):
    reverse_codebook = {v: k for k, v in codebook.items()}
    decoded = []
    buffer = ''
    for bit in cadena_binaria:
        buffer += bit
        if buffer in reverse_codebook:
            decoded.append(reverse_codebook[buffer])
            buffer = ''
    return ''.join(decoded)

#-----------------------------
#---------- 8 BITS -----------
#-----------------------------

class WiFi:
    def __init__(self, password):
        self.password = password

    def transmitir(self, data):
        print("WiFi: Transmitiendo datagrama a través del router hacia el transmisor\n")
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

    def codificar(self, data, metodo="8bits"):
        def string_a_binario(cadena):
            binario = ''.join(format(ord(char), '08b') for char in cadena)
            return binario

        def agregar_longitud_prefijo(binario):
            longitud = len(binario) // 8
            return format(longitud, '016b') + binario

        binarios = [string_a_binario(data[key]) for key in data]
        binarios_con_prefijo = [agregar_longitud_prefijo(b) for b in binarios]
        datagrama_binario = ''.join(binarios_con_prefijo)

        if metodo == "huffman":
            arbol = construir_arbol_huffman(datagrama_binario)
            codigo_huffman = huffman_codificar(arbol)
            datagrama_binario = ''.join([codigo_huffman[char] for char in datagrama_binario])

        print(f"Transmisor: Codificando datos... Datagrama en binario: {datagrama_binario}\n")
        return datagrama_binario

class Canal:
    def enviar(self, binaryData):
        print("Canal: Enviando datagrama codificado a Nintendo Switch...")
        return binaryData

    def recibir(self, binaryData):
        print("Canal: Recibiendo datagrama codificado del transmisor...")
        return binaryData

class ConsolaNintendoSwitchOLED:
    def __init__(self, nombre):
        self.nombre = nombre

    def recibir(self, binaryData):
        print(f"{self.nombre}: Recibiendo datagrama...")
        return binaryData

    def decodificar(self, binario, metodo="8bits"):
        data = {}
        keys = ['id', 'Player_skin', 'Using_emote', 'Player_glider']
        idx = 0

        def binario_a_string(binario):
            cadena = ''.join(chr(int(binario[i:i+8], 2)) for i in range(0, len(binario), 8))
            return cadena

        def extraer_con_prefijo(binario):
            longitud = int(binario[:16], 2) * 8
            return binario[16:16+longitud], binario[16+longitud:]

        if metodo == "huffman":
            arbol = construir_arbol_huffman(binario)
            binario = huffman_decodificar(arbol, binario)

        while binario:
            segmento, binario = extraer_con_prefijo(binario)
            data[keys[idx]] = binario_a_string(segmento)
            idx += 1

        print(f"{self.nombre}: Decodificando datagrama... Datos: {data}\n")
        return data

def simulacion_transmision():
    print("Selecciona el método de codificación:")
    print("1. Codificación normal (8 bits)")
    print("2. Codificación Huffman")
    print("3. Codificación Shannon-Fano")
    opcion = input("Introduce el número de la opción deseada: ")

    if opcion == "1":
        metodo = "8bits"
    elif opcion == "2":
        metodo = "huffman"
    elif opcion == "3":
        metodo = "shannon_fano"
    else:
        print("Opción no válida. Usando codificación normal (8 bits) por defecto.")
        metodo = "8bits"

    random_uuid = uuid.uuid4()
    uuid_str = str(random_uuid)

    datagram = {
        "id": uuid_str,
        "Player_skin": requestRandomSkins(),
        "Using_emote": requestRandomEmote(),
        "Player_glider": requestRandomGlider() 
    }

    print("\n---------- Inicio de la Transmisión ----------\n")

    wifi = WiFi("mySecretPassword")
    data_wifi = wifi.transmitir(datagram)

    transmisor = Transmisor(data_wifi)
    data_codificada = transmisor.codificar(datagram, metodo)
    datagram = transmisor.transmitir(data_codificada)

    canal = Canal()
    data_canal = canal.enviar(datagram)
    data_canal = canal.recibir(data_canal)

    consola = ConsolaNintendoSwitchOLED("Nintendo Switch OLED")
    data_nintendo = consola.recibir(data_canal)
    consola.decodificar(data_nintendo, metodo)

    print("---------- Fin de la Transmisión ----------\n")

simulacion_transmision()