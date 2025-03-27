# git archive

> 从代码树创建文件归档。
> 更多信息： <https://git-scm.com/docs/git-archive>.

- 从当前 HEAD 内容创建 tar 归档并输出到标准输出：

`git archive {{[-v|--verbose]}} HEAD`

- 使用 Zip 格式并显示详细进度：

`git archive {{[-v|--verbose]}} --format zip HEAD`

- 将 Zip 归档输出到指定文件：

`git archive {{[-v|--verbose]}} {{[-o|--output]}} {{path/to/file.zip}} HEAD`

- 从指定分支的最新提交内容创建 tar 归档：

`git archive {{[-o|--output]}} {{path/to/file.tar}} {{branch_name}}`

- 使用特定目录的内容创建归档：

`git archive {{[-o|--output]}} {{path/to/file.tar}} HEAD:{{path/to/directory}}`

- 为归档中的每个文件添加前缀路径：

`git archive {{[-o|--output]}} {{path/to/file.tar}} --prefix {{path/to/prepend}}/ HEAD`
