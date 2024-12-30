# rpicam-hello

> 使用树莓派摄像头查看实时摄像头流。
> 更多信息请访问：<https://www.raspberrypi.com/documentation/computers/camera_software.html#rpicam-hello>。

- 显示特定时间（以毫秒为单位）的摄像头预览流：

`rpicam-hello -t {{time}}`

- 针对特定摄像头传感器调整配置：

`rpicam-hello --tuning-file {{/usr/share/libcamera/ipa/rpi/path/to/config.json}}`