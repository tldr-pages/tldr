# bob

> 管理和切换 Neovim 版本。
> 更多信息：<https://github.com/MordechaiHadad/bob>.

- 安装并切换到指定的 Neovim 版本：

`bob use {{nightly|stable|latest|version_string|commit_hash}}`

- 列出已安装和当前使用的 Neovim 版本：

`bob list`

- 卸载指定的 Neovim 版本：

`bob uninstall {{nightly|stable|latest|version_string|commit_hash}}`

- 卸载 Neovim 并清除 `bob` 做出的所有更改：

`bob erase`

- 回滚到之前的 nightly 版本：

`bob rollback`
