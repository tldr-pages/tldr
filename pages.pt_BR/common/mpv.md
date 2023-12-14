# mpv

> Um tocador de vídeo/audio baseado no MPlayer.
> Mais informações: <https://mpv.io>.

- Tocar um vídeo ou áudio de uma URL ou arquivo:

`mpv {{url|caminho/para/arquivo}}'`

- Avançar/retroceder 5 segundos:

`ESQUERDA <ou> DIREITA`

- Avançar/retroceder 1 minuto:

`BAIXO <ou> CIMA`

- Aumentar ou diminuir a velocidade de reprodução em 10%:

`[ <ou> ]`

- Capturar a imagem atual (salva em `mpv-shotNNNN.jpg` por padrão):

`s`

- Tocar um arquivo em uma velocidade especificada (1 por padrão):

`mpv --speed {{0.01..100}} {{caminho/para/arquivo}}`

- Tocar um arquivo usando um perfil definido no arquivo `mpv.conf`:

`mpv --profile {{nome_do_perfil}} {{caminho/para/arquivo}}`

- Mostrar a saída da webcam ou de outro dispositivo de entrada de vídeo:

`mpv /dev/{{video0}}`
