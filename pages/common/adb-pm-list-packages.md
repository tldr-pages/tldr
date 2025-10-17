# pm list packages

> List installed, known, or filtered packages on an Android device.
> More information: <https://developer.android.com/tools/adb>.

- List all installed packages:

`adb shell pm list packages`

- List all packages and their associated APK file paths:

`adb shell pm list packages -f`

- Only list disabled packages:

`adb shell pm list packages -d`

- Only list enabled packages:

`adb shell pm list packages -e`

- Only list system packages:

`adb shell pm list packages -s`

- Only list third-party (non-system) packages:

`adb shell pm list packages -3`

- Show the installer for each package:

`adb shell pm list packages -i`
