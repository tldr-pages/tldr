# standard

> 用于检查和修复 JavaScript 代码的 JavaScript 标准风格工具。
> 更多信息：<https://standardjs.com>.

- 检查当前目录中所有的 JavaScript 源文件：

`standard`

- 检查特定的 JavaScript 文件：

`standard {{path/to/file1 path/to/file2 ...}}`

- 在检查时自动修复问题：

`standard --fix`

- 声明可用的全局变量：

`standard --global {{variable}}`

- 在检查时使用自定义 ESLint 插件：

`standard --plugin {{plugin}}`

- 在检查时使用自定义 JavaScript 解析器：

`standard --parser {{parser}}`

- 在检查时使用自定义 ESLint 环境：

`standard --env {{environment}}`