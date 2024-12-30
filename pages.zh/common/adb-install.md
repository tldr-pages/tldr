# adb 安装

> 将软件包推送到连接的 Android 设备或模拟器。
> 更多信息：<https://developer.android.com/tools/adb>。

- 将 Android 应用程序推送到模拟器/设备：

`adb install {{path/to/file.apk}}`

- 将 Android 应用程序推送到特定的模拟器/设备（覆盖 `$ANDROID_SERIAL`）：

`adb -s {{serial_number}} install {{path/to/file.apk}}`

- [r]einstall 现有应用，保留其数据：

`adb install -r {{path/to/file.apk}}`

- 推送 Android 应用程序，允许版本代码 [d]owngrade（仅限可调试包）：

`adb install -d {{path/to/file.apk}}`

- [g]rant 应用清单中列出的所有权限：

`adb install -g {{path/to/file.apk}}`

- 通过只更新更改的 APK 部分快速更新已安装的包：

`adb install --fastdeploy {{path/to/file.apk}}`