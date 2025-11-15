# ajson

> 对 JSON 对象执行 JSONPath 操作。
> 更多信息：<https://github.com/spyzhov/ajson>.

- 从文件中读取 JSON 并执行指定的 JSONPath 表达式：

`ajson '{{$..json[?(@.path)]}}' {{路径/到/文件.json}}`

- 从标准输入中读取 JSON 并执行指定的 JSONPath 表达式：

`cat {{路径/到/文件.json}} | ajson '{{$..json[?(@.path)]}}'`

- 从 URL 中获取 JSON 并计算指定的 JSONPath 表达式：

`ajson '{{avg($..price)}}' '{{https://example.com/api/}}'`

- 读取一些简单的 JSON 并计算一个值：

`echo '{{3}}' | ajson '{{2 * pi * $}}'`
