# scrcpy

> 在桌面上显示和控制您的 Android 设备。
> 更多信息：<https://github.com/Genymobile/scrcpy>.

- 显示连接设备的镜像：

`scrcpy`

- 根据设备的 ID 或 IP 地址显示特定设备的镜像（设备 ID 可通过 `adb devices` 命令获得）：

`scrcpy --serial {{0123456789abcdef|192.168.0.1:5555}}`

- 以全屏模式启动显示：

`scrcpy --fullscreen`

- 旋转显示屏幕。每个增量值增加 90 度逆时针旋转：

`scrcpy --rotation {{0|1|2|3}}`

- 显示物理设备上的触摸：

`scrcpy --show-touches`

- 录制显示屏幕：

`scrcpy --record {{path/to/file.mp4}}`

- 指定通过拖放推送到设备的目标目录（非 APK 文件）：

`scrcpy --push-target {{path/to/directory}}`