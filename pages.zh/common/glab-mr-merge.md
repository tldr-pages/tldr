# glab mr merge

> 合并 GitLab 合并请求。
> 更多信息: <https://glab.readthedocs.io/en/latest/mr/merge.html>。

- 交互式合并与当前分支相关的合并请求：

`glab mr merge`

- 交互式合并指定的合并请求：

`glab mr merge {{mr_number}}`

- 合并合并请求，同时在本地和远程删除分支：

`glab mr merge --remove-source-branch`

- 将当前合并请求压缩为一个提交，并带上消息体进行合并：

`glab mr merge --squash --message="{{commit_message_body}}"`

- 显示帮助信息：

`glab mr merge --help`