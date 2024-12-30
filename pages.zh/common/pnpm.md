# pnpm

> 快速、高效的 Node.js 包管理器。
> 管理 Node.js 项目及其模块依赖。
> 更多信息：<https://pnpm.io>。

- 创建一个 `package.json` 文件：

`pnpm init`

- 下载 `package.json` 中列出的所有依赖包：

`pnpm install`

- 下载特定版本的包并将其添加到 `package.json` 的依赖列表中：

`pnpm add {{module_name}}@{{version}}`

- 下载一个包并将其添加到 `package.json` 的 [D]ev 依赖列表中：

`pnpm add -D {{module_name}}`

- 下载一个包并全局安装：

`pnpm add -g {{module_name}}`

- 卸载一个包并将其从 `package.json` 的依赖列表中移除：

`pnpm remove {{module_name}}`

- 打印本地安装模块的树形结构：

`pnpm list`

- 列出顶级 [g]lobally 安装的模块：

`pnpm list -g --depth={{0}}`