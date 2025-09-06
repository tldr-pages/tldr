# adb

> Android Debug Bridge: comunica con una instancia del emulador Android o con dispositivos Android conectados.
> Algunos subcomandos como `shell` tienen su propia documentación de uso.
> Más información: <https://developer.android.com/tools/adb>.

- Comprueba si el proceso del servidor adb se está ejecutando y lo inicia:

`adb start-server`

- Finaliza el proceso del servidor adb:

`adb kill-server`

- Inicia una consola remota en el emulador/dispositivo de destino:

`adb shell`

- Instala una aplicación Android en un emulador/dispositivo:

`adb install -r {{ruta/al/archivo.apk}}`

- Copia un archivo/directorio del dispositivo de destino:

`adb pull {{ruta/al/archivo_o_directorio_del_dispositivo}} {{ruta/al/directorio_de_destino_local}}`

- Copia un archivo/directorio al dispositivo de destino:

`adb push {{ruta/al/archivo_o_directorio_local}} {{ruta/al/dirección_o_destino_del_dispositivo}}`

- Lista todos los dispositivos conectados:

`adb devices`

- Especifica a qué dispositivo envía los comandos si hay varios dispositivos:

`adb -s {{id_del_dispositivo}} {{shell}}`
