# pw-profiler

> 对本地或远程实例进行性能分析。
> 更多信息：<https://docs.pipewire.org/page_man_pw-profiler_1.html>。

- 对默认实例进行性能分析，并将日志记录到 `profile.log`（同时会生成 `gnuplot` 文件和 HTML 文件以可视化结果）：

`pw-profiler`

- 更改日志输出文件：

`pw-profiler {{[-o|--output]}} {{path/to/file.log}}`

- 对远程实例进行性能分析：

`pw-profiler {{[-r|--remote]}} {{remote_name}}`

- 显示帮助信息：

`pw-profiler {{[-h|--help]}}`
