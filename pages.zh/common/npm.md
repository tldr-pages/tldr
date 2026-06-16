# npm

> JavaScript 和 Node.js 软件包管理器。
> 管理 Node.js 项目及其模块依赖项。
> 此命令也有关于其子命令的文件，例如：`install`, `run`.
> 更多信息：<https://docs.npmjs.com/cli/npm/>。

- 使用默认值创建一个 `package.json` 文件（省略 `--yes` 来以交互方式执行）：

`npm init {{[-y|--yes]}}`

- 下载 `package.json` 中列出的所有依赖项软件包：

`npm {{[i|install]}}`

- 下载软件包的特定版本并将其添加到 `package.json` 中的依赖项列表中：

`npm {{[i|install]}} {{软件包名}}@{{版本号}}`

- 下载软件包的最新版本并将其添加到 `package.json` 中的开发依赖项列表中：

`npm {{[i|install]}} {{软件包名}} {{[-D|--save-dev]}}`

- 下载软件包的最新版本并全局安装（用 `npm config set prefix` 设置安装位置）：

`npm {{[i|install]}} {{软件包名}} {{[-g|--global]}}`

- 卸载软件包并将其从 `package.json` 中的依赖项列表中删除：

`npm {{[r|uninstall]}} {{软件包名}}`

- 列出所有本地安装的依赖项：

`npm {{[ls|list]}}`

- 列出所有顶层全局安装的软件包：

`npm {{[ls|list]}} {{[-g|--global]}} --depth {{0}}`
