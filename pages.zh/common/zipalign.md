# zipalign

> Zip 文件对齐工具。
> 是 Android SDK 构建工具的一部分。
> 更多信息：<https://developer.android.com/tools/zipalign>。

- 将 Zip 文件的数据对齐到 4 字节边界：

`zipalign {{4}} {{path/to/input.zip}} {{path/to/output.zip}}`

- 检查 Zip 文件是否正确对齐到 4 字节边界，并以详细方式显示结果：

`zipalign -v -c {{4}} {{path/to/input.zip}}`