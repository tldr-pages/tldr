# git gui

> Git 的图形用户界面，用于管理分支、提交和远程仓库，并执行本地合并。
> 另请参见：`git-cola`，`gitk`。
> 更多信息：<https://git-scm.com/docs/git-gui>。

- 启动 GUI：

`git gui`

- 显示特定文件，每行显示作者名称和提交哈希：

`git gui blame {{path/to/file}}`

- 在特定修订版本中打开 `git gui blame`：

`git gui blame {{revision}} {{path/to/file}}`

- 打开 `git gui blame` 并将视图滚动到居中显示特定行：

`git gui blame --line={{line}} {{path/to/file}}`

- 打开一个窗口以进行一次提交，并在完成后返回到命令行：

`git gui citool`

- 以“修改最后一次提交”模式打开 `git gui citool`：

`git gui citool --amend`

- 以只读模式打开 `git gui citool`：

`git gui citool --nocommit`

- 显示特定分支的树形结构浏览器，点击文件时打开 blame 工具：

`git gui browser maint`