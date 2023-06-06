# git config

> 管理 Git 仓库的自定义设置项。
> 这些设置可以分为局部设置（只对当前仓库生效）和全局设置（对当前用户生效）。
> 更多信息：<https://git-scm.com/docs/git-config>.

- 列出局部设置项（存储在当前仓库的 `.git/config`）：

`git config --list --local`

- 列出全局配置项（存储在 `~/.gitconfig`）：

`git config --list --global`

- 列出系统配置项（存储在 `/etc/gitconfig`），并且展示文件的位置：

`git config --list --system --show-origin`

- 获取某个配置项的值：

`git config alias.unstage`

- 设置某个全局配置项：

`git config --global alias.unstage "reset HEAD --"`

- 将某个全局配置项恢复为默认值：

`git config --global --unset alias.unstage`

- 使用默认编辑器修改本地设置：

`git config --edit`

- 使用默认编辑器修改全局设置：

`git config --global --edit`
