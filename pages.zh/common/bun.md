# bun

> JavaScript 运行时和工具包。
> 包括一个打包器、一个测试运行器和一个包管理器。
> 更多信息：<https://bun.sh>。

- 运行一个 JavaScript 文件或 `package.json` 脚本：

`bun run {{path/to/file|script_name}}`

- 运行单元测试：

`bun test`

- 下载并安装 `package.json` 中列出的所有依赖包：

`bun install`

- 向 `package.json` 添加一个依赖项：

`bun add {{module_name}}`

- 从 `package.json` 中移除一个依赖项：

`bun remove {{module_name}}`

- 在当前目录中创建一个新的 Bun 项目：

`bun init`

- 启动 REPL（交互式 shell）：

`bun repl`

- 将 Bun 升级到最新版本：

`bun upgrade`