# settings

> Android işletim sistemi ile ilgili bilgi al.
> Daha fazla bilgi için: <https://adbinstaller.com/commands/adb-shell-settings-5b670d5ee7958178a2955536>.

- `global` isim alanındaki ayarların sırasını görüntüle:

`settings list {{global}}`

- Belirtilen ayarın değerini al:

`settings get {{global}} {{airplane_mode_on}}`

- Bir ayarın değerini belirle:

`settings put {{system}} {{screen_brightness}} {{42}}`

- Belirtilen ayarı sil:

`settings delete {{secure}} {{screensaver_enabled}}`
