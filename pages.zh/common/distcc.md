# distcc

> 与 `distccd` 搭配使用的分布式 C/C++/ObjC 编译客户端.
> 更多信息：<https://manned.org/distcc>.

- 使用类似 `gcc` 的编译器编译源文件：

`distcc {{gcc}} -c {{路径/到/源文件.c}} -o {{路径/到/输出文件.o}}`

- 设置用于分布式编译的远程主机：

`export DISTCC_HOSTS="localhost {{主机IP1 主机IP2 ...}}"`

- 使用 `distcc` 和 `make` 并行编译项目：

`make {{[-j|--jobs]}} {{并行任务数}} CC="distcc {{gcc}}"`

- 显示当前配置的 `distcc` 主机列表：

`distcc --show-hosts`

- 显示帮助：

`distcc --help`

- 显示版本：

`distcc --version`
