# git log

> 查看提交历史。
> 更多信息：<https://git-scm.com/docs/git-log>.

- 按时间先后顺序列出当前仓库所有的提交，最近的更新排在最上面：

`git log`

- 查看指定文件或指定目录的历史，包括每次提交所引入的差异：

`git log -p {{路径/到/文件或目录}}`

- 显示每次提交的文件修改统计信息：

`git log --stat`

- 在日志旁以 ASCII 图形显示当前分支提交历史，并只展示提交消息的第一行：

`git log --oneline --graph`

- 在日志旁以 ASCII 图形显示整个仓库的所有提交、标签、分支：

`git log --oneline --decorate --all --graph`

- 查看提交消息中包含特定字符串（大小写敏感）的提交：

`git log -i --grep {{字符串}}`

- 查看特定作者的最近 N 条提交：

`git log -n {{数字}} --author={{作者}}`

- 查看两个日期之间的提交（yyyy-mm-dd）：

`git log --before="{{2017-01-29}}" --after="{{2017-01-17}}"`
