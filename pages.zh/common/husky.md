# husky

> 使 Git 钩子更加简单。
> 更多信息：<https://typicode.github.io/husky>.

- 在当前目录安装 Husky:

`husky install`

- 在指定目录安装 Husky:

`husky install {{path/to/directory}}`

- 设置一个特定的命令作为 Git 的 `pre-push` 钩子:

`husky set {{.husky/pre-push}} "{{command}} {{command_arguments}}"`

- 将特定命令添加到当前的 `pre-commit` 钩子中:

`husky add {{.husky/pre-commit}} "{{command}} {{command_arguments}}"`

- 从当前目录卸载 Husky 钩子:

`husky uninstall`

- 显示帮助信息:

`husky`