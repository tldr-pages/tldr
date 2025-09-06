# pm

> 显示关于 Android 设备上的应用程序的信息。
> 更多信息：<https://developer.android.com/tools/adb#pm>.

- 打印所有已安装应用程序的列表：

`pm list packages`

- 打印所有已安装的系统应用程序的列表：

`pm list packages -s`

- 打印所有已安装的第三方应用程序的列表：

`pm list packages -3`

- 打印与指定关键字匹配的应用程序列表：

`pm list packages {{关键词}}`

- 打印指定应用的 APK 的路径：

`pm path {{应用名}}`
