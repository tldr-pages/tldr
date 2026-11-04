# mkswap

> Configura un área de intercambio de Linux en un dispositivo o en un archivo.
> Nota: `ruta/al/archivo` puede apuntar a un archivo normal o a una partición de intercambio.
> Más información: <https://manned.org/mkswap>.

- Configura un área de intercambio determinada:

`sudo mkswap {{ruta/al/archivo}}`

- Busca bloques defectuosos en una partición antes de crear el área de intercambio:

`sudo mkswap {{[-c|--check]}} {{ruta/al/archivo}}`

- Especifica una etiqueta para la partición (para que `swapon` pueda usar la etiqueta):

`sudo mkswap {{[-L|--label]}} {{etiqueta}} {{/dev/sdXY}}`

- Usa el UUID especificado:

`sudo mkswap {{[-U|--uuid]}} {{clear|random|time|valor_uuid}}`

- Configura un archivo de intercambio (para btrfs, vea `tldr btrfs filesystem` en su lugar):

`sudo mkswap {{[-s|--size]}} {{tamaño_del_archivo}} {{[-F|--file]}} {{ruta/al/archivo_de_intercambio}}`
