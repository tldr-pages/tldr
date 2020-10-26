# aapt

> 安卓资源包工具（Android Asset Packaging Tools）.
> 该工具可以查看，创建， 更新资源压缩包(zip, jar, apk)。

- 列出资源压缩包里的内容:

`aapt l {{path/to/app.apk}}`

- 查看APK包内指定的内容 (版本, 权限许可等):

`aapt d badging {{path/to/app.apk}}`

- 打包生成资源压缩包:

`aapt p -F {{path/to/app.apk}} {{path/to/directory}}`

- 从压缩包中删除指定文件:

`aapt r {{path/to/app.apk}} {{path/to/filename}}`
