# bob

> 管理和切换 Neovim 版本。
> 更多信息：<https://github.com/MordechaiHadad/bob>。

- 安装并切换到指定版本的 Neovim：

`bob use {{nightly|stable|latest|version_string|commit_hash}}`

- 列出已安装和当前使用的 Neovim 版本：

`bob list`

- 卸载指定版本的 Neovim：

`bob uninstall {{nightly|stable|latest|version_string|commit_hash}}`

- 卸载 Neovim 并删除 `bob` 所做的任何更改：

`bob erase`

- 回滚到之前的夜间版本：

`bob rollback`