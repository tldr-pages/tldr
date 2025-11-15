# pw-cat

> Toca e grava arquivos de áudio através do PipeWire.
> Mais informações: <https://docs.pipewire.org/page_man_pw-cat_1.html>.

- Toca um arquivo WAV no alvo padrão:

`pw-cat {{[-p|--playback]}} {{caminho/para/arquivo.wav}}`

- Toca um arquivo WAV com uma qualidade de reamostragem específica (4 por padrão):

`pw-cat {{[-q|--quality]}} {{0..15}} {{[-p|--playback]}} {{caminho/para/arquivo.wav}}`

- Faz uma gravação com o volume em 125%:

`pw-cat {{[-r|--record]}} --volume {{1.25}} {{caminho/para/arquivo.wav}}`

- Faz uma gravação com uma taxa de amostragem diferente:

`pw-cat {{[-r|--record]}} --rate {{6000}} {{caminho/para/arquivo.wav}}`

- Exibe ajuda:

`pw-cat {{[-h|--help]}}`
