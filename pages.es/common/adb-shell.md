# adb shell

> Android Debug Bridge Shell: Ejecuta comandos shell remotos en una instancia del emulador de Android o en dispositivos Android conectados.
> Más información: <https://developer.android.com/studio/command-line/adb>.

- Inicia una shell interactiva remota en el emulador o dispositivo:

`adb shell`

- Obtén todas las propiedades del emulador o dispositivo:

`adb shell getprop`

- Revierte todos los permisos de ejecución a sus valores por defecto:

`adb shell pm reset-permissions`

- Revoca un permiso peligroso para una aplicación:

`adb shell pm revoke {{paquete}} {{permission}}`

- Activa un evento de clave:

`adb shell input keyevent {{keycode}}`

- Borra los datos de una aplicación en un emulador o dispositivo:

`adb shell pm clear {{paquete}}`

- Inicia una actividad en el emulador o dispositivo:

`adb shell am start -n {{paquete}}/{{activity}}`

- Inicia la actividad de inicio en un emulador o dispositivo:

`adb shell am start -W -c android.intent.category.HOME -a android.intent.action.MAIN`
