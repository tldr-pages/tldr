# megatools-dl

> Descarga archivos de `mega.nz`.
> Parte del paquete de utilidades `megatools`.
> Más información: <https://megatools.megous.com/man/megatools-dl.html>.

- Descarga los archivos de un enlace 'mega.nz' al directorio actual:

`megatools-dl {{https://mega.nz/...}}`

- Descarga los archivos de un enlace 'mega.nz` a un directorio específico:

`megatools-dl --path {{ruta/al/directorio}} {{https://mega.nz/...}}`

- Permite elegir interactivamente qué archivos descargar:

`megatools-dl --choose-files {{https://mega.nz/...}}`

- Limita la velocidad de descarga en KiB/s:

`megatools-dl --limit-speed {{velocidad}} {{https://mega.nz/...}}`
