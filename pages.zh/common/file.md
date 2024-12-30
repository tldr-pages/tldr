# 文件

> 确定文件类型。
> 更多信息：<https://manned.org/file>。

- 给出指定文件类型的描述。对于没有文件扩展名的文件效果很好：

`file {{path/to/file}}`

- 查看压缩文件中的内容并确定内部文件类型：

`file -z {{foo.zip}}`

- 允许文件与特殊或设备文件一起工作：

`file -s {{path/to/file}}`

- 不要在第一个文件类型匹配处停止；继续直到文件末尾：

`file -k {{path/to/file}}`

- 确定文件的 MIME 编码类型：

`file -i {{path/to/file}}`