# informationTheoryClass
Repositorio para llevar control y almacenamiento de los proyectos/tareas de la calse de Teoria de la información

Estructura del sistema de comunicacón:

El sistema simulará el envio de datagramas en video juegos online usando UDP, en concreto fortnite.

- Fuente de información:
    Se usará la representación de un datagrama que incluirá un identificador de jugador, su posicion en coordenadas (x,y,z), inventario de armas y salud.

- Transmisor:
    Se usará un medio wifi por protocolo UDP. Concretamente con el wifi 802.11ax o wifi 6.
    Se usará python para representar el datagrama y comprimirlo de tal forma que pueda ser enviado por el canal en formato binario.
 
- Canal 
    El canal será el wifi 6, con una velocidad de 100mbps
    El ruido a usar será el de velocidad y el de modificación de datos para simular el lag.

- Receptor
    El receptor será una nintendo switch oled.

- Decodificador
    En esta parte se decodificará el datagrama para poder visualizar los datos en el juego, y poder presenciar el lag.