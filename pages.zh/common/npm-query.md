# npm 查询

> 使用类似 CSS 的选择器打印依赖对象数组。
> 更多信息：<https://docs.npmjs.com/cli/commands/npm-query>。

- 打印直接依赖：

`npm query ':root > *'`

- 打印所有直接的生产/开发依赖：

`npm query ':root > .{{prod|dev}}'`

- 打印具有特定名称的依赖：

`npm query '#{{package}}'`

- 打印具有特定名称并在语义版本范围内的依赖：

`npm query '#{{package}}@{{semantic_version}}'`

- 打印没有依赖的依赖：

`npm query ':empty'`

- 查找所有具有 postinstall 脚本的依赖并卸载它们：

`npm query ":attr(scripts, [postinstall])" | jq 'map(.name) | join("\n")' -r | xargs -I {} npm uninstall {}`

- 查找所有 Git 依赖并打印哪个应用程序需要它们：

`npm query ":type(git)" | jq 'map(.name)' | xargs -I {} npm why {}`