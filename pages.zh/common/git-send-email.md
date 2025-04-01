# git send-email

> 将一系列补丁作为电子邮件发送。
> 补丁可以指定为文件、方向或版本列表。
> 更多信息：<https://git-scm.com/docs/git-send-email>。

- 以交互方式发送当前分支的最后一个提交：

`git send-email -1`

- 发送指定的提交：

`git send-email -1 {{commit}}`

- 发送当前分支中的多个（例如10个）提交：

`git send-email {{-10}}`

- 为补丁系列发送介绍邮件：

`git send-email -{{提交数量}} --compose`

- 查看并编辑即将发送的每个补丁的邮件内容：

`git send-email -{{提交数量}} --annotate`
