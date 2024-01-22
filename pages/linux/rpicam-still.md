# rpicam-still

> Capture and store a photo using a Raspberry Pi camera with legacy features missing from `rpicam-jpeg`.
> More information: <https://www.raspberrypi.com/documentation/computers/camera_software.html#rpicam-still>.

- Capture a photo with different encoding:

`rpicam-still -e {{bmp|png|rgb|yuv420}} -o {{path/to/file.{{bmp|png|rgb|yuv420}}}}`

- Capture a raw image:

`rpicam-still -r -o {{path/to/file.jpg}}`

- Capture a 100 second exposure image:

`rpicam-still -o {{path/to/file.jpg}} --shutter 100000`
