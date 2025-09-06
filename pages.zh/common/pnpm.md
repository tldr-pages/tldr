# pnpm

> 快速、节省磁盘空间的 Node.js 包管理器。
> 管理 Node.js 项目和其模块依赖。
> 更多信息：<https://pnpm.io/pnpm-cli>.

- 创建 `package.json` 文件：

`pnpm init`

- 下载 `package.json` 中列出的所有依赖包：

`pnpm install`

- 下载指定版本的包并添加至 `package.json` 的依赖列表：

`pnpm add {{模块名}}@{{版本}}`

- 下载包并添加至 `package.json` 的开发依赖列表：

`pnpm add {{[-D|--save-dev]}} {{模块名}}`

- 下载并全局安装包：

`pnpm add {{[-g|--global]}} {{模块名}}`

- 卸载包并将其从 `package.json` 的依赖列表删除：

`pnpm remove {{模块名}}`

- 打印本地安装的模块树：

`pnpm list`

- 列出顶级全局安装的模块：

`pnpm list {{[-g|--global]}} --depth {{0}}`
