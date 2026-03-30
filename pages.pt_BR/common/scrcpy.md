# scrcpy

> Exiba e controle seu dispositivo Android em um desktop.
> Mais informações: <https://github.com/Genymobile/scrcpy>.

- Espelha a tela de um dispositivo conectado:

`scrcpy`

- Desliga a tela do dispositivo e previne que ele entre em modo de suspensão enquanto espelha a tela:

`scrcpy {{[-S|--turn-screen-off]}} {{[-w|--stay-awake]}}`

- Espelha a tela de um dispositivo com base no seu ID ou endereço de IP (visível no comando `adb devices`):

`scrcpy {{[-s|--serial]}} {{0123456789abcdef|192.168.0.1:5555}}`

- Mostra toques no dispositivo físico:

`scrcpy {{[-t|--show-touches]}}`

- Grava a tela do dispositivo:

`scrcpy {{[-r|--record]}} {{caminho/para/arquivo.mp4}}`

- Especifica um diretório alvo para enviar arquivos para o disposivivo (exceto APKs):

`scrcpy --push-target {{caminho/para/diretório}}`

- Visualiza a câmera do dispositivo (requer Android 12 ou superior):

`scrcpy --video-source camera`

- Cria um dispositivo Video4Linux2 a partir da câmera do dispositivo (o pacote `v4l2loopback` deve estar instalado):

`scrcpy --video-source camera --camera-size {{1920x1080}} --v4l2-sink {{/dev/video0}} --no-playback`
