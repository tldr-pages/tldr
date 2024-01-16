# rpicam-still
> Capture and store a photo using a Raspberry Pi camera with legacy features missing from `rpicam-jpeg`.
> More information: <https://www.raspberrypi.com/documentation/computers/camera_software.html#rpicam-still>.

- Capture a photo with bmp encoding:

`rpicam-still -e {{bmp}} -o name/of/file.bmp`

- Capture a raw image:

`rpicam-still -r -o name/of/file.jpg`

- Capture a 100 seccond exposure image:

`rpicam-still -o name/of/file.jpg --shutter {{100000000}}`
