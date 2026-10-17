# adb pull

> Copy files or directories from a connected Android device or emulator to the computer.
> See also: `adb push`.
> More information: <https://developer.android.com/tools/adb>.

- Copy a file or directory from the device to the current directory:

`adb pull {{path/to/device_file_or_directory}}`

- Copy a file or directory from the device to a specific local directory:

`adb pull {{path/to/device_file_or_directory}} {{path/to/local_destination_directory}}`

- Copy multiple files or directories from the device:

`adb pull {{path/to/device_file1 path/to/device_file2 ...}} {{path/to/local_destination_directory}}`

- Copy the photos taken with the camera of the device:

`adb pull /sdcard/DCIM/Camera/ {{path/to/local_destination_directory}}`

- Copy a file from a specific emulator/device (overrides `$ANDROID_SERIAL`):

`adb -s {{serial_number}} pull {{path/to/device_file}} {{path/to/local_destination_directory}}`

- Copy a file, preserving its timestamp and mode:

`adb pull -a {{path/to/device_file}} {{path/to/local_destination_directory}}`
