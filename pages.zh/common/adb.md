# adb

> Android 调试桥：与 Android 模拟器实例或连接的 Android 设备进行通信。
> 一些子命令如 `shell` 有其自己的使用文档。
> 更多信息：<https://developer.android.com/tools/adb>。

- 检查 adb 服务器进程是否在运行并启动它：

`adb start-server`

- 终止 adb 服务器进程：

`adb kill-server`

- 在目标模拟器/设备实例中启动远程 shell：

`adb shell`

- 将 Android 应用程序推送到模拟器/设备：

`adb install -r {{path/to/file.apk}}`

- 从目标设备复制文件/目录：

`adb pull {{path/to/device_file_or_directory}} {{path/to/local_destination_directory}}`

- 将文件/目录复制到目标设备：

`adb push {{path/to/local_file_or_directory}} {{path/to/device_destination_directory}}`

- 列出所有连接的设备：

`adb devices`

- 如果有多个设备，请指定要发送命令的设备：

`adb -s {{device_ID}} {{shell}}`