# mysides

> 添加、列出和移除 Finder 收藏夹。
> 更多信息：<https://github.com/mosen/mysides>。

- 列出侧边栏收藏夹：

`mysides list`

- 将新项目添加到侧边栏收藏夹的末尾：

`mysides add {{example}} {{file:///Users/Shared/example}}`

- 按名称移除项目：

`mysides remove {{example}}`

- 将当前目录添加到侧边栏：

`mysides add $(basename $(pwd)) file:///$(pwd)`

- 从侧边栏移除当前目录：

`mysides remove $(basename $(pwd))`