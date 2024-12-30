# rpicam-still

> 使用树莓派相机捕获并存储照片，具有 `rpicam-jpeg` 中缺失的传统功能。
> 更多信息：<https://www.raspberrypi.com/documentation/computers/camera_software.html#rpicam-still>。

- 使用不同编码捕获照片：

`rpicam-still -e {{bmp|png|rgb|yuv420}} -o {{path/to/file.{{bmp|png|rgb|yuv420}}}}`

- 捕获原始图像：

`rpicam-still -r -o {{path/to/file.jpg}}`

- 捕获 100 秒曝光图像：

`rpicam-still -o {{path/to/file.jpg}} --shutter 100000`