# mh_metric

> 计算并强制执行 MATLAB 或 Octave 代码的度量标准。
> 更多信息：<https://misshit.org>.

- 打印指定文件的代码度量标准：

`mh_metric {{path/to/file1.m path/to/file2.m ...}}`

- 打印指定的 Octave 文件的代码度量标准：

`mh_metric --octave {{path/to/file1.m path/to/file2.m ...}}`

- 递归地打印指定目录的代码度量标准：

`mh_metric {{path/to/directory}}`

- 打印当前目录的代码度量标准：

`mh_metric`

- 以 HTML 或 JSON 格式打印代码度量标准报告：

`mh_metric --{{html|json}} {{path/to/output_file}}`
