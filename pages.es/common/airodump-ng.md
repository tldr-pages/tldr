# airodump-ng

> Captura paquetes y muestra información sobre redes inalámbricas.
> Parte de `aircrack-ng`.
> Más información: <https://www.aircrack-ng.org/doku.php?id=airodump-ng>.

- Captura paquetes y muestra información sobre red(es) inalámbricas en la banda de 2.4GHz:

`sudo airodump-ng {{interface}}`

- Captura paquetes y muestra información sobre red(es) inalámbrica(s) en la banda de 5GHz:

`sudo airodump-ng {{interface}} --band a`

- Captura paquetes y muestra información sobre rede(s) inalámbrica(s) en las bandas 2.4GHz y 5GHz:

`sudo airodump-ng {{interface}} --band abg`

- Captura paquetes y muestra información sobre una red inalámbrica dada la dirección MAC y canal, y guarda la salida en un archivo:

`sudo airodump-ng --channel {{canal}} --write {{ruta/al/archivo}} --bssid {{mac}} {{interfaz}}`
