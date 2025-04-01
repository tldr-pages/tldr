# scheme

> MIT Scheme 语言解释器和 REPL（交互式 shell）。
> 更多信息：<https://www.gnu.org/software/mit-scheme/documentation/stable/mit-scheme-user.html#Command_002dLine-Options>。

- 启动一个 REPL（交互式 shell）：

`scheme`

- 运行一个 Scheme 程序（不显示 REPL 输出）：

`scheme --quiet < {{script.scm}}`

- 将一个 Scheme 程序加载到 REPL 中：

`scheme --load {{script.scm}}`

- 将 Scheme 表达式加载到 REPL 中：

`scheme --eval "{{(define foo 'x)}}"`

- 以安静模式启动 REPL：

`scheme --quiet`
