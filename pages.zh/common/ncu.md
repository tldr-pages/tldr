# ncu

> 查找包依赖的更新版本，并检查本地或全局的过期 npm 包。
> `ncu` 仅更新 `package.json` 中的依赖版本。要安装新版本，请在之后运行 `npm install`。
> 更多信息：<https://github.com/raineorshine/npm-check-updates>。

- 列出当前目录中的过期依赖：

`ncu`

- 列出全局的过期 `npm` 包：

`ncu --global`

- 升级当前目录中的所有依赖：

`ncu --upgrade`

- 交互式升级当前目录中的依赖：

`ncu --interactive`

- 列出过期依赖，直到最高的次版本：

`ncu --target {{minor}}`

- 列出与关键字或正则表达式匹配的过期依赖：

`ncu --filter {{keyword|/regex/}}`

- 仅列出特定部分的过期依赖：

`ncu --dep {{dev|optional|peer|prod|packageManager}}`

- 显示帮助信息：

`ncu --help`