# rpicam-raw

> Capture a raw video on a Raspberry Pi camera
> More information <https://www.raspberrypi.com/documentation/computers/camera_software.html#rpicam-raw>

- Capture a 2 seccond video

`rpicam-raw -t {{2000}}} -o name/of/file.raw`

- Change video dimentions, framerate, etc.

`rpicam-raw -t 5000 --width {{4056}} --height {{3040}} -o name/of/file.raw --framerate {{8}}`
