# 标准

> 用于检查和修复 JavaScript 代码的 JavaScript 标准风格工具。
> 更多信息：<https://standardjs.com>。

- 检查当前目录下的所有 JavaScript 源文件：

`standard`

- 检查特定的 JavaScript 文件：

`standard {{path/to/file1 path/to/file2 ...}}`

- 在检查时应用自动修复：

`standard --fix`

- 声明任何可用的全局变量：

`standard --global {{variable}}`

- 在检查时使用自定义 ESLint 插件：

`standard --plugin {{plugin}}`

- 在检查时使用自定义 JS 解析器：

`standard --parser {{parser}}`

- 在检查时使用自定义 ESLint 环境：

`standard --env {{environment}}`