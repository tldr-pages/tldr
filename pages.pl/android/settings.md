# settings

> Uzyskaj informacje o systemie operacyjnym Android.
> Więcej informacji: <https://adbinstaller.com/commands/adb-shell-settings-5b670d5ee7958178a2955536>.

- Listuj ustawienia w przestrzeni `global`:

`settings list {{global}}`

- Wyświetl wartość określonego ustawienia:

`settings get {{global}} {{airplane_mode_on}}`

- Ustaw wartość dla określonego ustawienia:

`settings put {{system}} {{screen_brightness}} {{42}}`

- Delete a specific setting:

`settings delete {{secure}} {{screensaver_enabled}}`
