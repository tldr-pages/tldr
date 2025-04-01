# checksec

> 检查可执行文件的安全属性。
> 更多信息：<https://github.com/slimm609/checksec.sh>.

- 列出可执行二进制文件的安全属性：

`checksec --file={{path/to/binary}}`

- 递归列出目录中所有可执行文件的安全属性：

`checksec --dir={{path/to/directory}}`

- 列出进程的安全属性：

`checksec --proc={{pid}}`

- 列出运行中内核的安全属性：

`checksec --kernel`