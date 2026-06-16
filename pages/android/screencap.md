# screencap

> Take a screenshot of a mobile display.
> Note: This command can only be used through `adb shell`.
> More information: <https://developer.android.com/tools/adb#screencap>.

- Take a screenshot:

`screencap {{path/to/image.png}}`

- Print file contents to `stdout` as PNG:

`screencap -p`

- Take a screenshot and save it over an `adb` connection:

`adb shell screencap -p > {{path/to/image.png}}`

- Display help:

`screencap -h`
