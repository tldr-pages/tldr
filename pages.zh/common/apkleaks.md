# apkleaks

> 从 APK 文件中暴露 URI、端点和密钥。
> 注意：APKLeaks 利用 `jadx` 反汇编器来反编译 APK 文件。
> 更多信息：<https://github.com/dwisiswant0/apkleaks>。

- 扫描 APK 文件中的 URI、端点和密钥：

`apkleaks {{[-f|--file]}} {{路径/到/file}}.apk`

- 扫描并将输出保存到特定文件：

`apkleaks {{[-f|--file]}} {{路径/到/file}}.apk {{[-o|--output]}} {{路径/到/output.txt}}`

- 传递 `jadx` 反汇编器参数：

`apkleaks {{[-f|--file]}} {{路径/到/file}}.apk {{[-a|--args]}} "{{--threads-count 5 --deobf}}"`
