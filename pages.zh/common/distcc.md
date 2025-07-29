# distcc

> 与 `distccd` 搭配使用的分布式 C/C++/ObjC 编译客户端.
> 更多信息：<https://manned.org/distcc>.

- 使用类似 `gcc` 的编译器编译源文件：

`distcc {{gcc}} -c {{path/to/source.c}} -o {{path/to/output.o}}`

- 设置用于分布式编译的远程主机：

`export DISTCC_HOSTS="localhost {{ip1}} {{ip2}}"`

- 使用 `distcc` 和 `make` 并行编译项目：

`make {{[-j|--jobs]}} {{parallel_jobs}} CC="distcc {{gcc}}"`

- 显示当前配置的 `distcc` 主机列表：

`distcc --show-hosts`

- 显示版本信息：

`distcc --version`

- 显示帮助信息：

`distcc --help`
