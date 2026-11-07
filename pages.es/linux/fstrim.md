# fstrim

> Descarta los bloques no usados de un sistema de archivos montado.
> Solo es compatible con dispositivos de memoria flash como SSD y tarjetas microSD.
> Más información: <https://manned.org/fstrim>.

- Recorta los bloques no usados en todas las particiones montadas que lo admiten:

`sudo fstrim {{[-a|--all]}}`

- Recorta los bloques no usados en una partición especificada:

`sudo fstrim {{/}}`

- Muestra estadísticas después del recorte:

`sudo fstrim {{[-v|--verbose]}} {{/}}`
