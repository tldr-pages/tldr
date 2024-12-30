# scrcpy

> 在桌面上显示和控制您的 Android 设备。
> 更多信息：<https://github.com/Genymobile/scrcpy>。

- 显示已连接设备的镜像：

`scrcpy`

- 根据设备的 ID 或 IP 地址显示特定设备的镜像（可以在 `adb devices` 命令下找到）：

`scrcpy --serial {{0123456789abcdef|192.168.0.1:5555}}`

- 以全屏模式开始显示：

`scrcpy --fullscreen`

- 旋转显示屏。每增加的值会使屏幕逆时针旋转 90 度：

`scrcpy --rotation {{0|1|2|3}}`

- 在物理设备上显示触摸操作：

`scrcpy --show-touches`

- 录制显示屏：

`scrcpy --record {{path/to/file.mp4}}`

- 指定推送文件到设备的目标目录（非 APK 文件），通过拖放方式：

`scrcpy --push-target {{path/to/directory}}`