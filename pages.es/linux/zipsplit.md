# zipsplit

> Divide un archivo Zip dentro de archivos Zip más pequeños.
> Más información: <https://manned.org/zipsplit>.

- Divide un archivo Zip en partes no mayores a 36000 bytes (36 MB):

`zipsplit {{ruta/al/archivo.zip}}`

- Use un [n]úmero dado de bytes como limite parcial:

`zipsplit -n {{size}} {{ruta/al/archivo.zip}}`

- [p]ause entre la cración de cada parte:

`zipsplit -p -n {{size}} {{ruta/al/archivo.zip}}`

- De salida a los archivos Zip más pequeños en un directorio dado:

`zipsplit -b {{ruta/al/directorio_de_salida}} -n {{size}} {{ruta/al/archivo.zip}}`
