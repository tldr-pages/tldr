# pnpm outdated

> 检查过期的包。
> 通过提供参数（支持通配符），可以限制检查已安装包的子集。
> 更多信息：<https://pnpm.io/cli/outdated>。

- 检查过期的包：

`pnpm outdated`

- 检查每个工作区包中的过期依赖项：

`pnpm outdated {{[-r|--recursive]}}`

- 使用包选择器过滤过期的包：

`pnpm outdated --filter {{package_selector}}`

- 列出全局过期的包：

`pnpm outdated {{[-g|--global]}}`

- 打印过期包的详细信息：

`pnpm outdated --long`

- 以特定格式打印过期的依赖项：

`pnpm outdated --format {{format}}`

- 仅打印满足 `package.json` 中规格的版本：

`pnpm outdated --compatible`

- 仅检查过期的开发依赖项：

`pnpm outdated {{[-D|--dev]}}`