# settings

> Acquisici informazioni su Android OS.
> Maggiori informazioni: <https://adbinstaller.com/commands/adb-shell-settings-5b670d5ee7958178a2955536>.

- Visualizza una lista di impostazioni nel namespace `global`:

`settings list {{global}}`

- Ottieni il valore di un'impostazione specifica:

`settings get {{global}} {{airplane_mode_on}}`

- Imposta il valore di un'impostazione:

`settings put {{system}} {{screen_brightness}} {{42}}`

- Elimina un'impostazione specifica:

`settings delete {{secure}} {{screensaver_enabled}}`
