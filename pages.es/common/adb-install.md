# adb install

> Instalación de Android Debug Bridge: Envía paquetes a una instancia del emulador de Android o a dispositivos Android conectados.
> Más información: <https://developer.android.com/tools/adb>.

- Envía una aplicación Android a un emulador/dispositivo:

`adb install {{ruta/al/archivo.apk}}`

- Envía una aplicación Android a un emulador/dispositivo específico (ignora `$ANDROID_SERIAL`):

`adb -s {{numero_de_serie}} install {{ruta/al/archivo.apk}}`

- Reinstala una aplicación existente, manteniendo sus datos:

`adb install -r {{ruta/al/archivo.apk}}`

- Envía una aplicación Android permitiendo bajar el código de versión (sólo paquetes depurables):

`adb install -d {{ruta/al/archivo.apk}}`

- Concede todos los permisos enumerados en el manifiesto de la aplicación:

`adb install -g {{ruta/al/archivo.apk}}`

- Actualiza rápidamente un paquete instalado actualizando sólo las partes del APK que han cambiado:

`adb install --fastdeploy {{ruta/al/archivo.apk}}`
