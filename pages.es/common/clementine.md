# clementine

> Un moderno reproductor de música y organizador de bibliotecas.
> Ver también: `audacious`, `qmmp`, `cmus`, `mpv`.
> Más información: <https://manned.org/clementine>.

- Inicia la GUI o la trae al frente:

`clementine`

- Inicia la reproducción de música:

`clementine {{URL|ruta/a/música.ext}}`

- Alterna entre pausa y reproducción:

`clementine {{[-t|--play-pause]}}`

- Interrumpe la reproducción:

`clementine {{[-s|--stop]}}`

- Salta a la pista siguiente o anterior:

`clementine --{{next|previous}}`

- Crea una nueva lista de reproducción con uno o varios archivos de música o URLs:

`clementine {{[-c|--create]}} {{URL1|ruta/a/música1.ext URL2|ruta/a/música2.ext ...}}`

- Carga un archivo de lista de reproducción:

`clementine {{[-l|--load]}} {{ruta/para/playlist.ext}}`

- Reproduce una pista concreta de la lista de reproducción cargada:

`clementine {{[-k|--play-track]}} {{5}}`
