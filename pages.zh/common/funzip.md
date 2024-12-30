# funzip

> 打印归档文件中第一个（非目录）成员的内容而不进行提取。
> 更多信息：<https://manned.org/funzip>。

- 打印 Zip 归档文件中第一个成员的内容：

`funzip {{path/to/archive.zip}}`

- 打印 gzip 归档文件中的内容：

`funzip {{path/to/archive.gz}}`

- 解密 Zip 或 gzip 归档文件并打印内容：

`funzip -password {{password}} {{path/to/archive}}`