import struct

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

    def codificar(self, data):
        def string_a_binario(cadena):
            binario = ''.join(format(ord(char), '08b') for char in cadena)
            return binario

        def agregar_longitud_prefijo(binario):
            # Suponemos un prefijo de 16 bits
            longitud = len(binario) // 8
            return format(longitud, '016b') + binario

        binarios = [string_a_binario(data[key]) for key in data]
        binarios_con_prefijo = [agregar_longitud_prefijo(b) for b in binarios]

        datagrama_binario = ''.join(binarios_con_prefijo)

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
    
    def decodificar(self, binario):
        data = {}
        keys = ['id', 'Player_skin', 'Using_emote', 'Player_glider']
        idx = 0

        def binario_a_string(binario):
            """Convierte una cadena binaria a una cadena de texto"""
            cadena = ''.join(chr(int(binario[i:i+8], 2)) for i in range(0, len(binario), 8))
            return cadena

        for key in keys:
            # Leemos la longitud del prefijo (16 bits en este ejemplo)
            longitud = int(binario[idx:idx+16], 2)
            idx += 16  # Avanzamos el índice

            # Leemos los datos basándonos en la longitud
            campo = binario[idx:idx + longitud * 8]
            idx += longitud * 8  # Avanzamos el índice

            # Convertimos el binario a cadena y guardamos en el diccionario
            data[key] = binario_a_string(campo)

        print(f"{self.nombre}: Datos decodificados: {data}\n")
        return data

def simulacion_transmision():
    datagrama = {
        "id": "1",
        "Player_skin": "spiderman",
        "Using_emote": "happy",
        "Player_glider": "blue"
    }

    wifi = WiFi(123)
    data_wifi = wifi.recibir(datagrama)
    data_transmisor = wifi.transmitir(data_wifi)

    transmisor = Transmisor(data_transmisor)
    data_transmisor = transmisor.recibir(data_transmisor)
    data_codificada = transmisor.codificar(data_transmisor)
    data_canal = transmisor.transmitir(data_codificada)

    canal = Canal()
    data_canal = canal.recibir(data_canal)
    data_nintendo = canal.enviar(data_canal)

    consola = ConsolaNintendoSwitchOLED("Nintendo Switch")
    data_nintendo = consola.recibir(data_nintendo)
    consola.decodificar(data_nintendo)

simulacion_transmision()
