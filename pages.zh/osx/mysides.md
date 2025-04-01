# mysides

> 添加、列出和删除 Finder 收藏夹。
> 更多信息：<https://github.com/mosen/mysides>。

- 列出侧边栏收藏夹：

`mysides list`

- 在侧边栏收藏夹末尾添加新项目：

`mysides add {{example}} {{file:///Users/Shared/example}}`

- 通过名称删除项目：

`mysides remove {{example}}`

- 将当前目录添加到侧边栏：

`mysides add $(basename $(pwd)) file:///$(pwd)`

- 从侧边栏删除当前目录：

`mysides remove $(basename $(pwd))`