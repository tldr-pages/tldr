# aircrack-ng

> Crackea claves WEP y WPA/WPA2 a partir de handshake en paquetes capturados.
> Parte de la suite de software de red Aircrack-ng.
> Más información: <https://www.aircrack-ng.org/doku.php?id=aircrack-ng>.

- Crackea la clave desde el archivo de captura usando un listado:

`aircrack-ng -w {{ruta/a/listado.txt}} {{ruta/a/captura.cap}}`

- Crackea la clave usando múltiples hilos de CPU desde el archivo de captura usando una lista:

`aircrack-ng -p {{número}} -w {{ruta/a/listado.txt}} {{ruta/a/captura.cap}}`

- Descifra la clave del archivo de captura utilizando un listado y el [e]ssid del punto de acceso:

`aircrack-ng -w {{ruta/a/listado.txt}} -e {{essid}} {{ruta/a/captura.cap}}`

- Descifra la clave del archivo de captura utilizando una listado y la dirección MAC del punto de acceso:

`aircrack-ng -w {{ruta/a/listado.txt}} --bssid {{mac}} {{ruta/a/captura.cap}}`
