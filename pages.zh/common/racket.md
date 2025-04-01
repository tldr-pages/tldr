# racket

> Racket 语言解释器。
> 更多信息：<https://racket-lang.org>。

- 启动一个 REPL（交互式 shell）：

`racket`

- 执行 Racket 脚本：

`racket {{path/to/script.rkt}}`

- 执行 Racket 表达式：

`racket --eval "{{expression}}"`

- 作为脚本运行模块（终止选项列表）：

`racket --lib {{module_name}} --main {{arguments}}`

- 启动 `typed/racket` hashlang 的 REPL（交互式 shell）：

`racket -I typed/racket`
