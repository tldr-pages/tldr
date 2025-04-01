# emulator

> 管理 Android 模拟器。
> 更多信息：<https://developer.android.com/studio/run/emulator-commandline>.

- 启动一个 Android 模拟器设备：

`emulator -avd {{name}}`

- 显示开发计算机上可用于模拟的摄像头：

`emulator -avd {{name}} -webcam-list`

- 启动模拟器并覆盖后置摄像头设置（使用 `-camera-front` 覆盖前置摄像头）：

`emulator -avd {{name}} -camera-back {{none|emulated|webcamN}}`

- 启动带有最大网络速度的模拟器：

`emulator -avd {{name}} -netspeed {{gsm|hscsd|gprs|edge|hsdpa|lte|evdo|full}}`

- 启动带有网络延迟的模拟器：

`emulator -avd {{name}} -netdelay {{gsm|hscsd|gprs|edge|hsdpa|lte|evdo|none}}`

- 启动模拟器，通过指定的 HTTP/HTTPS 代理进行所有 TCP 连接（需要端口号）：

`emulator -avd {{name}} -http-proxy {{http://example.com:80}}`

- 启动带有指定 SD 卡分区映像文件的模拟器：

`emulator -avd {{name}} -sdcard {{path/to/sdcard.img}}`

- 显示帮助：

`emulator -help`
