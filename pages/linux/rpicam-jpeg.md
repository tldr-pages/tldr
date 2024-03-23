# rpicam-jpeg

> Capture and store a JPEG image using a Raspberry Pi camera.
> More information: <https://www.raspberrypi.com/documentation/computers/camera_software.html#rpicam-jpeg>.

- Capture an image and name the file:

`rpicam-jpeg -o {{path/to/file.jpg}}`

- Capture an image with set dimensions:

`rpicam-jpeg -o {{path/to/file.jpg}} --width {{1920}} --height {{1080}}`

- Capture an image with an exposure of 20 seconds and a gain of 150%:

`rpicam-jpeg -o {{path/to/file.jpg}} --shutter 20000 --gain 1.5`
