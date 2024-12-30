# aapt

> Android资源打包工具：编译和打包Android应用的资源。
> 更多信息：<https://manned.org/aapt>。

- 列出APK归档中包含的文件：

`aapt list {{path/to/app.apk}}`

- 显示应用的元数据（版本、权限等）：

`aapt dump badging {{path/to/app.apk}}`

- 从指定目录创建一个新的APK归档：

`aapt package -F {{path/to/app.apk}} {{path/to/directory}}`