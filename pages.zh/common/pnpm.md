# pnpm

> 快速、节省磁盘空间的 Node.js 包管理器。
> 管理 Node.js 项目及其模块依赖。
> 更多信息：<https://pnpm.io/pnpm-cli>。

- 创建一个 `package.json` 文件：

`pnpm init`

- 下载 `package.json` 中列出的所有依赖包：

`pnpm install`

- 下载指定版本的包并将其添加到 `package.json` 的依赖列表中：

`pnpm add {{module_name}}@{{version}}`

- 下载包并将其添加到 `package.json` 的开发依赖列表中：

`pnpm add {{[-D|--save-dev]}} {{module_name}}`

- 下载包并全局安装：

`pnpm add {{[-g|--global]}} {{module_name}}`

- 卸载包并从 `package.json` 的依赖列表中移除：

`pnpm remove {{module_name}}`

- 打印本地安装的模块树：

`pnpm list`

- 列出顶级全局安装的模块：

`pnpm list {{[-g|--global]}} --depth {{0}}`