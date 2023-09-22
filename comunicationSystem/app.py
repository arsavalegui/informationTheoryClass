import struct
import random
import math
from api import requestRandomSkins, requestRandomEmote, requestRandomGlider

class WiFi:
    def __init__(self, password):
        self.password = password
    
    def transmitir(self, data):
        print(f"Transmitiendo datagrama a través del router hacia el transmisor\n")
        return data
    
    def recibir(self, data):
        print(f"Router recibiendo datagrama: {data}\n")
        return data
    
class Transmisor:
    def __init__(self, data):
        self.data = data

    def transmitir(self, data):
        print(f"Transmitiendo el datagrama: {data} a través del transmisor\n")
    
    def recibir(self, data):
        print(f"Transmisor recibiendo los datos: {data}\n")

    def codificar(self, data):
        print(f"Codificando datos: {data}\n")
        formato = "32s 32s 32s 32s"

        #valores en binario
        packed_data = struct.pack(formato, str(data["id"]).encode(), 
                                  data["Player_skin"].encode(), 
                                  data["Using_emote"].encode(),
                                    data["Player_glider"].encode())

        binary_str = ''.join(format(byte, '08b') for byte in packed_data)
        print(f"Datagrama codificado: {binary_str}\n")

        return packed_data

class Canal:
    def __init__(self, binaryData):
        # self.datagramas = []
        self.binaryData = binaryData
    
    def enviar(self):
        # self.datagramas.append(binaryData)
        print(f"Canal enviando datagrama codificado a destino...\n")

    def recibir(self):
        print(f"Canal recibiendo el datagrama codificado...\n")

    def ruido(self, binaryData, probabilidad):
        # print(binaryData)
        print("\n")

        new_data = bytearray(binaryData)
        for i in range(len(new_data)):
            a = random.random() 

            umbral = [0.2, 0.4, 0.7, 0.9]

            if probabilidad in umbral:
                new_data[i] = random.randint(0, 255)
        return bytes(new_data)



class ConsolaNintendoSwitchOLED:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def recibir(self, binaryData):
        print(f"{self.nombre} recibiendo datagrama...\n")
    
    def decodificar(self, new_data, binaryData):
        print(f"{self.nombre} decodificando datagrama...\n")

        if(new_data == binaryData):

            formato = "32s 32s 32s 32s"

            unpacked_data = struct.unpack(formato, new_data)

            decoded_dict = {
                "id": unpacked_data[0].decode().strip('\x00'),
                "Player_skin": unpacked_data[1].decode().strip('\x00'),
                "Using_emote": unpacked_data[2].decode().strip('\x00'),
                "Player_glider": unpacked_data[3].decode().strip('\x00')
            }

            print(f"Los datos llegaron de manera correcta. {decoded_dict}\n\n")
            return 1

        else:
            decoded_data = new_data.decode('utf-8', 'ignore')
            print(f"Los datos llegaron con ruido. {decoded_data}\n\n")

            return 0

routerTplink = WiFi(123)
consola = ConsolaNintendoSwitchOLED("Nintendo switch de Alan")

def datagramas(values):

    numrand = str(random.randint(100, 999))

    randParameter = random.choice(values)

    datagram = {
        "id": numrand,
        "Player_skin": requestRandomSkins(),
        "Using_emote": requestRandomEmote(),
        "Player_glider": requestRandomGlider() 
    }

    routerTplink.recibir(datagram)
    originalDatagram = routerTplink.transmitir(datagram)
    transmisor = Transmisor(originalDatagram)
    transmisor.recibir(originalDatagram)
    binaryData = transmisor.codificar(originalDatagram)
    canal = Canal(binaryData)
    canal.recibir()
    new_data = canal.ruido(binaryData, randParameter)
    canal.enviar()
    consola.recibir(new_data)
    evento = consola.decodificar(new_data,binaryData)
    return evento

r = 0
sr = 0

values = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.8, 0.9]

total = len(values)

for i in range(0,total):
    evento = datagramas(values)
    if(evento == 1):
        sr = sr + 1
    else:
        r = r + 1

print("Sin ruido", sr, "Con ruido", r)

proba = 1/total

entropia = - proba * math.log2(proba)

entropia_total = entropia*r

print("Entropía: ", entropia_total)
