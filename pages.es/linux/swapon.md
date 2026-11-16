# swapon

> Activa dispositivos y archivos para intercambio.
> Nota: `ruta/al/archivo` puede apuntar a un archivo normal o a una partición de intercambio.
> Más información: <https://manned.org/swapon.8>.

- Muestra información sobre intercambio:

`swapon`

- Activa un área de intercambio determinada:

`sudo swapon {{ruta/al/archivo}}`

- Activa todas las áreas de intercambio indicadas en `/etc/fstab` excepto las que tienen la opción `noauto`:

`sudo swapon {{[-a|--all]}}`

- Activa una partición de intercambio por su etiqueta:

`sudo swapon -L {{etiqueta}}`
