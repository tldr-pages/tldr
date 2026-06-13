# adb connect

> Connect to an Android device wirelessly.
> More information: <https://developer.android.com/tools/adb>.

- Pair with an Android device (address and pairing code can be found in developer options):

`adb pair {{ip_address}}:{{port}}`

- Connect to an Android device (port will be different from pairing):

`adb connect {{ip_address}}:{{port}}`

- Disconnect a device:

`adb disconnect {{ip_address}}:{{port}}`
