# 补丁

> 用差异文件（diff 文件）修补一个文件（或多个文件）。
> 请注意，差异文件应通过 `diff` 命令生成。
> 更多信息：<https://manned.org/patch>。

- 使用差异文件应用补丁（文件名必须包含在差异文件中）：

`patch < {{patch.diff}}`

- 对特定文件应用补丁：

`patch {{path/to/file}} < {{patch.diff}}`

- 将补丁应用到一个文件，并将结果写入不同的文件：

`patch {{path/to/input_file}} -o {{path/to/output_file}} < {{patch.diff}}`

- 对当前目录应用补丁：

`patch -p1 < {{patch.diff}}`

- 应用补丁的反向补丁：

`patch -R < {{patch.diff}}`