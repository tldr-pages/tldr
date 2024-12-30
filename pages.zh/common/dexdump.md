# dexdump

> 显示有关 Android DEX 文件的信息。
> 更多信息：<https://manned.org/dexdump>。

- 从 APK 文件中提取类和方法：

`dexdump {{path/to/file.apk}}`

- 显示 APK 文件中包含的 DEX 文件的头信息：

`dexdump -f {{path/to/file.apk}}`

- 显示可执行部分的反汇编输出：

`dexdump -d {{path/to/file.apk}}`

- 将结果输出到文件：

`dexdump -o {{path/to/file}} {{path/to/file.apk}}`