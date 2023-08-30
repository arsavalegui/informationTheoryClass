class WiFi:
    def __init__(self, password):
        self.password = password
    
    def transmitir(self, datagram):
        print(f"Transmitiendo datagrama: {datagram} a través del router")
        return datagram
    
    def recibir(self, datagram):
        print(f"Router recibiendo datagrama: {datagram}")
        return datagram

class Canal:
    def __init__(self):
        self.datagramas = []
    
    def enviar(self, datagram):
        self.datagramas.append(datagram)
        print(f"Datagrama enviado al canal: {datagram}")

    def recibir(self):
        datagram = self.datagramas.pop(0)
        print(f"Datagrama recibido del canal: {datagram}")
        return datagram

class ConsolaNintendoSwitchOLED:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def recibir(self, datagram):
        print(f"{self.nombre} recibiendo datagrama: {datagram}")
    
    def decodificar(self, datagram):
        print(f"{self.nombre} decodificando datagrama: {datagram}")
        return datagram

router_wifi = WiFi(password="123")
canal = Canal()
nintendo_switch = ConsolaNintendoSwitchOLED(nombre="Nintendo Switch OLED")

datagrama = "Datagrammm"
datagram_enviado = router_wifi.transmitir(datagrama)
canal.enviar(datagram_enviado)
datagram_recibido = canal.recibir()
datagram_decodificado = nintendo_switch.decodificar(datagram_recibido)
nintendo_switch.recibir(datagram_decodificado)

