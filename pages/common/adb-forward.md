# adb forward

> Forward socket connections to a connected Android device or emulator.
> More information: <https://developer.android.com/tools/adb>.

- Forward a TCP port to the only connected emulator or device:

`adb forward tcp:{{local_port}} tcp:{{remote_port}}`

- Forward a TCP port to a specific emulator or device (by device ID / [s]erial number):

`adb -s {{device_ID}} forward tcp:{{local_port}} tcp:{{remote_port}}`

- List all forwardings:

`adb forward --list`

- Remove a forwarding rule:

`adb forward --remove tcp:{{local_port}}`

- Remove all forwarding rules:

`adb forward --remove-all`
