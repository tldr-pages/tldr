# crackle

> Crackea y descifra el cifrado Bluetooth Low Energy (BLE).
> Más información: <https://github.com/mikeryan/crackle>.

- Comprueba si las comunicaciones BLE grabadas contienen los paquetes necesarios para recuperar claves temporales (TKs):

`crackle -i {{ruta/a/entrada.pcap}}`

- Utiliza la fuerza bruta para recuperar la TK de los eventos de emparejamiento registrados y la utiliza para descifrar todas las comunicaciones posteriores:

`crackle -i {{ruta/a/entrada.pcap}} -o {{ruta/a/desencriptado.pcap}}`

- Utiliza la clave a largo plazo (LTK) especificada para descifrar la comunicación grabada:

`crackle -i {{ruta/a/entrada.pcap}} -o {{ruta/a/descifrar.pcap}} -l {{81b06facd90fe7a6e9bbd9cee59736a7}}`
