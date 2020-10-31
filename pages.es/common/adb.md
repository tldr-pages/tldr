# adb

> Android Debug Bridge: comunica con una instancia de un emulador Android o conecta dispositivos Android.
> Más información: <https://developer.android.com/studio/command-line/adb>.

- Verifica si el proceso del servidor adb está ejecutandose y lo inicia:

`adb start-server`

- Termina el proceso del servidor adb:

`adb kill-server`

- Inicia una terminal remota en la instance del emulador/dispositivo de destino:

`adb shell`

- Instala una aplicación Android a un emulador/dispositivo:

`adb install -r {{path/to/file.apk}}`

- Copia un archivo/directorio desde el dispositivo de destino:

`adb pull {{path/to/device_file_or_directory}} {{path/to/local_destination_directory}}`

- Copia un archivo/directorio al dispositivo de destino:

`adb push {{path/to/local_file_or_directory}} {{path/to/device_destination_directory}}`

- Obtiene una lista de dispositivos conectados:

`adb devices`
