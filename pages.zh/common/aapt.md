# aapt

> 安卓资源包工具（Android Asset Packaging Tools）.
> 该工具可以查看，创建， 更新资源压缩包(zip, jar, apk)。

- 列出资源压缩包里的内容:

`aapt l[ist] {{path/to/app.apk}}`

- 查看APK包内指定的内容 (版本, 权限许可等):

`aapt d[ump] badging {{path/to/app.apk}}`

- 打包生成资源压缩包:

`aapt p[ackage] -F {{path/to/app.apk}} {{path/to/directory}}`

- 从压缩包中删除指定文件:

<<<<<<< HEAD
`aapt r[emove] {{path/to/app.apk}} {{path/to/filename}}`
=======
`aapt r[emove] {{path/to/app.apk}} {{path/to/filename}}`
>>>>>>> b9ef5e1830c9b2dd9f23d4dcad97608d3ccf1ac5
