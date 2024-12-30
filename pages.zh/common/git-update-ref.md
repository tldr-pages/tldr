# git update-ref

> Git 命令用于创建、更新和删除 Git refs。
> 更多信息：<https://git-scm.com/docs/git-update-ref>。

- 删除一个引用，适用于软重置第一次提交：

`git update-ref -d {{HEAD}}`

- 使用消息更新引用：

`git update-ref -m {{message}} {{HEAD}} {{4e95e05}}`