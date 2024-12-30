# npm 安装

> 安装 Node 包。
> 更多信息：<https://docs.npmjs.com/cli/commands/npm-install>。

- 安装 `package.json` 中列出的依赖：

`npm install`

- 下载特定版本的包并将其添加到 `package.json` 的依赖列表中：

`npm install {{package_name}}@{{version}}`

- 下载最新版本的包并将其添加到 `package.json` 的开发依赖列表中：

`npm install {{package_name}} {{-D|--save-dev}}`

- 下载最新版本的包并全局安装：

`npm install {{-g|--global}} {{package_name}}`