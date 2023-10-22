# airodump-ng

> Captura paquetes y muestra información sobre redes inalámbricas.
> Parte de `aircrack-ng`.
> Más información: <https://www.aircrack-ng.org/doku.php?id=airodump-ng>.

- Captura paquetes y muestra información sobre una red inalámbrica:

`sudo airodump-ng {{interface}}`

- Captura paquetes y muestra información sobre una red inalámbrica dada la dirección MAC y canal, y guarda la salida en un archivo:

`sudo airodump-ng --channel {{canal}} --write {{ruta/al/archivo}} --bssid {{mac}} {{interfaz}}`
