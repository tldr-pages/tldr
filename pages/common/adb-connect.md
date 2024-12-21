# adb connect

> Connect to an android device wirelessly.
> More information: <https://developer.android.com/tools/adb>.

- Pair with an android device (address and pairing code can be found in developer options:

`adb pair {{ip_address}}:{{port}}`

- Connect to an android device (port will be different from pairing):

`adb connect {{ip_address}}:{{port}}`

- Disconnect a device:

`adb disconnect {{ip_address}}:{{port}}`
