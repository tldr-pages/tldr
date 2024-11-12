# mpv

> Um tocador de vídeo/audio baseado no MPlayer.
> Mais informações: <https://mpv.io>.

- Toca um vídeo ou áudio de uma URL ou arquivo:

`mpv {{url|caminho/para/arquivo}}'`

- Avança/retrocede 5 segundos:

`LEFT <or> RIGHT`

- Avança/retrocede 1 minuto:

`DOWN <or> UP`

- Aumenta ou diminui a velocidade de reprodução em 10%:

`[ <or> ]`

- Captura a imagem atual (salva em `./mpv-shotNNNN.jpg` por padrão):

`s`

- Toca um arquivo em uma velocidade especificada (1 por padrão):

`mpv --speed {{0.01..100}} {{caminho/para/arquivo}}`

- Toca um arquivo usando um perfil definido no arquivo `mpv.conf`:

`mpv --profile {{nome_do_perfil}} {{caminho/para/arquivo}}`

- Mostra a saída da webcam ou de outro dispositivo de entrada de vídeo:

`mpv {{/dev/video0}}`
