# pw-cat

> Reproduce y graba archivos de audio a través de PipeWire.
> Vea también: `wpctl`, `pw-cli`.
> Más información: <https://docs.pipewire.org/page_man_pw-cat_1.html>.

- Reproduce un archivo WAV en el destino predeterminado:

`pw-cat {{[-p|--playback]}} {{ruta/al/archivo.wav}}`

- Reproduce un archivo MIDI:

`pw-cat {{[-p|--playback]}} {{[-m|--midi]}} {{ruta/al/archivo.mid}}`

- Reproduce un archivo DSD:

`pw-cat {{[-p|--playback]}} {{[-d|--dsd]}} {{ruta/al/archivo.dsf}}`

- Reproduce un archivo de audio comprimido mediante passthrough (requiere integración con FFmpeg):

`pw-cat {{[-p|--playback]}} {{[-o|--encoded]}} {{ruta/al/archivo.ac3}}`

- Reproduce un archivo WAV con una calidad de remuestreo especificada (4 por defecto):

`pw-cat {{[-p|--playback]}} {{[-q|--quality]}} {{0..15}} {{ruta/al/archivo.wav}}`

- Graba un archivo MIDI:

`pw-cat {{[-r|--record]}} {{[-m|--midi]}} {{ruta/al/archivo.mid}}`

- Graba una muestra con un volumen del 125 %:

`pw-cat {{[-r|--record]}} --volume {{1.25}} {{ruta/al/archivo.wav}}`

- Graba una muestra utilizando una frecuencia de muestreo diferente:

`pw-cat {{[-r|--record]}} --rate {{6000}} {{ruta/al/archivo.wav}}`
