# yarn

> JavaScript 和 Node.js package manager 的一个替代。
> 更多信息：<https://yarnpkg.com>.

- 全局安装一个模块：

`yarn global add {{module_name}}`

- 安装 `package.json` 中指定的依赖（`install` 命令是可选的 -- 你可以直接输入`yarn`）：

`yarn install`

- 安装一个模块并将其写入 `package.json` 中的依赖项（增加 `--dev` 来作为开发依赖写入）：

`yarn add {{module_name}}@{{version}}`

- 卸载一个模块并将其从 `package.json` 的依赖项中移除：

`yarn remove {{module_name}}`

- 交互式地创建一个 `package.json` 文件：

`yarn init`

- 确认一个模块是否是一个依赖项并且列出依赖其的模块：

`yarn why {{module_name}}`
