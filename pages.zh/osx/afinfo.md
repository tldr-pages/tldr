# afinfo

> OS X 的音频文件元数据解析器。
> OS X 的内置命令。
> 更多信息：<https://keith.github.io/xcode-man-pages/afinfo.1.html>。

- 显示给定音频文件的信息：

`afinfo {{path/to/file}}`

- 打印音频文件的一行描述：

`afinfo --brief {{path/to/file}}`

- 打印音频文件的元数据和 InfoDictionary 的内容：

`afinfo --info {{path/to/file}}`

- 以 XML 格式打印输出：

`afinfo --xml {{path/to/file}}`

- 如果音频文件有任何警告，则打印警告：

`afinfo --warnings {{path/to/file}}`

- 显示帮助信息：

`afinfo --help`