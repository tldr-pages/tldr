# pw-cat

> Toca e grava arquivos de áudio através do pipewire.
> Mais informações: <https://fedoraproject.org/wiki/QA:Testcase_PipeWire_PipeWire_CLI>.

- Toca um arquivo WAV no alvo padrão:

`pw-cat --playback {{caminho/para/arquivo.wav}}`

- Toca um arquivo WAV com uma qualidade de reamostragem específica (4 por padrão):

`pw-cat --quality {{0..15}} --playback {{caminho/para/arquivo.wav}}`

- Faz uma gravação com um volume diferente:

`pw-cat --record --volume={{0.1}} {{caminho/para/arquivo.wav}}`

- Faz uma gravação com uma taxa de amostragem diferente:

`pw-cat --record --rate={{6000}} {{caminho/para/arquivo.wav}}`
