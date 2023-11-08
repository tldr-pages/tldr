# settings

> Krijg informatie over het Android-besturingssysteem.
> Meer informatie: <https://adbinstaller.com/commands/adb-shell-settings-5b670d5ee7958178a2955536>.

- Toon een lijst met instellingen in de `global` namespace:

`settings list {{global}}`

- Verkrijg een waarde van een specifieke instelling:

`settings get {{global}} {{airplane_mode_on}}`

- Zet een specifieke waarde van een instelling:

`settings put {{system}} {{screen_brightness}} {{42}}`

- Verwijder een specifieke instelling:

`settings delete {{secure}} {{screensaver_enabled}}`
