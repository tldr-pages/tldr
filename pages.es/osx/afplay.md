# afplay

> Reproductor de audio de línea de comandos.

- Reproducir un archivo de audio (espera hasta que finalice la reproducción):

`afplay {{path/to/file}}`

- Reproducir un archivo de audio a una velocidad 2x (velocidad de reproducción):

`afplay --rate 2 {{path/to/file}}`

- Reproducir un archivo de audio a la mitad de velocidad:

`afplay --rate 0.5 {{path/to/file}}`

- Reproducir los primeros N segundos de un archivo de audio:

`afplay --time {{seconds}} {{path/to/file}}`
