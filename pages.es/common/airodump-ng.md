# airmon-ng

> Activar el modo monitor en dispositivos de red inalámbricos.
> Forma parte de `aircrack-ng`.
> Más información: <https://www.aircrack-ng.org/doku.php?id=airmon-ng>.

- Lista de dispositivos inalámbricos y sus respectivos estados:

`sudo airmon-ng`

- Activar el modo monitor para un dispositivo específico:

`sudo airmon-ng start {{wlan0}}`

- Elimina los procesos molestos que utilizan dispositivos inalámbricos:

`sudo airmon-ng check kill`

- Desactiva el modo monitor para una interfaz de red específica:

`sudo airmon-ng stop {{wlan0mon}}`
