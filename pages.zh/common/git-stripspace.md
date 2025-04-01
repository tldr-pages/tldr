# git stripspace

> 从标准输入读取文本（例如提交信息、注释、标签和分支描述）并清理为 Git 使用的格式。
> 更多信息：<https://git-scm.com/docs/git-stripspace>.

- 去除文件中的空白字符：

`cat {{path/to/file}} | git stripspace`

- 去除文件中的空白字符和 Git 注释：

`cat {{path/to/file}} | git stripspace --strip-comments`

- 将文件中的所有行转换为 Git 注释：

`git stripspace --comment-lines < {{path/to/file}}`
