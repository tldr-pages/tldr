# scrcpy

> Display and control your Android device on a desktop .
> More information: <https://github.com/Genymobile/scrcpy>.

- Display/mirror your device:

`scrcpy`

- Start display in fullscreen mode:

`scrcpy -f`

- Rotate the display screen. Each incremental value adds a 90 degree counterclockwise rotation:

`scrcpy --rotation {{0|1|2|3}}`

- Show touches on physical device:

`scrcpy -t`

- Record display screen:

`scrcpy --record {{path/to/file.mp4}}`

- Set target directory for pushing files to device by drag and drop (non-APK):

`scrcpy --push-target {{path/to/directory}}`
