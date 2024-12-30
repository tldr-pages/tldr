# pnpm 过时

> 检查过时的包。
> 可以通过提供参数限制检查已安装包的子集（支持模式）。
> 更多信息：<https://pnpm.io/cli/outdated>。

- 检查过时的包：

`pnpm outdated`

- 检查每个工作区包中发现的过时依赖：

`pnpm outdated -r`

- 使用包选择器过滤过时的包：

`pnpm outdated --filter {{package_selector}}`

- 列出[全局]过时的包：

`pnpm outdated --global`

- 打印过时包的详细信息：

`pnpm outdated --long`

- 以特定格式打印过时的依赖：

`pnpm outdated --format {{format}}`

- 仅打印满足 `package.json` 中规范的版本：

`pnpm outdated --compatible`

- 仅检查过时的[D]ev依赖：

`pnpm outdated --dev`