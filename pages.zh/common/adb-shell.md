# adb shell

> Android Debug Bridge Shell: 运行安卓模拟器或者连接设备上的远程shell指令。
> 详见: <https://developer.android.com/studio/command-line/adb>.

- 启动模拟器/设备上的远程终端:

`adb shell`

- 获取设备全部属性:

`adb shell getprop`

- 查看进程列表

`adb shell ps`

- 查看指定进程状态

`adb shell ps -x {{PID}}`

- 查看后台services信息

`adb shell service list`

- 查看IO内存分区

`adb shell cat /proc/iomem`

- 文件操作---如-查看所有存储设备名

`adb shell ls mnt`

- 额外的 可以进行任意的文件操作（ls、cd、rm、 rename、 mv、 chmod、 mkdir等）
