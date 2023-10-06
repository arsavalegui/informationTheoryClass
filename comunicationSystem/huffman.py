datagram = {
    "id": "1",
    "Player_skin": "spiderman",
    "Using_emote": "happy",
    "Player_glider": "blue" 
}

def string_a_binario(cadena):
    binario = ''.join(format(ord(char), '08b') for char in cadena)
    return binario
id_binario = string_a_binario(datagram["id"])
skin_binario = string_a_binario(datagram["Player_skin"])
emote_binario = string_a_binario(datagram["Using_emote"])
glider_binario = string_a_binario(datagram["Player_glider"])

datagrama_binario = id_binario + skin_binario + emote_binario + glider_binario

print("Datagrama en binario (todos los campos):")
print(datagrama_binario)
