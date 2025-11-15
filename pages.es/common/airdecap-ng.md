# airdecap-ng

> Descifra un archivo de captura cifrado (WEP, WPA o WPA2).
> Parte del paquete de software de red de Aircrack-ng.
> Más información: <https://www.aircrack-ng.org/doku.php?id=airdecap-ng>.

- Elimina encabezados inalámbricos de una red abierta de archivos de captura y utiliza los puntos de acceso con dirección MAC para filtrar:

`airdecap-ng -b {{ap_mac}} {{ruta/al/archivo_de_captura.cap}}`

- Descifra un archivo de captura [w]EP cifrado usando la clave en formato hexadecimal:

`airdecap-ng -w {{clave_hex}} {{ruta/al/archivo_de_captura.cap}}`

- Descifra un archivo de captura WPA/WPA2 cifrado usando los puntos de acceso [e]ssid y contraseña:

`airdecap-ng -e {{essid}} -p {{contraseña}} {{ruta/al/archivo_de_captura.cap}}`

- Descifra un archivo de captura WPA/WPA2 cifrado preservando los encabezados usando los puntos de acceso [e]ssid y contraseña:

`airdecap-ng -l -e {{essid}} -p {{contraseña}} {{ruta/al/archivo_de_captura.cap}}`

- Descifra un archivo de captura WPA/WPA2 cifrado usando los puntos de acceso [e]ssid y contraseña, así como su dirección MAC para filtrar:

`airdecap-ng -b {{ap_mac}} -e {{essid}} -p {{contraseña}} {{ruta/al/archivo_de_captura.cap}}`
