# mpv

> Um tocador de vídeo/audio baseado no MPlayer.
> Veja também: `mplayer`, `vlc`.
> Mais informações: <https://mpv.io/manual/stable/>.

- Toca um vídeo ou áudio de uma URL ou arquivo:

`mpv {{url|caminho/para/arquivo}}`

- Avança/retrocede 5 segundos:

`{{<ArrowLeft>|<ArrowRight>}}`

- Avança/retrocede 1 minuto:

`{{<ArrowDown>|<ArrowUp>}}`

- Diminui ou aumenta a velocidade de reprodução em 10%:

`{{<[>|<]>}}`

- Captura a imagem do quadro atual (salva em `./mpv-shotNNNN.jpg` por padrão):

`<s>`

- Toca um arquivo em uma velocidade especificada (1 por padrão):

`mpv --speed {{0.01..100}} {{caminho/para/arquivo}}`

- Toca um arquivo usando um perfil definido no arquivo `mpv.conf`:

`mpv --profile {{nome_do_perfil}} {{caminho/para/arquivo}}`

- Mostra a saída da webcam ou de outro dispositivo de entrada de vídeo:

`mpv {{/dev/video0}}`
