# in-toto-record

> 创建一个签名的链接元数据文件，为供应链步骤提供证据。
> 更多信息：<https://in-toto.readthedocs.io/en/latest/command-line-tools/in-toto-record.html>.

- 开始记录（创建一个初步的链接文件）：

`in-toto-record start -n {{path/to/edit_file1 path/to/edit_file2 ...}} -k {{path/to/key_file}} -m {{.}}`

- 停止记录（需要一个初步的链接文件）：

`in-toto-record stop -n {{path/to/edit_file1 path/to/edit_file2 ...}} -k {{path/to/key_file}} -p {{.}}`
