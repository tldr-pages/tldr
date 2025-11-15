# zipalign

> Zip 文件对齐工具。
> 是 Android 软件开发工具包构建工具的一部分。
> 更多信息：<https://developer.android.com/tools/zipalign>.

- 在 4 字节边界上对齐一个 Zip 文件的数据：

`zipalign {{4}} {{路径/到/输入.zip}} {{路径/到/输出.zip}}`

- 检查一个 Zip 文件是否在 4 字节边界上正确对齐，并以详细的方式显示结果：

`zipalign -v -c {{4}} {{路径/到/输入.zip}}`
