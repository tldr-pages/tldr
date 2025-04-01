# unzipsfx

> 通过在 Zip 文件前添加自解压存根，创建自解压压缩二进制文件。
> 更多信息：<https://manned.org/unzipsfx>.

- 创建一个 Zip 存档的自解压二进制文件：

`cat unzipsfx {{path/to/archive.zip}} > {{filename}} && chmod 755 {{filename}}`

- 在当前目录中解压自解压二进制文件：

`{{./path/to/binary)}}`

- 测试自解压二进制文件是否有错误：

`{{./path/to/binary)}} -t`

- 不解压的情况下打印自解压二进制文件中的文件内容：

`{{./path/to/binary)}} -c {{path/to/filename}}`

- 打印自解压二进制文件中的 Zip 存档的注释：

`{{./path/to/binary)}} -z`