# 模拟器

> 管理 Android 模拟器。
> 更多信息：<https://developer.android.com/studio/run/emulator-commandline>。

- 启动 Android 模拟器设备：

`emulator -avd {{name}}`

- 显示您开发计算机上可用于模拟的网络摄像头：

`emulator -avd {{name}} -webcam-list`

- 启动一个模拟器，覆盖背面摄像头设置（使用 `-camera-front` 以使用前置摄像头）：

`emulator -avd {{name}} -camera-back {{none|emulated|webcamN}}`

- 启动一个模拟器，设置最大网络速度：

`emulator -avd {{name}} -netspeed {{gsm|hscsd|gprs|edge|hsdpa|lte|evdo|full}}`

- 启动一个模拟器，设置网络延迟：

`emulator -avd {{name}} -netdelay {{gsm|hscsd|gprs|edge|hsdpa|lte|evdo|none}}`

- 启动一个模拟器，使所有 TCP 连接通过指定的 HTTP/HTTPS 代理（需要端口号）：

`emulator -avd {{name}} -http-proxy {{http://example.com:80}}`

- 启动一个模拟器，并指定 SD 卡分区映像文件：

`emulator -avd {{name}} -sdcard {{path/to/sdcard.img}}`

- 显示帮助信息：

`emulator -help`