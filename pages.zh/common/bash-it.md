# bash-it

> 一组社区贡献的 Bash 命令和脚本，适用于 Bash 3.2 及以上版本。
> 更多信息：<https://bash-it.readthedocs.io/en/latest/>.

- 更新 Bash-it 到最新的稳定/开发版本：

`bash-it update {{stable|dev}}`

- 重新加载 Bash 配置文件（将 `BASH_IT_AUTOMATIC_RELOAD_AFTER_CONFIG_CHANGE` 设置为非空值以实现自动重新加载）：

`bash-it reload`

- 重启 Bash：

`bash-it restart`

- 以启用错误和警告日志的方式重新加载 Bash 配置文件：

`bash-it doctor`

- 以启用错误/警告/全部日志的方式重新加载 Bash 配置文件：

`bash-it doctor {{errors|warnings|all}}`

- 搜索 Bash-it 别名/插件/补全：

`bash-it search {{alias|plugin|completion}}`

- 搜索 Bash-it 别名/插件/补全并启用/禁用所有找到的项目：

`bash-it search --{{enable|disable}} {{alias|plugin|completion}}`