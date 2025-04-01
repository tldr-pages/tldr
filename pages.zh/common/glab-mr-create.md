# glab mr create

> 管理 GitLab 合并请求。
> 更多信息：<https://glab.readthedocs.io/en/latest/mr/create.html>。

- 交互式创建合并请求：

`glab mr create`

- 创建合并请求，从当前分支的提交消息中确定标题和描述：

`glab mr create --fill`

- 创建草稿合并请求：

`glab mr create --draft`

- 创建合并请求，指定目标分支、标题和描述：

`glab mr create --target-branch {{target_branch}} --title "{{title}}" --description "{{description}}"`

- 在默认网页浏览器中打开合并请求：

`glab mr create --web`
