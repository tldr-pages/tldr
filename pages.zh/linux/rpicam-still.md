# rpicam-still

> 使用 Raspberry Pi 相机拍摄并存储照片，支持 `rpicam-jpeg` 不具备的旧功能。
> 更多信息：<https://www.raspberrypi.com/documentation/computers/camera_software.html#rpicam-still>。

- 使用不同的编码格式拍摄照片：

`rpicam-still -e {{bmp|png|rgb|yuv420}} -o {{path/to/file.{{bmp|png|rgb|yuv420}}}}`

- 拍摄原始图像：

`rpicam-still -r -o {{path/to/file.jpg}}`

- 拍摄 100 秒曝光的照片：

`rpicam-still -o {{path/to/file.jpg}} --shutter 100000`
