import struct


#Clases del sistema

class routerWifi:
    def __init__(self, data, velocidad):
        self.data = data

    def transmitir(self, data, velocidad):
        print("Enviando datos")
        #return dato

    def codificar(self, data):
        print("codificar")
        
    
    def transmitir(self, dato):
        print("Router recibio datagrama")
        #return dato


class nintendoSwitch:
    def __init__(self, data):
        self.data = data
    
    def decodificar(self, data):
        print("decodificar")
    

class canal:
    def __init__(self, data, velocidad):
        print("Canal")
    

#Datagrama
datagramDict = {
    "id": 12891,
    "Inventory":{
        "Slot1": "Mammoth Pistol",
        "Slot2": "Sharp Tooth Shotgun",
        "Slot3": "Submachine Gun",
        "Slot4": "Shockwave Grenade",
        "Slot5": "Slurp Juice"
    },
    "Coords": (256.7, 72.3, -128.5)
}

velocidadRouter = 100

# Codificar el datagrama en binario
id_value = datagramDict["id"]
inventory_slot1 = datagramDict["Inventory"]["Slot1"].encode("utf-8")
inventory_slot2 = datagramDict["Inventory"]["Slot2"].encode("utf-8")
inventory_slot3 = datagramDict["Inventory"]["Slot3"].encode("utf-8")
inventory_slot4 = datagramDict["Inventory"]["Slot4"].encode("utf-8")
inventory_slot5 = datagramDict["Inventory"]["Slot5"].encode("utf-8")
coords = datagramDict["Coords"]

binary_data = struct.pack(f"i5s17s20s17s20s3f", id_value, inventory_slot1, inventory_slot2,
                           inventory_slot3, inventory_slot4, inventory_slot5,
                           coords[0], coords[1], coords[2])

# Imprimir la representación en binario
print(binary_data)

