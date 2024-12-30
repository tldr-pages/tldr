# 脚本

> 将所有终端输出记录到文件中。
> 更多信息：<https://manned.org/script>。

- 将新会话记录到当前目录下名为 `typescript` 的文件中：

`script`

- 将新会话记录到自定义文件路径：

`script {{path/to/session.out}}`

- 将新会话记录，并追加到现有文件中：

`script -a {{path/to/session.out}}`

- 记录时间信息（数据输出到 `stderr`）：

`script -t 2> {{path/to/timing_file}}`

- 数据发生时立即写出：

`script -f {{path/to/file}}`