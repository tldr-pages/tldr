# apkleaks

> 从 APK 文件中暴露 URI、端点和密钥。
> 注意：APKLeaks 使用 `jadx` 反编译器来反编译 APK 文件。
> 更多信息：<https://github.com/dwisiswant0/apkleaks>.

- 扫描一个 APK 文件以查找 URI、端点和密钥：

`apkleaks {{[-f|--file]}} {{路径/到/文件.apk}}`

- 扫描并将输出保存到指定文件：

`apkleaks {{[-f|--file]}} {{路径/到/文件.apk}} {{[-o|--output]}} {{路径/到/输出.txt}}`

- 传递 `jadx` 反编译器参数：

`apkleaks {{[-f|--file]}} {{路径/到/文件.apk}} {{[-a|--args]}} "{{--threads-count 5 --deobf}}"`
