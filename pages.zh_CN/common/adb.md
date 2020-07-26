# adb

> Android 调试桥：与 Android 仿真器或已连接的 Android 设备进行通信

- 检查 adb 服务器进程是否正在运行并启动它:

`adb start-server`

- 终止 adb 服务器进程:

`adb kill-server`

- 在目标模拟器、设备实例中启动一个远程的 shell :

`adb shell`

- 将 Android 应用程序推送到模拟器／设备:

`adb install -r {{path/to/file.apk}}`

- 从目标设备复制一个文件／目录:

`adb pull {{path/to/device_file_or_folder}} {{path/to/local_destination_folder}}`

- 将文件／文件夹复制到目标设备:

`adb push {{path/to/local_file_or_folder}} {{path/to/device_destination_folder}}`

- 获取已连接设备的列表:

`adb devices`

