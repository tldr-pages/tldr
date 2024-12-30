# ajson

> 在 JSON 对象上执行 JSONPath。
> 更多信息：<https://github.com/spyzhov/ajson>。

- 从文件中读取 JSON 并执行指定的 JSONPath 表达式：

`ajson '{{$..json[?(@.path)]}}' {{path/to/file.json}}`

- 从 `stdin` 中读取 JSON 并执行指定的 JSONPath 表达式：

`cat {{path/to/file.json}} | ajson '{{$..json[?(@.path)]}}'`

- 从 URL 中读取 JSON 并评估指定的 JSONPath 表达式：

`ajson '{{avg($..price)}}' '{{https://example.com/api/}}'`

- 读取一些简单的 JSON 并计算一个值：

`echo '{{3}}' | ajson '{{2 * pi * $}}'`