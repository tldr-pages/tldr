# rkdeveloptool

> Flashea, vacía y gestiona el firmware de arranque en dispositivos informáticos basados en Rockchip.
> Necesitará encender el dispositivo en modo Maskrom/Bootrom antes de conectarlo a través del USB.
> Algunos subcomandos pueden requerir ser ejecutados como root.
> Más información: <https://github.com/rockchip-linux/rkdeveloptool>.

- [l]ista todos los [d]ispositivos flash conectados basados en Rockchip:

`rkdeveloptool ld`

- Inicializa el dispositivo forzándolo a [d]escargar e instalar el [b]ootloader desde el archivo especificado:

`rkdeveloptool db {{ruta/al/bootloader.bin}}`

- Actualiza el software del boot[l]oader de arranque con uno nuevo:

`rkdeveloptool ul {{ruta/al/bootloader.bin}}`

- Escribe una imagen en una partición flash con formato GPT, especificando el sector de almacenamiento inicial (normalmente `0x0` alias `0`):

`rkdeveloptool wl {{sector_inicial}} {{ruta/a/imagen.img}}`

- Escribe en la partición flash por su nombre amigable:

`rkdeveloptool wlx {{nombre_partición}} {{ruta/a/imagen.img}}`

- [r]einicia/repone el [d]ispositivo, sale del modo Maskrom/Bootrom para arrancar en la partición flash seleccionada:

`rkdeveloptool rd`
