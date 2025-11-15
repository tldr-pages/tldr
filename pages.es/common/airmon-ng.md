# airmon-ng

> Activa el modo monitor en dispositivos de red inalámbricos.
> Parte de `aircrack-ng`.
> Más información: <https://www.aircrack-ng.org/doku.php?id=airmon-ng>.

- Lista dispositivos inalámbricos y sus estados:

`sudo airmon-ng`

- Activa el modo monitor para un dispositivo específico:

`sudo airmon-ng start {{wlan0}}`

- Elimina los procesos perturbadores que utilizan dispositivos inalámbricos:

`sudo airmon-ng check kill`

- Desactiva el modo monitor para una interfaz de red específica:

`sudo airmon-ng stop {{wlan0mon}}`
