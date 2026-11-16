# swapoff

> Desactiva dispositivos y archivos para intercambio.
> Nota: `ruta/al/archivo` puede apuntar a un archivo normal o a una partición de intercambio.
> Más información: <https://manned.org/swapoff.8>.

- Desactiva un área de intercambio determinada:

`sudo swapoff {{ruta/al/archivo}}`

- Desactiva todas las áreas de intercambio en `/proc/swaps`:

`sudo swapoff {{[-a|--all]}}`

- Desactiva una partición de intercambio por su etiqueta:

`sudo swapoff -L {{etiqueta}}`
