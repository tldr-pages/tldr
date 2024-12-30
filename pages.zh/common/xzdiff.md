# xzdiff

> 对使用 `xz`、`lzma`、`gzip`、`bzip2`、`lzop` 或 `zstd` 压缩的文件调用 `diff`。
> 所有指定的选项都直接传递给 `diff`。
> 更多信息：<https://manned.org/xzdiff>。

- 比较两个文件：

`xzdiff {{path/to/file1}} {{path/to/file2}}`

- 比较两个文件，显示并排的差异：

`xzdiff --side-by-side {{path/to/file1}} {{path/to/file2}}`

- 比较两个文件，仅报告它们不同（不显示具体的不同内容）：

`xzdiff --brief {{path/to/file1}} {{path/to/file2}}`

- 比较两个文件，并报告文件是否相同：

`xzdiff --report-identical-files {{path/to/file1}} {{path/to/file2}}`

- 使用分页结果比较两个文件：

`xzdiff --paginate {{path/to/file1}} {{path/to/file2}}`