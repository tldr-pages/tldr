# npm

> JavaScript 和 Node.js 包管理器。
> 管理 Node.js 项目及其模块依赖关系。
> 更多信息：<https://www.npmjs.com>。

- 创建一个具有默认值的 `package.json` 文件（省略 `--yes` 以交互方式进行）：

`npm init {{-y|--yes}}`

- 下载 `package.json` 中列出的所有依赖包：

`npm install`

- 下载特定版本的包并将其添加到 `package.json` 的依赖列表中：

`npm install {{package_name}}@{{version}}`

- 下载包的最新版本并将其添加到 `package.json` 的开发依赖列表中：

`npm install {{package_name}} {{-D|--save-dev}}`

- 下载包的最新版本并全局安装：

`npm install {{-g|--global}} {{package_name}}`

- 卸载一个包并将其从 `package.json` 的依赖列表中移除：

`npm uninstall {{package_name}}`

- 列出所有本地安装的依赖：

`npm list`

- 列出所有顶级全局安装的包：

`npm list {{-g|--global}} --depth {{0}}`