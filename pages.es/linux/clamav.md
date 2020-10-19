# clamav

> Antivirus de código abierto.
> Diseñado especialment para escanear correos electrónicos, pero puede ser usado en otros contextos.
> Más información: <https://www.clamav.net>.

- Actualizar definiciones de virus:

`freshclam`

- Escanear un archivo en busca de virus:

`clamscan {{ruta/al/archivo}}`

- Escanear directorios recursivamente y mostrar los archivos infectados:

`clamscan --recursive --infected {{ruta/al/directorio}}`

- Escanear directorios recursivamente y poner los archivos infectados en quarentena:

`clamscan --recursive --move={{directorio}}`
