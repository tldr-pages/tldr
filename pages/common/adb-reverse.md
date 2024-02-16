# adb reverse

> Android Debug Bridge Reverse: reverse socket connections from an Android emulator instance or connected Android devices.
> More information: <https://developer.android.com/tools/adb>.

- List all reverse socket connections from emulators and devices:

`adb reverse --list`

- Reverse a TCP port from an emulator or device to localhost:

`adb reverse tcp:{{remote_port}} tcp:{{local_port}}`

- Remove a reverse socket connections from an emulator or device:

`adb reverse --remove tcp:{{remote_port}}`

- Remove all reverse socket connections from all emulators and devices:

`adb reverse --remove-all`
