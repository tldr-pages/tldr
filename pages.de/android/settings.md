# settings

> Verwalte Android-Systemeinstellungen.
> Weitere Informationen: <https://web.archive.org/web/20240525010124/https://adbinstaller.com/commands/adb-shell-settings-5b670d5ee7958178a2955536>.

- Gib eine Liste aller Einstellungen im Namespace `global` aus:

`settings list {{global}}`

- Gib den Wert einer bestimmten Einstellung aus:

`settings get {{global}} {{airplane_mode_on}}`

- Setze den Wert einer bestimmten Einstellung:

`settings put {{system}} {{screen_brightness}} {{42}}`

- Lösche eine bestimmte Einstellung:

`settings delete {{secure}} {{screensaver_enabled}}`
