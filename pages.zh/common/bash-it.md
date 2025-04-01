# bash-it

> 一个为 Bash 3.2+ 提供的社区贡献的 Bash 命令和脚本集合。
> 更多信息：<https://bash-it.readthedocs.io/en/latest/>.

- 将 Bash-it 更新到最新的稳定版/开发版：

`bash-it update {{stable|dev}}`

- 重新加载 Bash 配置文件（将 `BASH_IT_AUTOMATIC_RELOAD_AFTER_CONFIG_CHANGE` 设置为非空值以自动重新加载）：

`bash-it reload`

- 重启 Bash：

`bash-it restart`

- 重新加载 Bash 配置文件并启用错误和警告日志：

`bash-it doctor`

- 重新加载 Bash 配置文件并启用错误/警告/全部日志：

`bash-it doctor {{errors|warnings|all}}`

- 搜索 Bash-it 别名/插件/补全：

`bash-it search {{alias|plugin|completion}}`

- 搜索 Bash-it 别名/插件/补全并启用/禁用所有找到的项目：

`bash-it search --{{enable|disable}} {{alias|plugin|completion}}`
