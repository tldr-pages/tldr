# afplay

> Reproductor de audio de línea de comandos.
> Más información: <https://keith.github.io/xcode-man-pages/afplay.1.html>.

- Reproduce un archivo de audio (espera hasta que finalice la reproducción):

`afplay {{ruta/al/archivo}}`

- Reproduce un archivo de audio a una velocidad 2x (velocidad de reproducción):

`afplay --rate {{2}} {{ruta/al/archivo}}`

- Reproduce un archivo de audio a la mitad de velocidad:

`afplay --rate {{0.5}} {{ruta/al/archivo}}`

- Reproduce los primeros N segundos de un archivo de audio:

`afplay --time {{segundos}} {{ruta/al/archivo}}`
