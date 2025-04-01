# xzdiff

> 在使用 `xz`、`lzma`、`gzip`、`bzip2`、`lzop` 或 `zstd` 压缩的文件上调用 `diff`。
> 所有指定的选项都将直接传递给 `diff`。
> 更多信息：<https://manned.org/xzdiff>.

- 比较两个文件：

`xzdiff {{path/to/file1}} {{path/to/file2}}`

- 比较两个文件，并并排显示差异：

`xzdiff --side-by-side {{path/to/file1}} {{path/to/file2}}`

- 比较两个文件，仅报告它们有差异（不显示具体差异）：

`xzdiff --brief {{path/to/file1}} {{path/to/file2}}`

- 比较两个文件，并在文件相同时报告：

`xzdiff --report-identical-files {{path/to/file1}} {{path/to/file2}}`

- 比较两个文件，使用分页结果显示：

`xzdiff --paginate {{path/to/file1}} {{path/to/file2}}`