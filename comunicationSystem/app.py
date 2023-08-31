import struct
import random
from api import requestRandomSkins, requestRandomEmote, requestRandomGlider

class WiFi:
    def __init__(self, password):
        self.password = password
    
    def transmitir(self, data):
        print(f"Transmitiendo datagrama: {data} a través del router hacia el transmisor\n")
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

        print(f"Datagrama codificado: {packed_data}\n")
        return packed_data

class Canal:
    def __init__(self, binaryData):
        # self.datagramas = []
        self.binaryData = binaryData
    
    def enviar(self):
        # self.datagramas.append(binaryData)
        print(f"Canal enviando datagrama codificado a destino...\n")

    def recibir(self):
        print(f"Canal recibiendo el datagrama codificado: {binaryData}\n")

    def ruido(self, binaryData, probabilidad):
        # print(binaryData)
        print("Ha habido una perdida de datos\n")

        new_data = bytearray(binaryData)
        for i in range(len(new_data)):
            if random.random() < probabilidad:
                new_data[i] = random.randint(0, 255)
        return bytes(new_data)



class ConsolaNintendoSwitchOLED:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def recibir(self, binaryData):
        print(f"{self.nombre} recibiendo datagrama: {binaryData}\n")
    
    def decodificar(self, new_data, binaryData):
        print(f"{self.nombre} decodificando datagrama: {new_data}\n")

        if(new_data == binaryData):

            formato = "32s 32s 32s 32s"

            unpacked_data = struct.unpack(formato, new_data)

            decoded_dict = {
                "id": unpacked_data[0].decode().strip('\x00'),
                "Player_skin": unpacked_data[1].decode().strip('\x00'),
                "Using_emote": unpacked_data[2].decode().strip('\x00'),
                "Player_glider": unpacked_data[3].decode().strip('\x00')
            }

            print(f"Los datos llegaron de manera correcta. {decoded_dict}")

        else:
            print(f"Los datos llegaron con ruido. {new_data}")

routerTplink = WiFi(123)
consola = ConsolaNintendoSwitchOLED("Nintendo switch de Alan")

numrand = str(random.randint(100, 999))

datagram = {
    "id": numrand,
    "Player_skin": requestRandomSkins(),
    "Using_emote": requestRandomEmote(),
    "Player_glider": requestRandomGlider() 
}
# print(datagram)

routerTplink.recibir(datagram)
originalDatagram = routerTplink.transmitir(datagram)
transmisor = Transmisor(originalDatagram)
transmisor.recibir(originalDatagram)
binaryData = transmisor.codificar(originalDatagram)
canal = Canal(binaryData)
canal.recibir()
new_data = canal.ruido(binaryData, 0.2)
canal.enviar()
consola.recibir(new_data)
consola.decodificar(new_data,binaryData)
# canal.recibir(enviar_datagrama)