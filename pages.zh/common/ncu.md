# ncu

> 查找包依赖项的新版本并检查本地或全局的过期 npm 包。
> `ncu` 仅更新 `package.json` 中的依赖版本。要安装新版本，请运行 `npm install`。
> 更多信息：<https://github.com/raineorshine/npm-check-updates>.

- 列出当前目录中的过期依赖项：

`ncu`

- 列出全局的过期 `npm` 包：

`ncu --global`

- 升级当前目录中的所有依赖项：

`ncu --upgrade`

- 交互式升级当前目录中的依赖项：

`ncu --interactive`

- 列出最多到最新次要版本的过期依赖项：

`ncu --target {{minor}}`

- 列出匹配关键字或正则表达式的过期依赖项：

`ncu --filter {{keyword|/regex/}}`

- 仅列出特定部分的过期依赖项：

`ncu --dep {{dev|optional|peer|prod|packageManager}}`

- 显示帮助：

`ncu --help`