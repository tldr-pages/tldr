# wacaw

> 从连接的相机捕获静态图片和视频。
> 更多信息：<https://webcam-tools.sourceforge.net>。

- 从网络摄像头拍照：

`wacaw {{filename}}`

- 录制视频：

`wacaw --video {{filename}} --duration {{10}}`

- 以自定义分辨率拍照：

`wacaw --width {{width}} --height {{100}} {{filename}}`

- 将刚拍摄的图像复制到剪贴板：

`wacaw --to-clipboard`

- 列出可用的设备：

`wacaw --list-devices`