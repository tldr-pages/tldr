# nvram

> Manipula variables del firmware.
> Más información: <https://ss64.com/osx/nvram.html>.

- Im[p]rime todas las variables almacenadas en la NVRAM:

`nvram -p`

- Im[p]rime todas las variables almacenadas en la NVRAM usando el formato [x]ML:

`nvram -xp`

- Modifica el valor de una variable del firmware:

`sudo nvram {{nombre}}="{{valor}}"`

- Elimina una variable de firmware:

`sudo nvram -d {{nombre}}`

- [c]larifica todas las variables de firmware:

`sudo nvram -c`

- Establece una variable de firmware de un [x]ML [f]ile específico:

`sudo nvram -xf {{ruta/al/archivo.xml}}`
