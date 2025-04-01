# rpicam-raw

> 在 Raspberry Pi 相机上捕获原始视频。
> 更多信息：<https://www.raspberrypi.com/documentation/computers/camera_software.html#rpicam-raw>.

- 捕获指定秒数的视频：

`rpicam-raw -t {{2000}} -o {{path/to/file.raw}}`

- 更改视频分辨率和帧率：

`rpicam-raw -t {{5000}} --width {{4056}} --height {{3040}} -o {{path/to/file.raw}} --framerate {{8}}`