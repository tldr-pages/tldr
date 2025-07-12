# scrcpy

> Display and control your Android device on a desktop.
> More information: <https://github.com/Genymobile/scrcpy>.

- Display a mirror of a connected device:

`scrcpy`

- Turn the device screen off and prevent it from sleeping while mirroring:

`scrcpy {{[-S|--turn-screen-off]}} {{[-w|--stay-awake]}}`

- Display a mirror of a specific device based on its ID or IP address (find it under the `adb devices` command):

`scrcpy {{[-s|--serial]}} {{0123456789abcdef|192.168.0.1:5555}}`

- Start display in fullscreen mode:

`scrcpy {{[-f|--fullscreen]}}`

- Show touches on physical device:

`scrcpy {{[-t|--show-touches]}}`

- Record display screen:

`scrcpy {{[-r|--record]}} {{path/to/file.mp4}}`

- Specify the target directory for pushing files to device by drag and drop (non-APK):

`scrcpy --push-target {{path/to/directory}}`
