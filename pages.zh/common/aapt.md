# aapt

> 安卓资源包工具（Android Asset Packaging Tools）。
> 该工具可以查看，创建，更新资源压缩包（zip, jar, apk）。
> 更多信息：<https://elinux.org/Android_aapt>.

- 列出资源压缩包里的内容：

`aapt list {{路径/到/应用.apk}}`

- 查看 APK 包内指定的内容（版本，权限许可等）：

`aapt dump badging {{路径/到/应用.apk}}`

- 打包生成资源压缩包：

`aapt package -F {{路径/到/应用.apk}} {{路径/到/目录}}`
