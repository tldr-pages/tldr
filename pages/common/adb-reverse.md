# adb reverse

> Android Debug Bridge Reverse: reverse socket connections from an Android emulator instance or connected Android devices.
> More information: <https://developer.android.com/studio/command-line/adb>.

- List all reverse socket connections from emulator/device:

`adb reverse --list`

- Reverse a TCP port from emulator/device to localhost:

`adb reverse tcp:{{remote_port}} tcp:{{local_port}}`

- Remove a reverse socket connections from emulator/device:

`adb reverse --remove tcp:{{remote_port}}`

- Remove all reverse socket connections from emulator/device:

`adb reverse --remove-all`
