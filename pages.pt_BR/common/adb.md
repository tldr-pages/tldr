# adb

> Android Debug Bridge: Comunica com uma instância do emulador Android emulator ou dispositivos conectados.
> Alguns subcomandos tais como `adb shell` possuem sua própria documentação de uso.
> Mais informações: <https://developer.android.com/studio/command-line/adb>.

- Checa se o servidor adb está em execução e o inicia:

`adb start-server`

- Encerra o processo do servidor adb:

`adb kill-server`

- Inicia uma shell remota no emulador/dispositivo desejado:

`adb shell`

- Instala um app Android no emulador/dispositivo:

`adb install -r {{caminho/para/arquivo.apk}}`

- Copia um arquivo/pasta do dispositivo desejado:

`adb pull {{caminho/para/arquivo_ou_pasta_no_dispositivo}} {{caminho/para/pasta_de_destino_local}}`

- Copia um arquivo/pasta para o dispositivo desejado:

`adb push {{caminho/para/arquivo_ou_pasta_local}} {{caminho/para/pasta_de_destino_no_dispositivo}}`

- Exibe a lista de dispositivos conectados:

`adb devices`
