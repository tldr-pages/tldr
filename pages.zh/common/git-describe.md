# git describe

> 基于可用的引用，为对象提供一个人类可读的名字。
> 更多信息：<https://git-scm.com/docs/git-describe>.

- 为当前提交创建一个唯一名称（该名称包含最近的带注解标签、额外的提交数量和简短的提交哈希）：

`git describe`

- 创建一个包含4位简短提交哈希的名称：

`git describe --abbrev={{4}}`

- 生成包含标签引用路径的名称：

`git describe --all`

- 描述一个Git标签：

`git describe {{v1.0.0}}`

- 为指定分支的最后一个提交创建名称：

`git describe {{branch_name}}`