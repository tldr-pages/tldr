# git update-ref

> 用于创建、更新和删除 Git 引用的 Git 命令。
> 更多信息：<https://git-scm.com/docs/git-update-ref>.

- 删除引用，对于软重置第一个提交很有用：

`git update-ref -d {{HEAD}}`

- 带有消息更新引用：

`git update-ref -m {{message}} {{HEAD}} {{4e95e05}}`