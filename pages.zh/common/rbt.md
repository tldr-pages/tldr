# rbt

> RBTools 是一套用于与 Review Board 和 RBCommons 交互的命令行工具。
> 更多信息请访问：<https://www.reviewboard.org/docs/rbtools/dev/>。

- 将更改发布到 Review Board：

`rbt post {{change_number}}`

- 显示将发送到 Review Board 的差异：

`rbt diff`

- 在本地分支或审查请求上合并更改：

`rbt land {{branch_name}}`

- 用审查请求中的更改修补你的树：

`rbt patch {{review_request_id}}`

- 设置 RBTool 与一个代码库进行交互：

`rbt setup-repo`