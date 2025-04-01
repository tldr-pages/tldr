# tig

> 基于 `ncurses` 的可配置 Git TUI。
> 参见：`gitui`、`git-gui`。
> 更多信息：<https://jonas.github.io/tig/doc/manual.html>。

- 从当前提交开始，以逆时间顺序显示提交序列：

`tig`

- 显示特定分支的历史记录：

`tig {{branch}}`

- 显示特定文件或目录的历史记录：

`tig {{path1 path2 ...}}`

- 显示两个引用（如分支或标签）之间的差异：

`tig {{base_ref}}..{{compared_ref}}`

- 显示所有分支和暂存区的提交：

`tig --all`

- 以暂存区视图启动，显示所有已保存的暂存区：

`tig stash`

- 在 TUI 中显示帮助：

`<h>`