# hexyl

> Un simple visor hexadecimal para la terminal. Utiliza salida coloreada para distinguir diferentes categorías de bytes.
> Más información: <https://github.com/sharkdp/hexyl>.

- Imprime la representación hexadecimal de un archivo:

`hexyl {{ruta/al/archivo}}`

- Imprime la representación hexadecimal de los primeros `n` bytes de un archivo:

`hexyl -n {{n}} {{ruta/al/archivo}}`

- Imprime los bytes 512 a 1024 de un archivo:

`hexyl -r {{512}}:{{1024}} {{ruta/al/archivo}}`

- Imprime 512 bytes empezando por el byte 1024:

`hexyl -r {{1024}}:+{{512}} {{ruta/al/archivo}}`
