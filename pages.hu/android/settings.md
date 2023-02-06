# settings

> Információk az Android operációs rendszerről. További információk: <https://adbinstaller.com/commands/adb-shell-settings-5b670d5ee7958178a2955536>.

- A `global` névtérben található beállítások listájának megjelenítése:

`settings list {{global}}`

- Egy adott beállítás értékének lekérdezése:

`settings get {{global}} {{airplane_mode_on}}`

- Egy beállítás adott értékének beállítása:

`settings put {{system}} {{screen_brightness}} {{42}}`

- Egy adott beállítás törlése:

`settings delete {{secure}} {{screensaver_enabled}}`
