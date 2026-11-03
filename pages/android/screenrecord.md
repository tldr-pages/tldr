# screenrecord

> Record a video of a mobile display.
> Note: This command can only be used through `adb shell`.
> More information: <https://developer.android.com/tools/adb#screenrecord>.

- Record the screen:

`screenrecord {{path/to/file}}.mp4`

- Record the screen at a specific resolution:

`screenrecord --size {{1280x720}} {{path/to/file}}.mp4`

- Record the screen with a specific bitrate:

`screenrecord --bit-rate {{6000000}} {{path/to/file}}.mp4`

- Record the screen with a maximum duration (in seconds, 180 seconds is the maximum):

`screenrecord --time-limit {{180}} {{path/to/file}}.mp4`

- Display help:

`screenrecord --help`
