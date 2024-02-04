# adb

> Android Debug Bridge: communicate with an Android emulator instance or connected Android devices.
> Some subcommands such as `adb shell` have their own usage documentation.
> More information: <https://developer.android.com/studio/command-line/adb>.

- Check whether the adb server process is running and start it:

`adb start-server`

- Terminate the adb server process:

`adb kill-server`

- Start a remote shell in the target emulator/device instance:

`adb shell`

- Push an Android application to an emulator/device:

`adb install -r {{path/to/file.apk}}`

- Copy a file/directory from the target device:

`adb pull {{path/to/device_file_or_directory}} {{path/to/local_destination_directory}}`

- Copy a file/directory to the target device:

`adb push {{path/to/local_file_or_directory}} {{path/to/device_destination_directory}}`

- List all connected devices:

`adb devices`
