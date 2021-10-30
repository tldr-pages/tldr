# make

> Makefile 文件描述目标的任务运行器。
> 通常用于控制源代码中可执行文件的编译。
> 更多信息：<https://www.gnu.org/software/make/manual/make.html>.

- 调用 Makefile 中指定的第一个目标（通常命名为 "all"）：

`make`

- 调用指定目标：

`make {{目标}}`

- 调用一个指定的目标，一次并行执行 4 个作业：

`make -j{{4}} {{目标}}`

- 使用指定的 Makefile 文件：

`make --file {{文件}}`

- 从另一个目录执行 make ：

`make --directory {{文件夹}}`

- 即使源文件未更改，也强制执行目标：

`make --always-make {{目标}}`

- 覆盖在 Makefile 中定义的环境变量：

`make --environment-overrides {{目标}}`
