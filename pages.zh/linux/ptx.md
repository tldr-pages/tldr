# ptx

> 从文本文件生成排列索引。
> 更多信息：<https://www.gnu.org/software/coreutils/ptx>。

- 生成一个排列索引，其中每行的第一个字段是索引引用：

`ptx --references {{path/to/file}}`

- 生成一个自动生成索引引用的排列索引：

`ptx --auto-reference {{path/to/file}}`

- 生成一个固定宽度的排列索引：

`ptx --width={{width_in_columns}} {{path/to/file}}`

- 生成一个带有过滤词列表的排列索引：

`ptx --only-file={{path/to/filter}} {{path/to/file}}`

- 生成一个具有SYSV风格行为的排列索引：

`ptx --traditional {{path/to/file}}`