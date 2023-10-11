# settings

> Get information about the Android OS.
> More information: <https://adbinstaller.com/commands/adb-shell-settings-5b670d5ee7958178a2955536>.

- Display a list of settings in the `global` namespace:

`settings list {{global}}`

- Get a value of a specific setting:

`settings get {{global}} {{airplane_mode_on}}`

- Set a specific value of a setting:

`settings put {{system}} {{screen_brightness}} {{42}}`

- Delete a specific setting:

`settings delete {{secure}} {{screensaver_enabled}}`
