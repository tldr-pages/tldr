# rpicam-raw

> Capture a raw video on a Raspberry Pi camera.
> More information: <https://www.raspberrypi.com/documentation/computers/camera_software.html#rpicam-raw>.

- Capture a video for a specific amount of seconds:

`rpicam-raw -t {{2000}}} -o {{path/to/file.raw}}`

- Change video dimensions and framerate:

`rpicam-raw -t {{5000}} --width {{4056}} --height {{3040}} -o {{path/to/file.raw}} --framerate {{8}}`
