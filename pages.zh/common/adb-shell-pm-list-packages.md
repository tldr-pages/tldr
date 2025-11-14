# adb shell pm list packages

> 列出安卓设备上，已安装的，已知的或经过自定义筛选后的软件包。
> 更多信息：<https://developer.android.com/tools/adb>.

- 列出所有已安装的软件包：

`adb shell pm list packages`

- 列出所有软件包，以及与它们关联的 APK 文件的路径：

`adb shell pm list packages -f`

- 仅列出禁用的软件包：

`adb shell pm list packages -d`

- 仅列出启用的软件包：

`adb shell pm list packages -e`

- 仅列出系统软件包：

`adb shell pm list packages -s`

- 仅列出第三方（非系统）的软件包：

`adb shell pm list packages -3`

- 显示每个包的安装来源：

`adb shell pm list packages -i`
