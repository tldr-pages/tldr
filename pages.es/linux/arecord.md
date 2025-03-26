# arecord

> Grabadora de sonido para el controlador de tarjeta de sonido ALSA.
> Más información: <https://manned.org/arecord>.

- Graba un fragmento en calidad "CD" (finaliza con `<Ctrl c>` cuando termines):

`arecord -vv --format=cd {{ruta/al/archivo.wav}}`

- Graba un fragmento en calidad "CD", con una duración fija de 10 segundos:

`arecord -vv --format=cd --duration={{10}} {{ruta/al/archivo.wav}}`

- Graba un fragmento y lo guarda como MP3 (finaliza con `<Ctrl c>` cuando termines):

`arecord -vv --format=cd --file-type raw | lame -r - {{ruta/al/archivo.mp3}}`

- Muestra todas las tarjetas de sonido y dispositivos de audio digital:

`arecord --list-devices`

- Permite una interfaz interactiva (por ejemplo, usa la `<Space>` o `<Enter>` para reproducir o pausar):

`arecord --interactive`

- Prueba tu micrófono grabando una muestra de 5 segundos y reproduciéndola:

`arecord -d 5 test-mic.wav && aplay test-mic.wav && rm test-mic.wav`
