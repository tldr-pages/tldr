# wacaw

> 一个用于 macOS 的小命令行工具，允许您从连接的摄像头捕获静止图片和视频。
> 更多信息：<http://webcam-tools.sourceforge.net>.

- 从网络摄像机拍照：

`wacaw {{文件名}}`

- 录制视频：

`wacaw --video {{文件名}} -D {{录制多少秒}}`

- 用自定义分辨率拍照：

`wacaw -x {{宽}} -y {{高}} {{文件名}}`

- 将刚拍摄的图像复制到剪贴板：

`wacaw --to-clipboard`

- 可用设备列表：

`wacaw -L`
