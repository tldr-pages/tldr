# funzip

> 打印存档中的第一个（非目录）成员的内容，而不进行解压。
> 更多信息：<https://manned.org/funzip>.

- 打印 Zip 存档中的第一个成员的内容：

`funzip {{path/to/archive.zip}}`

- 打印 gzip 存档中的内容：

`funzip {{path/to/archive.gz}}`

- 解密 Zip 或 gzip 存档并打印内容：

`funzip -password {{password}} {{path/to/archive}}`
