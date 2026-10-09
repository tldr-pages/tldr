# adb push

> Copy files or directories from the computer to a connected Android device or emulator.
> See also: `adb pull`.
> More information: <https://developer.android.com/tools/adb>.

- Copy a file or directory to the device:

`adb push {{path/to/local_file_or_directory}} {{path/to/device_destination_directory}}`

- Copy multiple files or directories to the device:

`adb push {{path/to/local_file1 path/to/local_file2 ...}} {{path/to/device_destination_directory}}`

- Copy a file to the `Download` directory of the device:

`adb push {{path/to/local_file}} /sdcard/Download/`

- Copy a file to a specific emulator/device (overrides `$ANDROID_SERIAL`):

`adb -s {{serial_number}} push {{path/to/local_file}} {{path/to/device_destination_directory}}`

- Copy only the files that have different timestamps on the computer than on the device:

`adb push --sync {{path/to/local_directory}} {{path/to/device_destination_directory}}`

- Simulate the copy without storing the files on the device:

`adb push -n {{path/to/local_file_or_directory}} {{path/to/device_destination_directory}}`
