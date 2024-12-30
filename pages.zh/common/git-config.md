# git 配置

> 管理 Git 仓库的自定义配置选项。
> 这些配置可以是本地的（针对当前仓库）或全局的（针对当前用户）。
> 更多信息：<https://git-scm.com/docs/git-config>。

- 全局设置您的姓名或电子邮件（此信息是提交到仓库所必需的，并将包含在所有提交中）：

`git config --global {{user.name|user.email}} "{{您的姓名|email@example.com}}"`

- 列出本地或全局配置条目：

`git config --list --{{local|global}}`

- 仅列出系统配置条目（存储在 `/etc/gitconfig` 中），并显示其文件位置：

`git config --list --system --show-origin`

- 获取给定配置条目的值：

`git config alias.unstage`

- 设置给定配置条目的全局值：

`git config --global alias.unstage "reset HEAD --"`

- 将全局配置条目恢复为其默认值：

`git config --global --unset alias.unstage`

- 在默认编辑器中编辑本地 Git 配置（`.git/config`）：

`git config --edit`

- 在默认编辑器中编辑全局 Git 配置（默认是 `~/.gitconfig`，如果存在这样的文件则是 `$XDG_CONFIG_HOME/git/config`）：

`git config --global --edit`