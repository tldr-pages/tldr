# apkleaks

> 暴露 APK 文件中的 URI、端点和秘密。
> 注意：APKLeaks 使用 `jadx` 反编译器来反编译 APK 文件。
> 更多信息：<https://github.com/dwisiswant0/apkleaks>.

- 扫描 APK 文件中的 URI、端点和秘密：

`apkleaks {{[-f|--file]}} {{path/to/file.apk}}`

- 扫描并将输出保存到指定文件：

`apkleaks {{[-f|--file]}} {{path/to/file.apk}} {{[-o|--output]}} {{path/to/output.txt}}`

- 传递 `jadx` 反编译器参数：

`apkleaks {{[-f|--file]}} {{path/to/file.apk}} {{[-a|--args]}} "{{--threads-count 5 --deobf}}"`
