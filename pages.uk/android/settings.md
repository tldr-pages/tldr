# settings

> Отримайте інформацію про операційну систему Android.
> Більше інформації: <https://adbinstaller.com/commands/adb-shell-settings-5b670d5ee7958178a2955536>.

- Вивести список налаштувань в глобальному (`global`) просторі імен:

`settings list {{global}}`

- Отримайте значення конкретного налаштування:

`settings get {{global}} {{airplane_mode_on}}`

- Встановіть значення для налаштування:

`settings put {{system}} {{screen_brightness}} {{42}}`

- Видаліть визначене налаштування:

`settings delete {{secure}} {{screensaver_enabled}}`
