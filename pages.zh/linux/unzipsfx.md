# unzipsfx

> 通过在 Zip 文件前添加自解压缩存根来创建自解压缩的压缩二进制文件。
> 更多信息：<https://manned.org/unzipsfx>。

- 创建 Zip 压缩文件的自解压缩二进制文件：

`cat unzipsfx {{path/to/archive.zip}} > {{filename}} && chmod 755 {{filename}}`

- 在当前目录中提取自解压缩二进制文件：

`{{./path/to/binary)}}`

- 测试自解压缩二进制文件是否有错误：

`{{./path/to/binary)}} -t`

- 在不提取的情况下打印自解压缩二进制文件中某个文件的内容：

`{{./path/to/binary)}} -c {{path/to/filename}}`

- 打印自解压缩二进制文件中 Zip 压缩文件的注释：

`{{./path/to/binary)}} -z`