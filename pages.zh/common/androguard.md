# androguard

> 反向工程 Android 应用程序。用 Python 编写。
> 更多信息: <https://github.com/androguard/androguard>。

- 显示 Android 应用清单：

`androguard axml {{path/to/app.apk}}`

- 显示应用元数据（版本和应用 ID）：

`androguard apkid {{path/to/app.apk}}`

- 反编译应用的 Java 代码：

`androguard decompile {{path/to/app.apk}} --output {{path/to/directory}}`