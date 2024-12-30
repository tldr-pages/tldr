# apkleaks

> 从APK文件中暴露URI、端点和密钥。
> 注意：APKLeaks利用`jadx`反汇编器来反编译APK文件。
> 更多信息：<https://github.com/dwisiswant0/apkleaks>。

- 扫描APK [f]ile以查找URI、端点和密钥：

`apkleaks --file {{path/to/file.apk}}`

- 扫描并将 [o]utput保存到特定文件：

`apkleaks --file {{path/to/file.apk}} --output {{path/to/output.txt}}`

- 传递`jadx`反汇编器的 [a]rguments：

`apkleaks --file {{path/to/file.apk}} --args "{{--threads-count 5 --deobf}}"`