# julia

> 一种用于技术计算的高层次、高性能动态编程语言。
> 更多信息：<https://docs.julialang.org/en/v1/manual/getting-started/>.

- 启动一个 REPL（交互式 shell）：

`julia`

- 执行一个 Julia 程序并退出：

`julia {{program.jl}}`

- 执行一个带有参数的 Julia 程序：

`julia {{program.jl}} {{参数}}`

- 执行包含 Julia 代码的字符串：

`julia -e '{{julia_代码}}'`

- 执行一段 Julia 代码，并向其传递参数：

`julia -e '{{for x in ARGS; println(x); end}}' {{参数}}`

- 计算一个表达式并打印结果：

`julia -E '{{(1 - cos(pi/4))/2}}'`

- 以多线程模式启动 Julia，使用 N 个线程：

`julia -t {{N}}`
