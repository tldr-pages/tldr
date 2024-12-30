# git describe

> 为一个对象根据可用的引用生成一个可读的名称。
> 更多信息：<https://git-scm.com/docs/git-describe>。

- 为当前提交创建一个唯一的名称（名称包含最近的注释标签、附加提交的数量，以及简短的提交哈希）：

`git describe`

- 为简短的提交哈希创建一个包含4位数字的名称：

`git describe --abbrev={{4}}`

- 生成一个带有标签引用路径的名称：

`git describe --all`

- 描述一个Git标签：

`git describe {{v1.0.0}}`

- 为给定分支的最后一次提交创建一个名称：

`git describe {{branch_name}}`