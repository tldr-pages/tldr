# npm

> JavaScript 和 Node.js 包管理器。
> 管理 Node.js 项目及其模块依赖项。
> 更多信息：<https://docs.npmjs.com/cli/npm>.

- 使用默认值创建一个 `package.json` 文件（省略 `--yes` 以交互方式执行）：

`npm init {{[-y|--yes]}}`

- 下载 `package.json` 中列出的所有依赖项包：

`npm install`

- 下载包的特定版本并将其添加到 `package.json` 中的依赖项列表中：

`npm install {{包名}}@{{版本号}}`

- 下载包的最新版本并将其添加到 `package.json` 中的开发依赖项列表中：

`npm install {{包名}} {{[-D|--save-dev]}}`

- 下载包的最新版本并全局安装：

`npm install {{[-g|--global]}} {{包名}}`

- 卸载包并将其从 `package.json` 中的依赖项列表中删除：

`npm uninstall {{包名}}`

- 列出所有本地安装的依赖项：

`npm list`

- 列出所有顶级全局安装的包：

`npm list {{[-g|--global]}} --depth {{0}}`
