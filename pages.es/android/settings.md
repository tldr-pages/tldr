# settings

> Muestra información sobre el sistema operativo Android.
> Más información: <https://adbinstaller.com/commands/adb-shell-settings-5b670d5ee7958178a2955536>.

- Muestra una lista de configuraciones en el espacio de nombres `global`:

`settings list {{global}}`

- Obtén el valor de una configuración específica:

`settings get {{global}} {{airplane_mode_on}}`

- Establece el valor de un ajuste:

`settings put {{system}} {{screen_brightness}} {{42}}`

- Elimina un ajuste específico:

`settings delete {{secure}} {{screensaver_enabled}}`
