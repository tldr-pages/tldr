# julia

> 一种用于技术计算的高级、高性能动态编程语言。
> 更多信息请访问：<https://docs.julialang.org/en/v1/manual/getting-started/>。

- 启动 REPL（交互式命令行）：

`julia`

- 执行一个 Julia 程序并退出：

`julia {{program.jl}}`

- 执行一个带参数的 Julia 程序：

`julia {{program.jl}} {{arguments}}`

- 评估包含 Julia 代码的字符串：

`julia -e '{{julia_code}}'`

- 评估一段 Julia 代码字符串，并传递参数：

`julia -e '{{for x in ARGS; println(x); end}}' {{arguments}}`

- 评估一个表达式并打印结果：

`julia -E '{{(1 - cos(pi/4))/2}}'`

- 以多线程模式启动 Julia，使用 N 个线程：

`julia -t {{N}}`