# ipscan

> Un rápido escáner de red diseñado para ser simple de usar.
> También conocido como Angry IP Scanner.
> Más información: <https://angryip.org/>.

- Escanea una dirección IP específica:

`ipscan {{192.168.0.1}}`

- Escanea un rango de direcciones IP:

`ipscan {{192.168.0.1-254}}`

- Escanea un rango de direcciones IP y guardar los resultados en un archivo:

`ipscan {{192.168.0.1-254}} -o {{ruta/a/salida.txt}}`

- Escanea IPs con un conjunto específico de puertos:

`ipscan {{192.168.0.1-254}} -p {{80,443,22}}`

- Escanea con un retardo entre peticiones para evitar la congestión de la red:

`ipscan {{192.168.0.1-254}} -d {{200}}`

- Muestra ayuda:

`ipscan --help`
