# git send-email

> 作为电子邮件发送一组补丁。
> 补丁可以指定为文件、方向或修订列表。
> 更多信息：<https://git-scm.com/docs/git-send-email>。

- 交互式发送当前分支中的最后一次提交：

`git send-email -1`

- 发送给定的提交：

`git send-email -1 {{commit}}`

- 在当前分支中发送多个（例如 10）提交：

`git send-email {{-10}}`

- 为补丁系列发送一封介绍性电子邮件：

`git send-email -{{number_of_commits}} --compose`

- 审查和编辑即将发送的每个补丁的电子邮件消息：

`git send-email -{{number_of_commits}} --annotate`