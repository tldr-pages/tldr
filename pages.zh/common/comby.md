# comby

> 结构化代码搜索和替换工具，支持多种语言。
> 更多信息：<https://github.com/comby-tools/comby>。

- 匹配和重写模板，并打印更改：

`comby '{{assert_eq!(:[a], :[b])}}' '{{assert_eq!(:[b], :[a])}}' {{.rs}}`

- 带重写属性的匹配和重写：

`comby '{{assert_eq!(:[a], :[b])}}' '{{assert_eq!(:[b].Capitalize, :[a])}}' {{.rs}}`

- 原地匹配和重写：

`comby -in-place '{{match_pattern}}' '{{rewrite_pattern}}'`

- 仅执行匹配并打印匹配项：

`comby -match-only '{{match_pattern}}' ""`