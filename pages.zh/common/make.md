# make

> 用于控制 Makefile 中描述的目标的任务运行器。
> 主要用于控制从源代码编译可执行文件的过程。
> 更多信息：<https://www.gnu.org/software/make/manual/make.html>。

- 调用 Makefile 中指定的第一个目标（通常命名为 "all"）：

`make`

- 调用特定目标：

`make {{target}}`

- 调用特定目标，同时并行执行 4 个作业：

`make -j{{4}} {{target}}`

- 使用特定的 Makefile：

`make --file {{path/to/file}}`

- 从另一个目录执行 make：

`make --directory {{path/to/directory}}`

- 强制生成一个目标，即使源文件没有更改：

`make --always-make {{target}}`

- 重写 Makefile 中定义的变量：

`make {{target}} {{variable}}={{new_value}}`

- 通过环境重写 Makefile 中定义的变量：

`make --environment-overrides {{target}}`