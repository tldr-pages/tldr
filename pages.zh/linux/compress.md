# compress

> 使用 Unix `compress` 命令压缩文件。
> 更多信息：<https://manned.org/compress.1>.

- 压缩指定文件：

`compress {{path/to/file1 path/to/file2 ...}}`

- 压缩指定文件，忽略不存在的文件：

`compress -f {{path/to/file1 path/to/file2 ...}}`

- 指定最大压缩位数（9-16 位）：

`compress -b {{bits}}`

- 输出到 `标准输出`（不更改文件）：

`compress -c {{path/to/file}}`

- 解压缩文件（功能类似于 `uncompress`）：

`compress -d {{path/to/file}}`

- 显示压缩百分比：

`compress -v {{path/to/file}}`