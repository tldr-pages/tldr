# pw-profiler

> 对本地或远程实例进行分析。
> 更多信息请访问: <https://docs.pipewire.org/page_man_pw-profiler_1.html>。

- 分析默认实例，将日志记录到 `profile.log`（同时生成 `gnuplot` 文件和用于结果可视化的 HTML 文件）：

`pw-profiler`

- 更改日志输出文件：

`pw-profiler --output {{path/to/file.log}}`

- 分析远程实例：

`pw-profiler --remote {{remote_name}}`

- 显示帮助信息：

`pw-profiler --help`