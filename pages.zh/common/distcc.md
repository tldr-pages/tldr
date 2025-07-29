# distcc

> 与 `distccd` 搭配使用的分布式 C/C++/ObjC 编译客户端.
> 更多信息：<https://manned.org/distcc>.

- 使用類似 `gcc` 的編譯器編譯源文件：

`distcc {{gcc}} -c {{路徑/到/源文件.c}} -o {{路徑/到/輸出文件.o}}`

- 設置用於分布式編譯的遠程主機：

`export DISTCC_HOSTS="localhost {{主機IP1}} {{主機IP2}}"`

- 使用 `distcc` 和 `make` 並行編譯項目：

`make {{[-j|--jobs]}} {{並行任務數}} CC="distcc {{gcc}}"`

- 顯示當前配置的 `distcc` 主機列表：

`distcc --show-hosts`

- 顯示版本信息：

`distcc --version`

- 顯示幫助信息：

`distcc --help`
