# git gui

> 一个 Git 的图形界面工具，用于管理分支、提交和远程仓库，并执行本地合并。
> 其他相关工具：`git-cola`, `gitk`。
> 更多信息：<https://git-scm.com/docs/git-gui>。

- 启动图形界面：

`git gui`

- 显示特定文件，每行包含作者名称和提交哈希：

`git gui blame {{path/to/file}}`

- 在特定修订版本中打开 `git gui blame`：

`git gui blame {{revision}} {{path/to/file}}`

- 打开 `git gui blame` 并将视图滚动到指定行的中间：

`git gui blame --line={{line}} {{path/to/file}}`

- 打开一个窗口进行一次提交，完成后返回到 shell：

`git gui citool`

- 以“修改最后一个提交”模式打开 `git gui citool`：

`git gui citool --amend`

- 以只读模式打开 `git gui citool`：

`git gui citool --nocommit`

- 显示特定分支的树形浏览器，并在点击文件时打开 blame 工具：

`git gui browser maint`