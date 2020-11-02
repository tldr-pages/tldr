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

`adb install -r {{ruta/al/archivo.apk}}`

- Copia un archivo/directorio desde el dispositivo de destino:

`adb pull {{ruta/al/archivo_o_directorio_en_el_dispositivo}} {{ruta/al/directorio_de_destino_local}}`

- Copia un archivo/directorio al dispositivo de destino:

`adb push {{ruta/al/archivo_o_directorio_local}} {{ruta/al/directorio_de_destino_en_el_dispositivo}}`

- Obtiene una lista de dispositivos conectados:

`adb devices`
