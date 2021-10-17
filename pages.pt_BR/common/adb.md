# adb

> Android Debug Bridge: Comunica com uma instância do emulador Android emulator ou dispositivos conectados.
> Alguns subcomandos tais como `adb shell` possuem sua própria documentação de uso.
> Mais informações: <https://developer.android.com/studio/command-line/adb>.

- Checar se o servidor adb está em execução e o iniciar:

`adb start-server`

- Encerra o processo do servidor adb:

`adb kill-server`

- Iniciar uma shell remota no emulador/dispositivo desejado:

`adb shell`

- Install um app Android no emulador/dispositivo:

`adb install -r {{path/to/file.apk}}`

- Copiar um arquivo/pasta do dispositivo desejado:

`adb pull {{path/to/device_file_or_directory}} {{path/to/local_destination_directory}}`

- Copiar um arquivo/pasta para o dispositivo desejado:

`adb push {{path/to/local_file_or_directory}} {{path/to/device_destination_directory}}`

- Exibir a lista de dispositivos conectados:

`adb devices`
