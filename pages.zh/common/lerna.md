# lerna

> 管理具有多个包的 JavaScript 项目。
> 更多信息：<https://lerna.js.org>。

- 初始化项目文件（`lerna.json`，`package.json`，`.git` 等）：

`lerna init`

- 安装每个包的所有外部依赖并将本地依赖符号链接在一起：

`lerna bootstrap`

- 为每个在其 `package.json` 中包含特定脚本的包运行该脚本：

`lerna run {{script}}`

- 在每个包中执行任意 shell 命令：

`lerna exec -- {{ls}}`

- 发布自上次发布以来已更改的所有包：

`lerna publish`