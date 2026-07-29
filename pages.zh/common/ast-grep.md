# ast-grep

> 使用 AST 模式搜索、lint 和重写代码。
> 更多信息：<https://ast-grep.github.io/reference/cli.html>。

- 在文件中搜索模式：

`ast-grep run {{[-p|--pattern]}} '{{pattern}}' {{路径/到/file}}`

- 在特定语言中搜索模式：

`ast-grep run {{[-p|--pattern]}} '{{pattern}}' {{[-l|--lang]}} {{python}} {{路径/到/目录}}`

- 重写匹配模式的代码：

`ast-grep run {{[-p|--pattern]}} '{{pattern}}' {{[-r|--rewrite]}} '{{replacement}}' {{路径/到/file}}`

- 从配置文件运行规则：

`ast-grep scan {{[-r|--rule]}} {{路径/到/rule.yml}} {{路径/到/目录}}`

- 交互式搜索和重写代码：

`ast-grep run {{[-p|--pattern]}} '{{pattern}}' {{[-i|--interactive]}} {{路径/到/目录}}`

- 显示子命令的帮助：

`ast-grep {{run}} {{[-h|--help]}}`
