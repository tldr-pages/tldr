# pnpx

> 直接执行 `npm` 包中的二进制文件，使用 `pnpm` 而不是 `npm`。
> 注意：此命令已弃用！请改用 `pnpm exec` 和 `pnpm dlx`。
> 更多信息：<https://cuyl.github.io/pnpm.github.io/pnpx-cli>。

- 执行来自指定 `npm` 模块的二进制文件：

`pnpx {{module_name}}`

- 如果模块包含多个二进制文件，执行指定的二进制文件：

`pnpx --package {{package_name}} {{module_name}}`

- 显示帮助：

`pnpx --help`
