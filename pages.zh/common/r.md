# R

> R语言解释器。
> 更多信息：<https://www.r-project.org>。

- 启动REPL（交互式命令行）：

`R`

- 以原生模式启动R（即一个空白会话，结束时不保存工作空间）：

`R --vanilla`

- 执行一个文件：

`R -f {{path/to/file.R}}`

- 执行一个R表达式然后退出：

`R -e {{expr}}`

- 使用调试器运行R：

`R -d {{debugger}}`

- 检查来自软件包源的R包：

`R CMD check {{path/to/package_source}}`

- 显示版本：

`R --version`