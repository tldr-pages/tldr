# adb shell pm

> Show information about apps on an Android device.
> More information: <https://adbinstaller.com/commands>.

- Print a list of all installed apps:

`adb shell pm list packages`

- Print a list of all installed system apps:

`adb shell pm list packages -s`

- Print a list of all installed 3rd-Party apps:

`adb shell pm list packages -3`

- Print a list of apps matching specific keywords:

`adb shell pm list packages {{keywords}}`

- Print the path of the APK of a specific app:

`adb shell pm path {{app}}`
