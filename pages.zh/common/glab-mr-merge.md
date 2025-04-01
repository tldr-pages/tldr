# glab mr merge

> 合并 GitLab 合并请求。
> 更多信息：<https://glab.readthedocs.io/en/latest/mr/merge.html>.

- 交互式合并当前分支关联的合并请求：

`glab mr merge`

- 交互式合并指定的合并请求：

`glab mr merge {{mr_number}}`

- 合并合并请求，并在本地和远程删除源分支：

`glab mr merge --remove-source-branch`

- 将当前合并请求压缩为一个提交，并包含提交消息体后合并：

`glab mr merge --squash --message="{{commit_message_body}}"`

- 显示帮助：

`glab mr merge --help`
