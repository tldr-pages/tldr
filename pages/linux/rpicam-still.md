# rpicam-still

> Capture and store a photo using a Raspberry Pi camera with legacy features missing from `rpicam-jpeg`.
> More information: <https://www.raspberrypi.com/documentation/computers/camera_software.html#rpicam-still>.

- Capture a photo with different encoding:

`rpicam-still {{[-e|--encoding]}} {{bmp|png|rgb|yuv420}} {{[-o|--output]}} {{path/to/file.{{bmp|png|rgb|yuv420}}}}`

- Capture a raw image:

`rpicam-still {{[-r|--raw]}} {{[-o|--output]}} {{path/to/file.jpg}}`

- Capture a 100 second exposure image:

`rpicam-still {{[-o|--output]}} {{path/to/file.jpg}} --shutter 100000`
