# settings

> Uzyskaj informacje o systemie operacyjnym Android.
> Więcej informacji: <https://web.archive.org/web/20240525010124/https://adbinstaller.com/commands/adb-shell-settings-5b670d5ee7958178a2955536>.

- Wypisz ustawienia w przestrzeni `global`:

`settings list {{global}}`

- Wyświetl wartość określonego ustawienia:

`settings get {{global}} {{airplane_mode_on}}`

- Ustaw wartość określonego ustawienia:

`settings put {{system}} {{screen_brightness}} {{42}}`

- Usuń określone ustawienie:

`settings delete {{secure}} {{screensaver_enabled}}`
