# git archive

> 从树中创建文件的归档。
> 更多信息：<https://git-scm.com/docs/git-archive>。

- 从当前 HEAD 的内容创建 tar 归档并输出到 `stdout`：

`git archive {{[-v|--verbose]}} HEAD`

- 使用 Zip 格式并详细报告进度：

`git archive {{[-v|--verbose]}} --format zip HEAD`

- 将 Zip 归档输出到特定文件：

`git archive {{[-v|--verbose]}} {{[-o|--output]}} {{path/to/file.zip}} HEAD`

- 从特定分支的最新提交内容创建 tar 归档：

`git archive {{[-o|--output]}} {{path/to/file.tar}} {{branch_name}}`

- 使用特定目录的内容：

`git archive {{[-o|--output]}} {{path/to/file.tar}} HEAD:{{path/to/directory}}`

- 为每个文件添加路径前缀，以将归档文件存储在特定目录中：

`git archive {{[-o|--output]}} {{path/to/file.tar}} --prefix {{path/to/prepend}}/ HEAD`
