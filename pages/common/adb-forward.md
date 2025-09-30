# adb forward

> Connect to an Android device wirelessly.
> More information: <https://developer.android.com/tools/adb>.

- Forward a TCP port:

`adb forward tcp:{{local_port}} tcp:{{remote_port}}`

- List all forwardings:

`adb forward --list`

- Remove a forwarding rule:

`adb forward --remove tcp:{{local_port}}`

- Remove all forwarding rules:

`adb forward --remove-all`
