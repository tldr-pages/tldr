# in-toto-record

> 创建一个签名链接元数据文件，以提供供应链步骤的证据。
> 更多信息：<https://in-toto.readthedocs.io/en/latest/command-line-tools/in-toto-record.html>。

- 开始记录（创建一个初步链接文件）：

`in-toto-record start -n {{path/to/edit_file1 path/to/edit_file2 ...}} -k {{path/to/key_file}} -m {{.}}`

- 停止记录（期待一个初步链接文件）：

`in-toto-record stop -n {{path/to/edit_file1 path/to/edit_file2 ...}} -k {{path/to/key_file}} -p {{.}}`