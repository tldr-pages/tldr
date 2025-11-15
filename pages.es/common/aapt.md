# aapt

> Herramienta para empaquetado de activos de Android.
> Compila y empaqueta recursos de una app de Android.
> Más información: <https://manned.org/aapt>.

- Lista los archivos contenidos en un archivo APK:

`aapt list {{ruta/al/app.apk}}`

- Muestra la metadata de una app (versión, permisos, etc.):

`aapt dump badging {{ruta/al/app.apk}}`

- Crea un nuevo archivo APK con archivos de un directorio especificado:

`aapt package -F {{ruta/al/app.apk}} {{ruta/al/directorio}}`
