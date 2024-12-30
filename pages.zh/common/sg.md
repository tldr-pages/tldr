# sg

> Ast-grep 是一个用于代码结构搜索、代码检查和重写的工具。
> 更多信息：<https://ast-grep.github.io/guide/introduction.html>。

- 使用交互模式扫描可能的查询：

`sg scan --interactive`

- 使用模式在当前目录中重写代码：

`sg run --pattern '{{foo}}' --rewrite '{{bar}}' --lang {{python}}`

- 可视化可能的更改而不应用它们：

`sg run --pattern '{{useState<number>($A)}}' --rewrite '{{useState($A)}}' --lang {{typescript}}`

- 将结果输出为 JSON，使用 `jq` 提取信息，并使用 `jless` 进行交互式查看：

`sg run --pattern '{{Some($A)}}' --rewrite '{{None}}' --json | jq '{{.[].replacement}}' | jless`