# rbt

> RBTools 是一组用于与 Review Board 和 RBCommons 交互的命令行工具。
> 更多信息：<https://www.reviewboard.org/docs/rbtools/dev/>.

- 将更改发布到 Review Board：

`rbt post {{change_number}}`

- 显示将发送到 Review Board 的差异：

`rbt diff`

- 在本地分支或审查请求中应用更改：

`rbt land {{branch_name}}`

- 使用审查请求中的更改补丁你的工作树：

`rbt patch {{review_request_id}}`

- 设置 RBTool 以与仓库通信：

`rbt setup-repo`
