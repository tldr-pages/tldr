# zipsplit

> Divide un archivo Zip en archivos Zip más pequeños.
> Más información: <https://manned.org/zipsplit>.

- Divide un archivo Zip en partes no mayores a 36000 bytes (36 MB):

`zipsplit {{ruta/al/archivo.zip}}`

- Usa un [n]úmero dado de bytes como límite parcial:

`zipsplit -n {{size}} {{ruta/al/archivo.zip}}`

- [p]ausa entre la creación de cada parte:

`zipsplit -p -n {{size}} {{ruta/al/archivo.zip}}`

- Da salida a los archivos Zip más pequeños en un directorio dado:

`zipsplit -b {{ruta/al/directorio_de_salida}} -n {{size}} {{ruta/al/archivo.zip}}`
