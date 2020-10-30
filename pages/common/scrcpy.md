# scrcpy

> Display and control your Android device on a desktop.
> More information: <https://github.com/Genymobile/scrcpy>.

- Display a mirror of a connected device:

`scrcpy`

- Display a mirror of a specific device based on its ID or IP address (find it under the `adb devices` command):

`scrcpy --serial {{0123456789abcdef|192.168.0.1:5555}}`

- Start display in fullscreen mode:

`scrcpy --fullscreen`

- Rotate the display screen. Each incremental value adds a 90 degree counterclockwise rotation:

`scrcpy --rotation {{0|1|2|3}}`

- Show touches on physical device:

`scrcpy --show-touches`

- Record display screen:

`scrcpy --record {{path/to/file.mp4}}`

- Set target directory for pushing files to device by drag and drop (non-APK):

`scrcpy --push-target {{path/to/directory}}`
