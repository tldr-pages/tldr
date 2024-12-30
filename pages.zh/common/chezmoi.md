# Chezmoi

> 一个多机器的 dotfile 管理器，使用 Go 编写。
> 另见：`stow`，`tuckr`，`vcsh`，`homeshick`。
> 更多信息：<https://chezmoi.io>。

- 设置 `chezmoi`，在 `~/.local/share/chezmoi` 中创建一个 Git 仓库：

`chezmoi init`

- 从 Git 仓库的现有 dotfiles 设置 `chezmoi`：

`chezmoi init {{repository_url}}`

- 开始跟踪一个或多个 dotfiles：

`chezmoi add {{path/to/dotfile1 path/to/dotfile2 ...}}`

- 使用本地更改更新仓库：

`chezmoi re-add {{path/to/dotfile1 path/to/dotfile2 ...}}`

- 编辑已跟踪 dotfile 的源状态：

`chezmoi edit {{path/to/dotfile_or_symlink}}`

- 查看待处理的更改：

`chezmoi diff`

- 应用更改：

`chezmoi -v apply`

- 从远程仓库拉取更改并应用它们：

`chezmoi update`