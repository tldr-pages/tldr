# clamav

> Antivirus de código abierto.
> Diseñado especialment para escanear correos electrónicos, pero puede ser usado en otros contextos.
> Más información: <https://www.clamav.net>.

- Actualiza definiciones de virus:

`freshclam`

- Escanea un archivo en busca de virus:

`clamscan {{ruta/al/archivo}}`

- Escanea directorios recursivamente y mostrar los archivos infectados:

`clamscan --recursive --infected {{ruta/al/directorio}}`

- Escanea directorios recursivamente y poner los archivos infectados en cuarentena:

`clamscan --recursive --move={{directorio}}`
