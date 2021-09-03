# adb

> 安卓调试桥：与 Android 模拟器或已连接的 Android 设备通信。
> 此命令也有关于其子命令的文件，例如：`adb shell`.
> 更多信息：<https://developer.android.com/studio/command-line/adb>.

- 检查 adb server 进程的是否在运行，并开启它：

`adb start-server`

- 终止 adb server 进程：

`adb kill-server`

- 在目标模拟器 / 设备实例上开启一个远程 shell:

`adb shell`

- 将 Android 应用程序推送到模拟器 / 设备 :

`adb install -r {{路径/到/应用.apk}}`

- 从目标设备上拷贝一个文件 / 目录到本地：

`adb pull {{路径/到/设备的文件或目录}} {{路径/到/本地上的目录}}`

- 从本地拷贝一个文件 / 目录到目标设备：

`adb push {{路径/到/本地文件或目录}} {{路径/到/设备上的目录}}`

- 列出已连接的设备：

`adb devices`
