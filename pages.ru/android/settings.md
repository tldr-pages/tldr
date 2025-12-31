# settings

> Получить информацию об операционной системе Android.
> Больше информации: <https://web.archive.org/web/20240525010124/https://adbinstaller.com/commands/adb-shell-settings-5b670d5ee7958178a2955536>.

- Показать список настроек в `global`:

`settings list {{global}}`

- Получить значение определенного параметра:

`settings get {{global}} {{airplane_mode_on}}`

- Задать значение параметра:

`settings put {{system}} {{screen_brightness}} {{42}}`

- Удалить конкретную настройку:

`settings delete {{secure}} {{screensaver_enabled}}`
