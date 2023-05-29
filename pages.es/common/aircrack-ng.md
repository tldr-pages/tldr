# aircrack-ng

> Crackea claves WEP y WPA/WPA2 desde handshake en paquetes capturados.
> Parte de la suite de software de red Aircrack-ng.
> Más información: <https://www.aircrack-ng.org/doku.php?id=aircrack-ng>.

- Crackea la clave desde el archivo de captura usando [w]ordlist:

`aircrack-ng -w {{ruta/al/lista.txt}} {{ruta/al/captura.cap}}`

- Descifra la clave del archivo de captura utilizando [w]ordlist y el [e]ssid del punto de acceso:

`aircrack-ng -w {{ruta/al/lista.txt}} -e {{essid}} {{ruta/al/captura.cap}}`

- Descifra la clave del archivo de captura utilizando [w]ordlist y la dirección MAC del punto de acceso:

`aircrack-ng -w {{ruta/al/lista.txt}} --bssid {{mac}} {{ruta/al/captura.cap}}`
