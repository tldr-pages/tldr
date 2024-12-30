# 方案

> MIT Scheme 语言解释器和 REPL（交互式外壳）。
> 更多信息：<https://www.gnu.org/software/mit-scheme>。

- 启动 REPL（交互式外壳）：

`scheme`

- 运行一个 scheme 程序（没有 REPL 输出）：

`scheme --quiet < {{script.scm}}`

- 将一个 scheme 程序加载到 REPL 中：

`scheme --load {{script.scm}}`

- 将 scheme 表达式加载到 REPL 中：

`scheme --eval "{{(define foo 'x)}}"`

- 在静默模式下打开 REPL：

`scheme --quiet`