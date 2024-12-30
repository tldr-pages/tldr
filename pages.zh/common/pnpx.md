# pnpx

> 直接执行来自 npm 包的二进制文件，使用 `pnpm` 而不是 `npm`。
> 注意：此命令已被弃用！请改用 `pnpm exec` 和 `pnpm dlx`。
> 更多信息：<https://cuyl.github.io/pnpm.github.io/pnpx-cli>。

- 从给定的 `npm` 模块执行二进制文件：

`pnpx {{module_name}}`

- 从给定的 `npm` 模块执行特定的二进制文件，以防该模块有多个二进制文件：

`pnpx --package {{package_name}} {{module_name}}`

- 显示帮助信息：

`pnpx --help`