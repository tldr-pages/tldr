# npm install

> 安装 Node 包。
> 更多信息：<https://docs.npmjs.com/cli/commands/npm-install>。

- 安装 `package.json` 中列出的依赖项：

`npm install`

- 下载指定版本的包，并将其添加到 `package.json` 的依赖项列表中：

`npm install {{package_name}}@{{version}}`

- 下载包的最新版本，并将其添加到 `package.json` 的开发依赖项列表中：

`npm install {{package_name}} {{[-D|--save-dev]}}`

- 下载包的最新版本并全局安装：

`npm install {{[-g|--global]}} {{package_name}}`