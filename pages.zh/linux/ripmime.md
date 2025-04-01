# ripmime

> 从 MIME 编码的邮件包中提取附件。
> 更多信息：<https://pldaniels.com/ripmime>.

- 在当前目录中提取文件内容：

`ripmime -i {{path/to/file}}`

- 在指定目录中提取文件内容：

`ripmime -i {{path/to/file}} -d {{path/to/directory}}`

- 提取文件内容并打印详细输出：

`ripmime -i {{path/to/file}} -v`

- 获取整个解码过程的详细信息：

`ripmime -i {{path/to/file}} --debug`
