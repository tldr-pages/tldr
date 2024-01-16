# rpicam

> View and store footage from connected Raspberry Pi cameras.
> More information: <https://www.raspberrypi.com/documentation/computers/camera_software.html>.

- Start a camera preview stream:

`rpicam-hello`

- Tune the configuration for a particular camera sensor:

`rpicam-hello --tuning-file {{/usr/share/libcamera/ipa/rpi/path/to/config.json}}`

- Capture a JPEG image:

`rpicam-jpeg {{path/to/file.jpeg}}`

- Capture a video for the specified duration:

`rpicam-vid -t {{duration_in_ms}} -o {{path/to/file.h264}}`

- Capture a RAW video:

`rpicam-raw -t {{duration_in_ms}} -o {{path/to/file.raw}}`
