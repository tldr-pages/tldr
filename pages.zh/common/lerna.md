# lerna

> 管理包含多个包的 JavaScript 项目。
> 更多信息：<https://lerna.js.org>。

- 初始化项目文件（`lerna.json`，`package.json`，`.git` 等）：

`lerna init`

- 安装每个包的所有外部依赖项，并为本地依赖项创建符号链接：

`lerna bootstrap`

- 运行每个包含在 `package.json` 中的特定脚本：

`lerna run {{script}}`

- 在每个包中执行任意 shell 命令：

`lerna exec -- {{ls}}`

- 发布自上次发布以来发生更改的所有包：

`lerna publish`