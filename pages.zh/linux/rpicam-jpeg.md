# rpicam-jpeg

> 使用树莓派相机捕获并存储JPEG图像。
> 更多信息：<https://www.raspberrypi.com/documentation/computers/camera_software.html#rpicam-jpeg>。

- 捕获图像并命名文件：

`rpicam-jpeg -o {{path/to/file.jpg}}`

- 捕获具有指定尺寸的图像：

`rpicam-jpeg -o {{path/to/file.jpg}} --width {{1920}} --height {{1080}}`

- 捕获曝光时间为20秒，增益为150%的图像：

`rpicam-jpeg -o {{path/to/file.jpg}} --shutter 20000 --gain 1.5`