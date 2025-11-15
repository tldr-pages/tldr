# aireplay-ng

> Inyecta paquetes en una red inalámbrica.
> Parte de `aircrack-ng`.
> Más información: <https://www.aircrack-ng.org/doku.php?id=aireplay-ng>.

- Envía una cantidad específica de paquetes disociados dada la dirección MAC de un punto de acceso, la dirección MAC de un cliente y una interfaz:

`sudo aireplay-ng --deauth {{cantidad}} --bssid {{mac_punto_acceso}} --dmac {{mac_cliente}} {{interfaz}}`
