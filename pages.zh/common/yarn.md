# yarn

> JavaScript 和 Node.js 的包管理器替代品。
> 更多信息：<https://yarnpkg.com>。

- 全局安装一个模块：

`yarn global add {{module_name}}`

- 安装 `package.json` 文件中引用的所有依赖（`install` 是可选的）：

`yarn install`

- 安装一个模块并将其保存为 `package.json` 文件中的依赖（添加 `--dev` 以保存为开发依赖）：

`yarn add {{module_name}}@{{version}}`

- 卸载一个模块并从 `package.json` 文件中删除它：

`yarn remove {{module_name}}`

- 交互式创建 `package.json` 文件：

`yarn init`

- 确定一个模块是否是依赖，并列出其他依赖于它的模块：

`yarn why {{module_name}}`