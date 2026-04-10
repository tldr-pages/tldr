# adb shell pm list packages

> List installed, known, or filtered packages on an Android device.
> More information: <https://developer.android.com/tools/adb>.

- List all installed packages:

`adb shell pm list packages`

- List all packages and their associated APK [f]ile paths:

`adb shell pm list packages -f`

- Only list [d]isabled packages:

`adb shell pm list packages -d`

- Only list [e]nabled packages:

`adb shell pm list packages -e`

- Only list [s]ystem packages:

`adb shell pm list packages -s`

- Only list [3]rd-party (non-system) packages:

`adb shell pm list packages -3`

- Show the [i]nstaller for each package:

`adb shell pm list packages -i`
