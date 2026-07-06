# pw-cat

> Riproduce e registra file audio tramite PipeWire.
> Vedi anche: `wpctl`, `pw-cli`.
> Maggiori informazioni: <https://docs.pipewire.org/page_man_pw-cat_1.html>.

- Riproduce un file WAV sulla destinazione predefinita:

`pw-cat {{[-p|--playback]}} {{percorso/del/file.wav}}`

- Riproduce un file MIDI:

`pw-cat {{[-p|--playback]}} {{[-m|--midi]}} {{percorso/del/file.mid}}`

- Riproduce un file DSD:

`pw-cat {{[-p|--playback]}} {{[-d|--dsd]}} {{percorso/del/file.dsf}}`

- Riproduce un file audio compresso usando passthrough (richiede integrazione FFmpeg):

`pw-cat {{[-p|--playback]}} {{[-o|--encoded]}} {{percorso/del/file.ac3}}`

- Riproduce un file WAV con una qualità di ricampionamento specificata (4 predefinita):

`pw-cat {{[-p|--playback]}} {{[-q|--quality]}} {{0..15}} {{percorso/del/file.wav}}`

- Registra un file MIDI:

`pw-cat {{[-r|--record]}} {{[-m|--midi]}} {{percorso/del/file.mid}}`

- Registra un campione a un livello di volume del 125%:

`pw-cat {{[-r|--record]}} --volume {{1.25}} {{percorso/del/file.wav}}`

- Registra un campione usando una frequenza di campionamento diversa:

`pw-cat {{[-r|--record]}} --rate {{6000}} {{percorso/del/file.wav}}`
