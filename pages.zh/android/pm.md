# pm

> 显示有关 Android 设备上应用程序的信息。
> 更多信息：<https://developer.android.com/tools/adb#pm>。

- 列出所有已安装的应用程序：

`pm list packages`

- 列出所有已安装的 [s]ystem 应用程序：

`pm list packages -s`

- 列出所有已安装的 [3]rd-party 应用程序：

`pm list packages -3`

- 列出匹配特定关键字的应用程序：

`pm list packages {{关键字1 关键字2 ...}}`

- 显示特定应用程序的 APK 路径：

`pm path {{应用程序}}`