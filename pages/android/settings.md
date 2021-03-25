# settings

> Get information about the Android OS.

- Display a list of settings in the `global` namespace:

`settings list {{global}}`

- Get the value of a specific setting:

`settings get {{global}} {{airplane_mode_on}}`

- Set the value of a setting:

`settings put {{system}} {{screen_brightness}} {{42}}`

- Delete a specific setting:

`settings delete {{secure}} {{screensaver_enabled}}`
