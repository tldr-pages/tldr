# emulator

> Manager Android emulators from the command line.
> More information: <https://developer.android.com/studio/run/emulator-commandline>.

- Display the help:

`emulator -help`

- Start an Android emulator device:

`emulator -avd {{name}}`

- Display the webcams on your development computer that are available for emulation:

`emulator -avd {{name}} -webcam-list`

- Start an emulator overriding the facing back camera setting (use `-camera-front` for front camera):

`emulator -avd {{name}} -camera-back {{none|emulated|webcamN}}`

- Start an emulator, with a maximun network speed:

`emulator -avd {{name}} -netspeed {{gsm|hscsd|gprs|edge|hsdpa|lte|evdo|full}}`

- Start an emulator with network latency:

`emulator -avd {{name}} -netdelay {{gsm|hscsd|gprs|edge|hsdpa|lte|evdo|none}}`

- Start an emulator, making all TCP connections through a specified HTTP/HTTPS proxy (port number is required):

`emulator -avd {{name}} -http-proxy {{http://example.com:80}}`

- Start an emulator with a given SD card partition image file:

`emulator -avd {{name}} -sdcard {{path/to/sdcard.img}}`
